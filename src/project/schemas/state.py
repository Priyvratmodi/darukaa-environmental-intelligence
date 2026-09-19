from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ConversationState(BaseModel):
    original_user_problem: Optional[str] = None
    species_ecosystem: Optional[str] = None
    location: Optional[str] = None
    provided_metrics: List[str] = Field(default_factory=list)
    missing_metrics: List[dict] = Field(default_factory=list)
    retrieved_evidence: List[dict] = Field(default_factory=list)
    candidate_drivers: List[str] = Field(default_factory=list)
