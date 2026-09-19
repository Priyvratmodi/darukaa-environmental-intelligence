from typing import List
from project.schemas.metric import EnvironmentalMetric, SourceMetadata
from project.schemas.problem import DomainEnum, ProblemUnderstanding

METRICS_DB: List[EnvironmentalMetric] = [
    # SOIL
    EnvironmentalMetric(
        name="pH",
        domain=DomainEnum.soil,
        description="A measure of the acidity or alkalinity of the soil.",
        why_it_matters="Soil pH affects nutrient availability, microbial activity, and plant growth.",
        problems_investigated=["soil degradation", "nutrient deficiency", "acidification", "yield drop"],
        related_variables=["soil organic carbon", "soil moisture", "nutrient levels"],
        measurement_unit="pH scale (0-14)",
        source=SourceMetadata(
            source_id="FAO-SOIL-PH-1",
            organization="FAO",
            url="https://www.fao.org/soils-portal/soil-management/soil-acidity/en/",
            evidence_provenance="FAO Global Soil Partnership guidelines"
        )
    ),
    EnvironmentalMetric(
        name="soil organic carbon",
        domain=DomainEnum.soil,
        description="Carbon stored in soil organic matter, critical for soil health.",
        why_it_matters="Improves soil structure, water retention, and acts as a climate sink.",
        problems_investigated=["soil degradation", "erosion", "loss of fertility", "carbon depletion"],
        related_variables=["pH", "soil moisture", "vegetation cover"],
        measurement_unit="Percentage (%) or g/kg",
        source=SourceMetadata(
            source_id="FAO-SOIL-SOC-1",
            organization="FAO",
            url="https://www.fao.org/soils-portal/soil-management/soil-organic-carbon/en/",
            evidence_provenance="FAO Global Soil Organic Carbon Map"
        )
    ),
    EnvironmentalMetric(
        name="soil moisture",
        domain=DomainEnum.soil,
        description="The amount of water held in the soil.",
        why_it_matters="Essential for plant growth and regulates surface temperature.",
        problems_investigated=["drought", "compaction", "desertification", "yield drop"],
        related_variables=["rainfall", "temperature", "soil organic carbon"],
        measurement_unit="Volumetric water content (m3/m3) or %",
        source=SourceMetadata(
            source_id="FAO-SOIL-MST-1",
            organization="FAO",
            url="https://www.fao.org/land-water/land/land-governance/land-resources-planning/en/",
            evidence_provenance="FAO Land and Water Division"
        )
    ),
    # LAND USE / LAND COVER
    EnvironmentalMetric(
        name="land-cover composition",
        domain=DomainEnum.land_use,
        description="The physical material at the surface of the earth, mapping different cover types.",
        why_it_matters="Fundamental for assessing habitat availability and human footprint.",
        problems_investigated=["habitat loss", "urbanization", "deforestation"],
        related_variables=["land-cover change", "vegetation cover", "habitat diversity"],
        measurement_unit="Area (ha or km2) per class",
        source=SourceMetadata(
            source_id="IPBES-LULC-COMP-1",
            organization="IPBES",
            url="https://ipbes.net/models-drivers-biodiversity-ecosystem-change",
            evidence_provenance="IPBES Global Assessment Report on Biodiversity and Ecosystem Services"
        )
    ),
    EnvironmentalMetric(
        name="land-cover change",
        domain=DomainEnum.land_use,
        description="The transition of land cover from one type to another over time.",
        why_it_matters="Identifies active areas of habitat destruction or restoration.",
        problems_investigated=["deforestation", "habitat fragmentation", "land degradation"],
        related_variables=["land-cover composition", "deforestation/land conversion", "patch size"],
        measurement_unit="Rate of change (% per year) or Area (ha/year)",
        source=SourceMetadata(
            source_id="IPBES-LULC-CHG-1",
            organization="IPBES",
            url="https://ipbes.net/models-drivers-biodiversity-ecosystem-change",
            evidence_provenance="IPBES Global Assessment"
        )
    ),
    EnvironmentalMetric(
        name="vegetation cover",
        domain=DomainEnum.land_use,
        description="The proportion of land obscured by vegetation.",
        why_it_matters="Crucial for preventing soil erosion and maintaining local microclimates.",
        problems_investigated=["desertification", "soil erosion", "overgrazing"],
        related_variables=["soil moisture", "land-cover change", "species abundance/occurrence"],
        measurement_unit="Percentage (%)",
        source=SourceMetadata(
            source_id="FAO-LULC-VEG-1",
            organization="FAO",
            url="https://www.fao.org/land-water/land/en/",
            evidence_provenance="FAO Global Forest Resources Assessment"
        )
    ),
    EnvironmentalMetric(
        name="patch size",
        domain=DomainEnum.land_use,
        description="The area of contiguous patches of specific land cover (e.g., forest patches).",
        why_it_matters="Determines the viability of populations requiring large core habitats.",
        problems_investigated=["habitat fragmentation", "population isolation", "edge effects"],
        related_variables=["habitat connectivity", "land-cover composition", "species richness"],
        measurement_unit="Hectares (ha) or km2",
        source=SourceMetadata(
            source_id="IPBES-LULC-PATCH-1",
            organization="IPBES",
            url="https://ipbes.net/glossary/habitat-fragmentation",
            evidence_provenance="IPBES Global Assessment"
        )
    ),
    EnvironmentalMetric(
        name="habitat connectivity",
        domain=DomainEnum.land_use,
        description="The degree to which the landscape facilitates or impedes animal movement.",
        why_it_matters="Essential for genetic exchange, migration, and range shifts due to climate change.",
        problems_investigated=["habitat fragmentation", "population isolation", "biodiversity decline"],
        related_variables=["patch size", "land-cover change", "species occurrence"],
        measurement_unit="Connectivity indices (e.g., Probability of Connectivity)",
        source=SourceMetadata(
            source_id="IPBES-LULC-CONN-1",
            organization="IPBES",
            url="https://ipbes.net/glossary/connectivity",
            evidence_provenance="IPBES Global Assessment"
        )
    ),
    # BIODIVERSITY
    EnvironmentalMetric(
        name="species richness",
        domain=DomainEnum.biodiversity,
        description="The number of different species represented in an ecological community, landscape or region.",
        why_it_matters="A fundamental metric of biodiversity health and ecosystem resilience.",
        problems_investigated=["biodiversity decline", "habitat degradation", "invasive species"],
        related_variables=["species abundance/occurrence", "habitat diversity", "patch size"],
        measurement_unit="Count (number of species)",
        source=SourceMetadata(
            source_id="IPBES-BIO-RICH-1",
            organization="IPBES",
            url="https://ipbes.net/glossary/species-richness",
            evidence_provenance="IPBES Core Biodiversity Metrics"
        )
    ),
    EnvironmentalMetric(
        name="species abundance/occurrence",
        domain=DomainEnum.biodiversity,
        description="The number of individuals per species, or the presence/absence of a species in a given area.",
        why_it_matters="Tracks population trends and the risk of local extinction.",
        problems_investigated=["population collapse", "overexploitation", "biodiversity decline"],
        related_variables=["species richness", "habitat connectivity", "pesticide pressure"],
        measurement_unit="Count per area, or binary (presence/absence)",
        source=SourceMetadata(
            source_id="IPBES-BIO-ABUN-1",
            organization="IPBES",
            url="https://ipbes.net/glossary/abundance",
            evidence_provenance="IPBES Global Assessment"
        )
    ),
    EnvironmentalMetric(
        name="habitat diversity",
        domain=DomainEnum.biodiversity,
        description="The range of different habitats or ecological niches present in an area.",
        why_it_matters="Higher habitat diversity typically supports higher species richness.",
        problems_investigated=["monoculture impacts", "habitat simplification", "biodiversity decline"],
        related_variables=["land-cover composition", "species richness", "vegetation cover"],
        measurement_unit="Diversity index (e.g., Shannon index for habitats)",
        source=SourceMetadata(
            source_id="IPBES-BIO-HDIV-1",
            organization="IPBES",
            url="https://ipbes.net/glossary/habitat-diversity",
            evidence_provenance="IPBES Global Assessment"
        )
    ),
    # CLIMATE
    EnvironmentalMetric(
        name="temperature",
        domain=DomainEnum.climate,
        description="Air or surface temperature measurements.",
        why_it_matters="Drives biological processes, evapotranspiration, and species distribution.",
        problems_investigated=["global warming", "heat stress", "range shifts"],
        related_variables=["extreme temperature events", "rainfall", "soil moisture"],
        measurement_unit="Degrees Celsius (°C)",
        source=SourceMetadata(
            source_id="IPCC-CLIM-TEMP-1",
            organization="IPCC",
            url="https://www.ipcc.ch/report/ar6/wg1/",
            evidence_provenance="IPCC AR6 Physical Science Basis"
        )
    ),
    EnvironmentalMetric(
        name="rainfall",
        domain=DomainEnum.climate,
        description="Precipitation amount over a specific period.",
        why_it_matters="Primary input for fresh water ecosystems, agriculture, and soil moisture.",
        problems_investigated=["drought", "flooding", "water scarcity"],
        related_variables=["water availability", "drought/dry-period duration", "soil moisture"],
        measurement_unit="Millimeters (mm)",
        source=SourceMetadata(
            source_id="IPCC-CLIM-RAIN-1",
            organization="IPCC",
            url="https://www.ipcc.ch/report/ar6/wg1/",
            evidence_provenance="IPCC AR6 Physical Science Basis"
        )
    ),
    EnvironmentalMetric(
        name="extreme temperature events",
        domain=DomainEnum.climate,
        description="Frequency and severity of heatwaves or unusual frost events.",
        why_it_matters="Causes acute physiological stress to plants and animals, driving sudden mortality.",
        problems_investigated=["crop failure", "coral bleaching", "heat stress"],
        related_variables=["temperature", "drought/dry-period duration"],
        measurement_unit="Days/year exceeding threshold",
        source=SourceMetadata(
            source_id="IPCC-CLIM-EXT-1",
            organization="IPCC",
            url="https://www.ipcc.ch/report/ar6/wg2/",
            evidence_provenance="IPCC AR6 Impacts, Adaptation and Vulnerability"
        )
    ),
    EnvironmentalMetric(
        name="drought/dry-period duration",
        domain=DomainEnum.climate,
        description="The length of time without significant precipitation.",
        why_it_matters="Prolonged drought leads to ecosystem collapse, wildfires, and agricultural failure.",
        problems_investigated=["drought", "desertification", "water scarcity"],
        related_variables=["rainfall", "soil moisture", "water availability"],
        measurement_unit="Consecutive dry days",
        source=SourceMetadata(
            source_id="IPCC-CLIM-DRO-1",
            organization="IPCC",
            url="https://www.ipcc.ch/report/ar6/wg1/",
            evidence_provenance="IPCC AR6 Physical Science Basis"
        )
    ),
    EnvironmentalMetric(
        name="water availability",
        domain=DomainEnum.climate,
        description="The amount of fresh water accessible for ecosystems and human use.",
        why_it_matters="Critical constraint on biomass production and aquatic habitat health.",
        problems_investigated=["water scarcity", "river drying", "aquifer depletion"],
        related_variables=["rainfall", "drought/dry-period duration", "pollution pressure"],
        measurement_unit="Cubic meters (m3) or discharge rate",
        source=SourceMetadata(
            source_id="IPCC-CLIM-WAT-1",
            organization="IPCC",
            url="https://www.ipcc.ch/report/ar6/wg2/",
            evidence_provenance="IPCC AR6 Impacts, Adaptation and Vulnerability"
        )
    ),
    # HUMAN IMPACT
    EnvironmentalMetric(
        name="pollution pressure",
        domain=DomainEnum.pollution,
        description="The level of contaminants (e.g., heavy metals, plastics, nutrients) introduced into the environment.",
        why_it_matters="Causes direct toxicity to wildlife, eutrophication, and soil degradation.",
        problems_investigated=["eutrophication", "water contamination", "soil toxicity"],
        related_variables=["water availability", "pesticide pressure", "species abundance/occurrence"],
        measurement_unit="Concentration (mg/L or mg/kg)",
        source=SourceMetadata(
            source_id="IPBES-HUM-POL-1",
            organization="IPBES",
            url="https://ipbes.net/models-drivers-biodiversity-ecosystem-change",
            evidence_provenance="IPBES Global Assessment: Direct Drivers"
        )
    ),
    EnvironmentalMetric(
        name="pesticide pressure",
        domain=DomainEnum.agriculture,
        description="The volume and toxicity of chemical pesticides applied in an area.",
        why_it_matters="Directly drives pollinator decline and aquatic ecosystem poisoning.",
        problems_investigated=["pollinator decline", "biodiversity decline", "water contamination"],
        related_variables=["pollution pressure", "species richness", "land-cover composition"],
        measurement_unit="Application rate (kg/ha) or Toxicity index",
        source=SourceMetadata(
            source_id="FAO-HUM-PEST-1",
            organization="FAO",
            url="https://www.fao.org/pest-and-pesticide-management/en/",
            evidence_provenance="FAO Pest and Pesticide Management"
        )
    ),
    EnvironmentalMetric(
        name="deforestation/land conversion",
        domain=DomainEnum.land_use,
        description="The permanent removal of natural ecosystems for other land uses like agriculture or urban areas.",
        why_it_matters="The primary driver of global terrestrial biodiversity loss.",
        problems_investigated=["habitat loss", "carbon emissions", "biodiversity decline"],
        related_variables=["land-cover change", "habitat connectivity", "soil organic carbon"],
        measurement_unit="Area converted (ha) or Deforestation rate (%)",
        source=SourceMetadata(
            source_id="FAO-HUM-DEF-1",
            organization="FAO",
            url="https://www.fao.org/forest-resources-assessment/en/",
            evidence_provenance="FAO Global Forest Resources Assessment"
        )
    )
]

