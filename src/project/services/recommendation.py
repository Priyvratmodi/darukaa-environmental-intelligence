from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from project.services.reasoning import MultiMetricReasoning
from project.services.evidence_retrieval import ExtractedEvidence

class ScientificEvidenceDetail(BaseModel):
    source: str = Field(description="Name of the source organization")
    url: str = Field(description="URL of the source")
    claims: List[str] = Field(description="Specific claims supporting the recommendation")

class EvidenceBackedRecommendation(BaseModel):
    recommendation: str = Field(description="Specific, actionable intervention to implement.")
    why_it_works: str = Field(description="Explanation of how the intervention addresses the underlying drivers. MUST explicitly label [Observed Data], [Scientific Evidence], [System Inference], and [Uncertainty].")
    impacted_metrics: List[str] = Field(description="The environmental metrics expected to improve.")
    expected_time_horizon: str = Field(description="Estimated time to observe measurable results (e.g., '1-3 years').")
    scientific_evidence: List[ScientificEvidenceDetail] = Field(description="Curated evidence supporting this intervention.")
    confidence: str = Field(description="Confidence level (High, Medium, Low) based on evidence strength.")

class RecommendationPlan(BaseModel):
    recommendations: List[EvidenceBackedRecommendation]

def generate_recommendations(
    user_observations: List[str],
    reasoning_result: MultiMetricReasoning,
    extracted_evidence: List[ExtractedEvidence],
    model_name: str = "openai/gpt-oss-20b"
) -> RecommendationPlan:
    """
    Generates evidence-backed recommendations targeting the root causal drivers, 
    grounded strictly in the provided scientific evidence.
    """
    llm = ChatGroq(model=model_name, temperature=0.0)
    
    # Format drivers and relationships
    drivers_text = "\n".join([
        f"- Driver: {d.driver} (Primary: {d.is_primary}, Evidence: {d.evidence_strength})\n"
        f"  Explains: {', '.join(d.explained_metrics)}\n"
        f"  Reasoning: {d.reasoning}"
        for d in reasoning_result.candidate_drivers
    ])
    
    # Format scientific evidence explicitly
    evidence_text = "\n\n".join([
        f"Driver: {e.driver}\nSource: {e.source_name} ({e.url})\nClaims: {'; '.join(e.supporting_claims)}"
        for e in extracted_evidence
    ])
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are an expert environmental intervention planner. Your task is to generate actionable, "
         "specific recommendations to resolve the environmental problems based on the identified causal drivers.\n\n"
         "CRITICAL ANTI-HALLUCINATION SAFEGUARDS:\n"
         "- NEVER generate generic advice. Recommendations must specifically target the identified drivers.\n"
         "- NEVER invent scientific sources, studies, measurements, or causal relationships.\n"
         "- NEVER present assumptions as facts or give unsupported numerical claims.\n"
         "- CLEARLY distinguish between: [Observed Data], [Scientific Evidence], [System Inference], and [Uncertainty].\n"
         "- Use ONLY the provided scientific evidence to justify why it works.\n"
         "- If evidence is weak or absent, explicitly state the [Uncertainty] and reflect it in the confidence level.\n\n"
         "=== IDENTIFIED CAUSAL RELATIONSHIPS ===\n{relationships_text}\n\n"
         "=== UNDERLYING DRIVERS ===\n{drivers_text}\n\n"
         "=== RETRIEVED SCIENTIFIC EVIDENCE ===\n{evidence_text}"
        ),
        ("human", "User Observations: {observations}\nGenerate the evidence-backed recommendation plan.")
    ])
    
    chain = prompt | llm.with_structured_output(RecommendationPlan)
    
    result = chain.invoke({
        "observations": ", ".join(user_observations),
        "relationships_text": reasoning_result.relationships_identified,
        "drivers_text": drivers_text,
        "evidence_text": evidence_text or "No specific scientific evidence provided."
    })
    
    # Post-process: Guarantee that retrieved evidence is attached to recommendations if missing
    if extracted_evidence:
        for rec in result.recommendations:
            if not rec.scientific_evidence:
                matching_sources = []
                for ev in extracted_evidence:
                    detail = ScientificEvidenceDetail(
                        source=ev.source_name,
                        url=ev.url,
                        claims=ev.supporting_claims
                    )
                    if detail not in matching_sources:
                        matching_sources.append(detail)
                rec.scientific_evidence = matching_sources
                
    return result
