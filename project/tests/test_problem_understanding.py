import pytest
from project.services.problem_understanding import analyze_problem
from project.schemas.problem import DomainEnum

def test_soil_degradation():
    text = "My corn yield is dropping. The soil feels very compacted, dry, and the pH seems off."
    result = analyze_problem(text)
    
    assert result["domain"] in [DomainEnum.soil, DomainEnum.agriculture]
    assert "corn" in str(result["affected_entity"]).lower() or "soil" in str(result["affected_entity"]).lower()
    assert len(result["mentioned_factors"]) >= 2
    # Check that factors like "pH" or "compacted" or "dry" are extracted
    factors = " ".join(result["mentioned_factors"]).lower()
    assert "ph" in factors or "compact" in factors or "dry" in factors

def test_biodiversity_decline():
    text = "Biodiversity is declining on my farm. I see fewer bees and butterflies this year."
    result = analyze_problem(text)
    
    assert result["domain"] == DomainEnum.biodiversity
    assert result["affected_entity"] is not None
    assert "farm" in str(result["affected_entity"]).lower() or "bees" in str(result["affected_entity"]).lower() or "butterflies" in str(result["affected_entity"]).lower()

def test_habitat_fragmentation():
    text = "A new highway was built through the local forest, and now deer populations are isolated."
    result = analyze_problem(text)
    
    assert result["domain"] in [DomainEnum.habitat, DomainEnum.ecosystem, DomainEnum.land_use, DomainEnum.biodiversity]
    assert "forest" in str(result["affected_entity"]).lower() or "deer" in str(result["affected_entity"]).lower()

def test_climate_related_problem():
    text = "We haven't had rain in 3 months and the temperature is unusually high, drying out the river."
    result = analyze_problem(text)
    
    assert result["domain"] in [DomainEnum.climate, DomainEnum.water]
    assert "river" in str(result["affected_entity"]).lower()
    factors = " ".join(result["mentioned_factors"]).lower()
    assert "rain" in factors or "temperature" in factors

def test_ambiguous_query():
    text = "Things just don't look right outside."
    result = analyze_problem(text)
    
    # Should not invent things
    assert result["domain"] == DomainEnum.unknown
    assert not result["mentioned_factors"]
    assert result["location"] is None
