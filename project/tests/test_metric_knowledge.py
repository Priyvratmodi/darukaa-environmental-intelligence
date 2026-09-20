from project.schemas.problem import ProblemUnderstanding, DomainEnum
from project.services.metric_knowledge import get_relevant_metrics, METRICS_DB

def test_soil_problem_retrieves_soil_metrics():
    problem = ProblemUnderstanding(
        problem_statement="The corn yield is dropping and soil is compacted.",
        domain=DomainEnum.soil,
        affected_entity="corn",
        ecosystem_context="farm",
        location=None,
        suspected_outcome="yield drop",
        mentioned_factors=["compacted"]
    )
    
    metrics = get_relevant_metrics(problem)
    metric_names = [m.name for m in metrics]
    
    # Assert soil metrics are retrieved
    assert "pH" in metric_names
    assert "soil organic carbon" in metric_names
    assert "soil moisture" in metric_names
    
    # Assert irrelevant metrics are NOT retrieved
    assert "habitat connectivity" not in metric_names
    assert "temperature" not in metric_names

def test_biodiversity_problem_retrieves_biodiversity_metrics():
    problem = ProblemUnderstanding(
        problem_statement="Fewer bees and butterflies this year.",
        domain=DomainEnum.biodiversity,
        affected_entity="bees and butterflies",
        ecosystem_context="farm",
        location=None,
        suspected_outcome="biodiversity decline",
        mentioned_factors=["bees", "butterflies"]
    )
    
    metrics = get_relevant_metrics(problem)
    metric_names = [m.name for m in metrics]
    
    # Should retrieve biodiversity metrics
    assert "species richness" in metric_names
    assert "species abundance/occurrence" in metric_names
    
    # Should NOT retrieve completely unrelated metrics
    assert "soil organic carbon" not in metric_names

def test_land_fragmentation_problem_retrieves_land_metrics():
    problem = ProblemUnderstanding(
        problem_statement="Highway built through the forest.",
        domain=DomainEnum.land_use,
        affected_entity="forest",
        ecosystem_context="forest",
        location=None,
        suspected_outcome="habitat fragmentation",
        mentioned_factors=["highway"]
    )
    
    metrics = get_relevant_metrics(problem)
    metric_names = [m.name for m in metrics]
    
    # Should retrieve land use / fragmentation metrics
    assert "land-cover change" in metric_names
    assert "habitat connectivity" in metric_names
    assert "patch size" in metric_names
    
    # Should NOT retrieve completely unrelated metrics
    assert "pH" not in metric_names
