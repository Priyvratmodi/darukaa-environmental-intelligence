from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from project.services.causal_graph import get_causal_graph
from project.services.qdrant_retrieval import KnowledgeRetriever

class DriverAnalysis(BaseModel):
    driver: str = Field(description="Name of the candidate underlying driver")
    explained_metrics: List[str] = Field(description="List of observations explained by this driver")
    is_primary: bool = Field(description="Whether this is a primary driver or contributing driver. MUST ONLY be true if both observed quantitative data and retrieved scientific evidence directly support it as the primary cause. Otherwise set to false.")
    evidence_strength: str = Field(description="Strength of evidence: Strong, Moderate, or Weak")
    reasoning: str = Field(description="Explanation of how the driver connects the metrics. MUST explicitly label [Observed Data], [Scientific Evidence], [System Inference], and [Uncertainty]. If no retrieved scientific source supports a claim, label it as [UNSUPPORTED CLAIM].")

class MultiMetricReasoning(BaseModel):
    relationships_identified: str = Field(description="Relationships found between the observed metrics")
    candidate_drivers: List[DriverAnalysis] = Field(description="Candidate drivers explaining the observations")

def query_neo4j_for_drivers(observations: List[str]) -> List[dict]:
    """Finds drivers in Neo4j that causally link to the observed metrics.
    Returns an empty list if Neo4j is unavailable, allowing the pipeline to degrade gracefully.
    """
    try:
        graph = get_causal_graph()
        
        query = """
        MATCH (d:Driver)-[r*1..3]->(m)
        WHERE toLower(m.name) IN $observations
        WITH d, collect(DISTINCT m.name) as explained_metrics, count(DISTINCT m.name) as coverage
        RETURN d.name as driver, explained_metrics, coverage
        ORDER BY coverage DESC
        """
        
        obs_lower = [obs.lower() for obs in observations]
        results = graph.query(query, params={"observations": obs_lower})
        return results
    except Exception:
        # Neo4j unavailable — pipeline continues with Qdrant-only evidence
        return []

def analyze_multiple_metrics(
    observations: List[str], 
    qdrant_retriever: KnowledgeRetriever,
    model_name: str = "openai/gpt-oss-20b",
    graph_results: List[dict] = None,
    extracted_evidence: List['ExtractedEvidence'] = None
) -> MultiMetricReasoning:
    """
    Analyzes multiple observations collectively to find underlying drivers.
    Uses Neo4j for causal graph relationships and Qdrant for scientific evidence.
    """
    
    # 1. Fetch graph connections
    if graph_results is None:
        graph_results = query_neo4j_for_drivers(observations)
    graph_context = "\n".join([
        f"Driver '{r['driver']}' explains: {', '.join(r['explained_metrics'])} (Coverage: {r['coverage']})"
        for r in graph_results
    ])
    
    # 2. Fetch retrieved knowledge for context
    if extracted_evidence:
        doc_context = "\n\n".join([
            f"Driver: {e.driver}\nSource: {e.source_name} ({e.url})\nClaims: {'; '.join(e.supporting_claims)}"
            for e in extracted_evidence
        ])
    else:
        query_text = " ".join(observations)
        retrieved_docs = qdrant_retriever.retrieve(query_text, k=4)
        doc_context = "\n\n".join([
            f"Source: {doc.metadata.get('organization', 'Scientific Source')} ({doc.metadata.get('url', '')})\nContent: {doc.page_content}"
            for doc in retrieved_docs
        ])
    
    # 3. Reasoning with LLM
    llm = ChatGroq(model=model_name, temperature=0.0)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are an expert environmental reasoning engine. "
         "Given multiple environmental observations, do not treat each metric as a separate problem. "
         "Instead, identify relationships between them and determine common candidate underlying drivers.\n\n"
         "CRITICAL ANTI-HALLUCINATION SAFEGUARDS:\n"
         "- PRESERVE all quantitative metric values and units from the observations.\n"
         "- NEVER invent scientific sources or measurements.\n"
         "- EVERY scientific claim mentioned must be explicitly backed by a source from the retrieved scientific knowledge. If no source is retrieved for a claim, mark it as [UNSUPPORTED CLAIM].\n"
         "- DO NOT label a driver as 'primary' (is_primary=true) unless both the quantitative observations and retrieved scientific evidence explicitly support it as the main cause.\n"
         "- CLEARLY distinguish between: [Observed Data], [Scientific Evidence], [System Inference], and [Uncertainty].\n"
         "- Explain which drivers account for multiple observations.\n"
         "- Preserve uncertainty when evidence is weak.\n"
         "- Do NOT generate final recommendations or interventions yet.\n\n"
         "=== GRAPH CONNECTIONS ===\n{graph_context}\n\n"
         "=== RETRIEVED SCIENTIFIC KNOWLEDGE ===\n{doc_context}"
        ),
        ("human", "Observations to analyze: {observations}")
    ])
    
    chain = prompt | llm.with_structured_output(MultiMetricReasoning)
    result = chain.invoke({
        "observations": ", ".join(observations),
        "graph_context": graph_context or "No graph connections found.",
        "doc_context": doc_context or "No retrieved scientific evidence found."
    })
    
    return result
