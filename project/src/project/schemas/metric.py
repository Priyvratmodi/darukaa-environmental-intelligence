from pydantic import BaseModel
from typing import List, Optional
from project.schemas.problem import DomainEnum

class SourceMetadata(BaseModel):
    source_id: str
    organization: str
    url: Optional[str]
    evidence_provenance: str

class EnvironmentalMetric(BaseModel):
    name: str
    domain: DomainEnum
    description: str
    why_it_matters: str
    problems_investigated: List[str]
    related_variables: List[str]
    measurement_unit: str
    source: SourceMetadata

class ExtractedMetricObservation(BaseModel):
    canonical_name: str
    value: Optional[str] = None
    unit: Optional[str] = None
    trend: Optional[str] = None
    qualitative_state: Optional[str] = None
    evidence: str
    confidence: float = 0.95
