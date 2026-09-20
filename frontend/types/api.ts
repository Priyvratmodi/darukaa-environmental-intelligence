// ─── Request Types ─────────────────────────────────────────────────────────────

/** POST /analyze request body */
export interface AnalysisRequest {
  session_id: string;
  query: string;
}

// ─── Domain Enum ───────────────────────────────────────────────────────────────

export type Domain =
  | 'soil'
  | 'water'
  | 'biodiversity'
  | 'land_use'
  | 'climate'
  | 'pollution'
  | 'agriculture'
  | 'habitat'
  | 'species'
  | 'ecosystem'
  | 'unknown';

// ─── Problem Understanding ─────────────────────────────────────────────────────
// Mirrors project/src/project/schemas/problem.py :: ProblemUnderstanding

export interface ProblemUnderstanding {
  problem_statement: string;
  domain: Domain;
  affected_entity: string | null;
  ecosystem_context: string | null;
  location: string | null;
  suspected_outcome: string | null;
  mentioned_factors: string[];
  observed_values: string[];
}

// ─── Evidence Chain ────────────────────────────────────────────────────────────
// Mirrors project/src/project/services/explainability.py :: build_evidence_chain

export interface EvidenceChain {
  Problem: string;
  'Required metrics': string[];
  Observations: string[];
  'Candidate driver': string[];
  'Causal relationship': string;
  'Scientific source': string[];
  Recommendation: string[];
}

// ─── Reasoning ─────────────────────────────────────────────────────────────────
// Mirrors project/src/project/services/reasoning.py :: MultiMetricReasoning

export interface DriverAnalysis {
  driver: string;
  explained_metrics: string[];
  is_primary: boolean;
  evidence_strength: 'Strong' | 'Moderate' | 'Weak';
  reasoning: string;
}

export interface MultiMetricReasoning {
  relationships_identified: string;
  candidate_drivers: DriverAnalysis[];
}

// ─── Recommendations ───────────────────────────────────────────────────────────
// Mirrors project/src/project/services/recommendation.py :: RecommendationPlan

export interface ScientificEvidenceDetail {
  source: string;
  url: string;
  claims: string[];
}

export interface EvidenceBackedRecommendation {
  recommendation: string;
  why_it_works: string;
  impacted_metrics: string[];
  expected_time_horizon: string;
  scientific_evidence: ScientificEvidenceDetail[];
  confidence: 'High' | 'Medium' | 'Low';
}

export interface RecommendationPlan {
  recommendations: EvidenceBackedRecommendation[];
}

// ─── Missing Metric ────────────────────────────────────────────────────────────
// Mirrors the dict returned by identify_missing_metrics() in metric_knowledge.py:
// { "metric_name": str, "why_it_matters": str, "expected_unit": str }

export interface MissingMetric {
  metric_name: string;
  why_it_matters: string;
  expected_unit: string;
}

// ─── API Response Variants ─────────────────────────────────────────────────────

/** Complete analysis — all pipeline stages succeeded */
export interface AnalysisResponseComplete {
  status: 'complete';
  session_id: string;
  problem_understanding: ProblemUnderstanding;
  evidence_chain: EvidenceChain;
  reasoning: MultiMetricReasoning;
  recommendations: RecommendationPlan;
  evidence_scope?: 'provided_data_only' | 'full';
}

/** Pipeline halted — missing metrics must be provided in a follow-up turn */
export interface AnalysisResponseRequiresInfo {
  status: 'requires_more_info';
  session_id: string;
  missing_metrics: MissingMetric[];
  message: string;
  evidence_scope?: 'provided_data_only' | 'full';
}

/** Union — discriminate on `status` */
export type AnalysisResponse =
  | AnalysisResponseComplete
  | AnalysisResponseRequiresInfo;

// ─── Health ────────────────────────────────────────────────────────────────────

export interface HealthResponse {
  status: 'ok';
  service: string;
}

// ─── Session State ─────────────────────────────────────────────────────────────
// Mirrors project/src/project/schemas/state.py :: ConversationState

export interface ConversationState {
  original_user_problem: string | null;
  species_ecosystem: string | null;
  location: string | null;
  provided_metrics: string[];
  missing_metrics: MissingMetric[];
  retrieved_evidence: Record<string, unknown>[];
  candidate_drivers: string[];
}

export interface SessionResponse {
  session_id: string;
  state: ConversationState;
}

// ─── API Error ─────────────────────────────────────────────────────────────────

export interface ApiErrorPayload {
  detail: string;
}
