from typing import Dict, Any, List
from project.schemas.problem import ProblemUnderstanding
from project.services.metric_knowledge import get_relevant_metrics
from project.services.reasoning import MultiMetricReasoning
from project.services.evidence_retrieval import ExtractedEvidence
from project.services.recommendation import RecommendationPlan

def build_evidence_chain(
    problem: ProblemUnderstanding,
    observations: List[str],
    reasoning_result: MultiMetricReasoning,
    extracted_evidence: List[ExtractedEvidence],
    recommendation_plan: RecommendationPlan
) -> Dict[str, Any]:
    """
    Builds a transparent evidence chain mapping the progression from 
    Problem to Recommendation without exposing internal LLM chain-of-thought.
    """
    
    required_metrics = [m.name for m in get_relevant_metrics(problem)]
    candidate_drivers = [d.driver for d in reasoning_result.candidate_drivers]
    
    # Deduplicate sources while preserving order
    sources = []
    for ev in extracted_evidence:
        if ev.source_name not in sources:
            sources.append(ev.source_name)
            
    recommendations = [r.recommendation for r in recommendation_plan.recommendations]
    
    evidence_chain = {
        "Problem": problem.problem_statement,
        "Required metrics": required_metrics,
        "Observations": observations,
        "Candidate driver": candidate_drivers,
        "Causal relationship": reasoning_result.relationships_identified,
        "Scientific source": sources,
        "Recommendation": recommendations
    }
    
    return evidence_chain
