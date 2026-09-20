from typing import List, Dict, Any
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from project.services.qdrant_retrieval import KnowledgeRetriever

class ExtractedEvidence(BaseModel):
    driver: str = Field(description="The candidate driver being evaluated.")
    supporting_claims: List[str] = Field(description="Exact scientific claims from the text supporting the relationship.")
    source_name: str = Field(description="Name of the scientific source organization.")
    url: str = Field(description="URL of the source.")
    metadata: Dict[str, Any] = Field(description="Preserved document metadata.")

def retrieve_evidence_for_drivers(
    candidate_drivers: List[str],
    affected_metrics: List[str],
    biodiversity_outcome: str,
    retriever: KnowledgeRetriever,
    model_name: str = "openai/gpt-oss-20b"
) -> List[ExtractedEvidence]:
    """
    Retrieves relevant scientific evidence from the Qdrant vector database.
    Runs vector retrieval directly on affected metrics and biodiversity outcome first,
    as well as candidate drivers if provided.
    Preserves source metadata with 100% fidelity.
    """
    llm = ChatGroq(model=model_name, temperature=0.0)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a strict scientific data extractor. Your job is to extract evidence that supports "
         "the relationship between the provided driver/context, the affected metrics, and the biodiversity outcome.\n\n"
         "CRITICAL RULES:\n"
         "- ONLY use the provided retrieved context. Prioritize the project's existing scientific sources.\n"
         "- NEVER invent studies, sources, measurements, or numerical claims.\n"
         "- If the context does not support the reasoning, return an empty list for supporting_claims.\n"
         "- Preserve the exact source organization and URL provided in the context.\n\n"
         "=== RETRIEVED CONTEXT ===\n{context}"
        ),
        ("human", "Driver/Context: {driver}\nAffected Metrics: {metrics}\nBiodiversity Outcome: {outcome}")
    ])
    
    chain = prompt | llm.with_structured_output(ExtractedEvidence)
    
    # 1. Always run Qdrant retrieval for general metrics and biodiversity outcome
    search_targets = []
    if candidate_drivers:
        for driver in candidate_drivers:
            search_targets.append((driver, f"Impact of {driver} on {', '.join(affected_metrics)} leading to {biodiversity_outcome}"))
    
    # Add baseline retrieval for affected metrics to guarantee Qdrant execution
    search_targets.append(("General Environmental Driver", f"Impact of environmental degradation on {', '.join(affected_metrics)} leading to {biodiversity_outcome}"))
    
    all_docs_with_drivers = []
    seen_content = set()

    for driver_label, query in search_targets:
        docs = retriever.retrieve(query, k=3)
        for doc in docs:
            if doc.page_content not in seen_content:
                seen_content.add(doc.page_content)
                all_docs_with_drivers.append((driver_label, doc))
                
    all_evidence = []
    
    for driver_label, doc in all_docs_with_drivers:
        org_name = doc.metadata.get("organization") or doc.metadata.get("source") or "Unknown Organization"
        doc_url = doc.metadata.get("url") or doc.metadata.get("URL") or ""
        
        context_text = (
            f"Content: {doc.page_content}\n"
            f"Organization: {org_name}\n"
            f"URL: {doc_url}"
        )
        
        try:
            extracted = chain.invoke({
                "context": context_text,
                "driver": driver_label,
                "metrics": ", ".join(affected_metrics),
                "outcome": biodiversity_outcome
            })
            
            # Strictly enforce metadata preservation in code
            extracted.source_name = org_name
            extracted.url = doc_url
            extracted.metadata = doc.metadata
            
            if extracted.supporting_claims:
                all_evidence.append(extracted)
        except Exception:
            continue
            
    return all_evidence
