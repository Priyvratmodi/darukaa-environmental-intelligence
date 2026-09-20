from typing import Dict, Any
from project.schemas.problem import ProblemUnderstanding
from project.services.problem_understanding import analyze_problem
from project.services.metric_knowledge import identify_missing_metrics
from project.services.state_manager import get_conversation_state, update_conversation_state
from project.services.reasoning import query_neo4j_for_drivers, analyze_multiple_metrics
from project.services.evidence_retrieval import retrieve_evidence_for_drivers
from project.services.recommendation import generate_recommendations
from project.services.qdrant_retrieval import KnowledgeIndexer, KnowledgeRetriever
from project.services.explainability import build_evidence_chain

def run_analysis_pipeline(session_id: str, query: str) -> Dict[str, Any]:
    """
    Executes the full Darukaa analysis pipeline sequentially.
    Returns early if required metrics are missing.
    """
    # 1. Understand problem
    problem_dict = analyze_problem(query)
    problem = ProblemUnderstanding(**problem_dict)
    new_observations = problem.observed_values or problem.mentioned_factors or [query]
    metric_names = problem.mentioned_factors or []
    
    # Retrieve existing state and merge metrics across turns
    existing_state = get_conversation_state(session_id)
    combined_metrics = list(dict.fromkeys((existing_state.provided_metrics or []) + new_observations))
    observations = combined_metrics
    
    # Store updated state
    update_conversation_state(session_id, {
        "original_user_problem": existing_state.original_user_problem or problem.problem_statement,
        "species_ecosystem": existing_state.species_ecosystem or problem.affected_entity,
        "location": existing_state.location or problem.location,
        "provided_metrics": combined_metrics
    })
    
    # 2 & 3. Identify required metrics & detect missing metrics
    missing_metrics = identify_missing_metrics(problem, observations)
    
    if missing_metrics:
        update_conversation_state(session_id, {"missing_metrics": missing_metrics})
        return {
            "status": "requires_more_info",
            "missing_metrics": missing_metrics,
            "message": "Additional environmental metrics are required to proceed."
        }
        
    # Initialize retrieval dependencies
    indexer = KnowledgeIndexer()
    indexer.ingest() # Must populate the in-memory Qdrant instance
    retriever = KnowledgeRetriever(indexer.vector_store)
    
    # 4 & 5. Analyze observations and retrieve graph relationships
    graph_results = query_neo4j_for_drivers(metric_names or observations)
    candidate_drivers = [res['driver'] for res in graph_results]
    
    update_conversation_state(session_id, {"candidate_drivers": candidate_drivers})
    
    # 6. Retrieve scientific evidence (Qdrant retrieval ALWAYS runs first)
    biodiversity_outcome = problem.suspected_outcome or "ecological impact"
    evidence_list = retrieve_evidence_for_drivers(
        candidate_drivers=candidate_drivers,
        affected_metrics=observations,
        biodiversity_outcome=biodiversity_outcome,
        retriever=retriever
    )
    
    update_conversation_state(session_id, {
        "retrieved_evidence": [e.model_dump() for e in evidence_list]
    })
    
    # 7. Multi-metric reasoning
    reasoning_result = analyze_multiple_metrics(
        observations=observations, 
        qdrant_retriever=retriever, 
        graph_results=graph_results,
        extracted_evidence=evidence_list
    )
    
    # 8. Generate recommendations
    recommendation_plan = generate_recommendations(
        user_observations=observations,
        reasoning_result=reasoning_result,
        extracted_evidence=evidence_list
    )
    
    # 9. Explainability
    evidence_chain = build_evidence_chain(
        problem=problem,
        observations=observations,
        reasoning_result=reasoning_result,
        extracted_evidence=evidence_list,
        recommendation_plan=recommendation_plan
    )
    
    return {
        "status": "complete",
        "problem_understanding": problem_dict,
        "evidence_chain": evidence_chain,
        "reasoning": reasoning_result.model_dump(),
        "recommendations": recommendation_plan.model_dump()
    }