def get_relevant_metrics(problem: ProblemUnderstanding) -> List[EnvironmentalMetric]:
    """
    Retrieves relevant environmental metrics based on the structured problem understanding.
    This avoids hardcoding metrics in the LLM prompt.
    """
    relevant = []
    
    # Map high-level domains to allow cross-pollination 
    # (e.g. biodiversity problems should pull species metrics and habitat metrics)
    domain_mapping = {
        DomainEnum.soil: [DomainEnum.soil, DomainEnum.agriculture],
        DomainEnum.biodiversity: [DomainEnum.biodiversity, DomainEnum.species, DomainEnum.ecosystem, DomainEnum.habitat],
        DomainEnum.species: [DomainEnum.species, DomainEnum.biodiversity],
        DomainEnum.habitat: [DomainEnum.habitat, DomainEnum.ecosystem, DomainEnum.land_use, DomainEnum.biodiversity],
        DomainEnum.ecosystem: [DomainEnum.ecosystem, DomainEnum.habitat, DomainEnum.biodiversity, DomainEnum.land_use, DomainEnum.climate],
        DomainEnum.land_use: [DomainEnum.land_use, DomainEnum.agriculture, DomainEnum.habitat],
        DomainEnum.climate: [DomainEnum.climate, DomainEnum.water],
        DomainEnum.water: [DomainEnum.water, DomainEnum.climate, DomainEnum.pollution],
        DomainEnum.pollution: [DomainEnum.pollution, DomainEnum.water, DomainEnum.soil],
        DomainEnum.agriculture: [DomainEnum.agriculture, DomainEnum.soil, DomainEnum.land_use],
        DomainEnum.unknown: []
    }
    
    target_domains = domain_mapping.get(problem.domain, [problem.domain])
    
    for metric in METRICS_DB:
        # Match by domain
        if metric.domain in target_domains:
            if metric not in relevant:
                relevant.append(metric)
            continue
            
        # Match by mentioned factors or suspected outcome (keyword overlap)
        search_terms = []
        if problem.mentioned_factors:
            search_terms.extend([f.lower() for f in problem.mentioned_factors])
        if problem.suspected_outcome:
            search_terms.append(problem.suspected_outcome.lower())
        if problem.problem_statement:
            search_terms.append(problem.problem_statement.lower())
            
        for term in search_terms:
            if term in metric.name.lower() or any(term in p.lower() for p in metric.problems_investigated):
                if metric not in relevant:
                    relevant.append(metric)
                break

    return relevant

def identify_missing_metrics(problem: ProblemUnderstanding, user_observations: List[str] = None) -> List[dict]:
    """
    Compares user-provided observations with required relevant metrics.
    Returns missing metrics that are relevant to the problem.
    """
    if user_observations is None:
        user_observations = problem.mentioned_factors or []
        
    relevant = get_relevant_metrics(problem)
    user_obs_lower = [obs.lower() for obs in user_observations]
    
    missing_metrics = []
    for metric in relevant:
        # Check if metric name or any variant (e.g. slash parts) is mentioned in user observations
        name_variants = [metric.name.lower()] + [part.strip().lower() for part in metric.name.split('/') if part.strip()]
        is_mentioned = any(
            any(variant in obs or obs in variant for variant in name_variants)
            for obs in user_obs_lower
        )
        if not is_mentioned:
            missing_metrics.append({
                "metric_name": metric.name,
                "why_it_matters": metric.why_it_matters,
                "expected_unit": metric.measurement_unit
            })
            
    return missing_metrics
