from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class DomainEnum(str, Enum):
    soil = "soil"
    water = "water"
    biodiversity = "biodiversity"
    land_use = "land_use"
    climate = "climate"
    pollution = "pollution"
    agriculture = "agriculture"
    habitat = "habitat"
    species = "species"
    ecosystem = "ecosystem"
    unknown = "unknown"

class ProblemUnderstanding(BaseModel):
    problem_statement: str = Field(
        default="Environmental observation update",
        description="A concise summary of the environmental problem described or metrics provided."
    )
    domain: DomainEnum = Field(
        description="The primary environmental domain involved based on the query."
    )
    affected_entity: Optional[str] = Field(
        description="The specific entity affected (e.g., farm, lake, forest, crops). Null if not mentioned."
    )
    ecosystem_context: Optional[str] = Field(
        description="The broader ecosystem context, if mentioned. Null if not mentioned."
    )
    location: Optional[str] = Field(
        description="The geographic or spatial location, if mentioned. Null if not mentioned."
    )
    suspected_outcome: Optional[str] = Field(
        description="The observed or suspected negative outcome/impact described in the problem."
    )
    mentioned_factors: List[str] = Field(
        description="Any specific environmental factors, metrics, or variables explicitly mentioned (e.g., rainfall, soil pH, monoculture). Empty list if none."
    )
    observed_values: List[str] = Field(
        default_factory=list,
        description="Explicit observations including any numeric values, units, or measurements mentioned in the query (e.g., 'species richness: 18', 'soil pH: 5.2', 'house sparrow: 24 per ha')."
    )
