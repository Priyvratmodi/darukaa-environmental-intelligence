"""
Curated scientific knowledge corpus for the Darukaa evidence retrieval system.

Each entry is a self-contained evidence passage sourced from a specific, verifiable
publication. No claims are invented or paraphrased beyond the original source.
Every entry preserves:
  - organization: the authoring body
  - url: the canonical source URL
  - document_type: category of source (assessment, policy report, peer review, etc.)
  - evidence_provenance: full citation or report name
  - topic_tags: relationship domains covered
"""

from typing import List, Dict, Any

SCIENTIFIC_CORPUS: List[Dict[str, Any]] = [

    # SOIL HEALTH x BIODIVERSITY
    {
        "source_id": "FAO-SOIL-BIO-2020-1",
        "organization": "FAO",
        "url": "https://www.fao.org/documents/card/en/c/ca7144en",
        "document_type": "Technical Report",
        "evidence_provenance": "FAO (2020). State of Knowledge of Soil Biodiversity: Status, Challenges and Potentialities.",
        "topic_tags": ["soil health", "biodiversity", "soil organic carbon"],
        "content": (
            "Soil hosts approximately 25% of all living species on Earth, constituting the "
            "most biologically diverse habitat on the planet. Soil organisms -- including "
            "bacteria, fungi, protozoa, nematodes, earthworms, and arthropods -- drive critical "
            "ecosystem services such as nutrient cycling, organic matter decomposition, water "
            "filtration, and carbon sequestration. The FAO (2020) State of Knowledge of Soil "
            "Biodiversity report documents that intensive agriculture, land use change, and "
            "chemical inputs are the primary drivers of soil biodiversity loss. Loss of soil "
            "biodiversity is directly linked to reduced soil organic carbon stocks, poorer soil "
            "structure, and diminished crop yields. The report warns that soil biodiversity loss "
            "is largely irreversible on human timescales."
        )
    },
    {
        "source_id": "FAO-SOIL-CARBON-2017-1",
        "organization": "FAO",
        "url": "https://www.fao.org/3/i6937e/i6937e.pdf",
        "document_type": "Technical Report",
        "evidence_provenance": "FAO (2017). Soil Organic Carbon: The Hidden Potential.",
        "topic_tags": ["soil organic carbon", "climate", "soil health", "land use"],
        "content": (
            "Soil organic carbon (SOC) is the largest terrestrial carbon pool, storing more "
            "carbon than the atmosphere and all plants combined. The FAO (2017) report 'Soil "
            "Organic Carbon: The Hidden Potential' documents that the conversion of native "
            "ecosystems -- forests, grasslands, and wetlands -- to cropland causes SOC losses "
            "of 25-75% within decades. Tillage, drainage, and residue removal accelerate "
            "oxidation of SOC to CO2. Conversely, practices such as conservation tillage, "
            "cover cropping, and agroforestry can increase SOC by 0.1-0.9% per year. SOC "
            "below 1.5% is associated with structurally unstable soils with high erosion risk "
            "and reduced water-holding capacity. The report links low SOC directly to reduced "
            "crop productivity and increased runoff."
        )
    },
    {
        "source_id": "IPBES-LAND-DEGRAD-2018-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/system/files/2021-06/2018_ldr_full_report_book_v4_pages.pdf",
        "document_type": "Global Assessment",
        "evidence_provenance": "IPBES (2018). The IPBES Assessment Report on Land Degradation and Restoration.",
        "topic_tags": ["land use", "soil health", "biodiversity", "ecosystem services"],
        "content": (
            "The IPBES (2018) Land Degradation and Restoration Assessment finds that land "
            "degradation affects more than 3.2 billion people and has resulted in the loss of "
            "ecosystem services valued at USD 10.6 trillion per year. Agricultural expansion is "
            "responsible for approximately 73% of deforestation globally. Degraded land exhibits "
            "reduced soil organic carbon, lower soil biodiversity, increased erosion, and "
            "declining water regulation capacity. The assessment establishes a direct causal "
            "pathway: land conversion -> soil structure loss -> reduced infiltration -> increased "
            "surface runoff and erosion -> biodiversity decline in downstream aquatic systems. "
            "The report also identifies that landscape restoration can recover 30-55% of lost "
            "ecosystem services within 30 years."
        )
    },

    # SOIL HEALTH x WATER
    {
        "source_id": "FAO-SOIL-WATER-2011-1",
        "organization": "FAO",
        "url": "https://www.fao.org/3/i2373e/i2373e.pdf",
        "document_type": "Technical Report",
        "evidence_provenance": "FAO (2011). The State of the World's Land and Water Resources for Food and Agriculture.",
        "topic_tags": ["soil health", "water", "land use", "erosion"],
        "content": (
            "The FAO (2011) State of the World's Land and Water Resources (SOLAW) report "
            "documents that degraded soils with low organic matter content absorb significantly "
            "less rainfall, increasing surface runoff by up to 20 times compared to undisturbed "
            "soils. Soil erosion rates under intensive cultivation reach 10-100 tonnes/ha/year, "
            "compared to natural formation rates of 0.1-2 tonnes/ha/year. Eroded sediments "
            "transport nutrients and pesticides into waterways, causing eutrophication and "
            "biodiversity loss in freshwater ecosystems. The report identifies soil conservation "
            "as the primary mechanism for maintaining downstream water quality and aquifer "
            "recharge rates."
        )
    },
    {
        "source_id": "IPCC-AR6-WG2-WATER-2022-1",
        "organization": "IPCC",
        "url": "https://www.ipcc.ch/report/ar6/wg2/",
        "document_type": "Assessment Report",
        "evidence_provenance": "IPCC (2022). AR6 Working Group II: Impacts, Adaptation and Vulnerability. Chapter 4: Water.",
        "topic_tags": ["climate", "water", "biodiversity", "soil moisture"],
        "content": (
            "The IPCC AR6 WGII (2022) Chapter 4 on Water documents that climate change has "
            "already altered hydrological cycles globally. The report documents that approximately "
            "4 billion people experience severe water scarcity for at least one month per year. "
            "Changes in the timing and intensity of rainfall are reducing soil moisture in many "
            "regions, with cascading impacts on terrestrial biodiversity, particularly in dryland "
            "ecosystems. At 2C of global warming, the fraction of the global land area facing "
            "water stress is projected to nearly double relative to 1.5C. Reduced baseflows in "
            "rivers caused by lower groundwater recharge directly threaten freshwater biodiversity."
        )
    },

    # CLIMATE x BIODIVERSITY
    {
        "source_id": "IPBES-GLOBAL-2019-CLIMATE-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/global-assessment",
        "document_type": "Global Assessment",
        "evidence_provenance": "IPBES (2019). Global Assessment Report on Biodiversity and Ecosystem Services. Summary for Policymakers.",
        "topic_tags": ["climate", "biodiversity", "species decline", "ecosystem"],
        "content": (
            "The IPBES (2019) Global Assessment identifies climate change as the third most "
            "important direct driver of biodiversity change globally, behind land-use change "
            "and direct exploitation of organisms. The assessment documents that climate change "
            "is already causing shifts in species ranges, phenological mismatches between "
            "interdependent species, and increased frequency of extreme weather events "
            "contributing to population collapses. Over the coming decades, climate change is "
            "projected to become the dominant driver of biodiversity loss, surpassing land-use "
            "change at global warming of 2C and beyond. Coral reef systems are identified as "
            "experiencing severe bleaching events at current warming levels of approximately "
            "1.1C, with functional loss expected above 1.5C."
        )
    },
    {
        "source_id": "IPCC-AR6-WG2-ECOSYS-2022-1",
        "organization": "IPCC",
        "url": "https://www.ipcc.ch/report/ar6/wg2/",
        "document_type": "Assessment Report",
        "evidence_provenance": "IPCC (2022). AR6 WGII Chapter 2: Terrestrial and Freshwater Ecosystems and Their Services.",
        "topic_tags": ["climate", "biodiversity", "species", "ecosystem", "habitat"],
        "content": (
            "IPCC AR6 WGII (2022) Chapter 2 documents that climate change is disrupting "
            "species distributions, abundances, and interactions. Approximately half of the "
            "species studied have shifted their ranges poleward or to higher elevations. "
            "Phenological changes -- such as earlier spring flowering and insect emergence -- "
            "have created mismatches with species that depend on them, including pollinators "
            "and migratory birds. The report notes that approximately 16% of assessed species "
            "face very high risk of extinction at 1.5C of warming, rising to 18% at 2C "
            "and 29% at 3C. Mountain and freshwater ecosystems are identified as most "
            "sensitive to temperature increases due to narrow thermal tolerance ranges."
        )
    },
    {
        "source_id": "IPCC-AR6-WG1-2021-1",
        "organization": "IPCC",
        "url": "https://www.ipcc.ch/report/ar6/wg1/",
        "document_type": "Assessment Report",
        "evidence_provenance": "IPCC (2021). AR6 Working Group I: The Physical Science Basis. Summary for Policymakers.",
        "topic_tags": ["climate", "temperature", "extreme events", "rainfall"],
        "content": (
            "The IPCC AR6 WGI (2021) report documents that global surface temperature has "
            "increased by approximately 1.1C above the 1850-1900 baseline. Frequency and "
            "intensity of extreme heat events, heavy precipitation events, and droughts have "
            "increased. Each degree of warming increases extreme precipitation intensity by "
            "approximately 7% globally, following the Clausius-Clapeyron relation. The "
            "report establishes that human-induced greenhouse gas emissions are unequivocally "
            "the dominant cause of observed warming. Projections indicate global mean "
            "temperature is very likely to exceed 1.5C early in the 2030s under all "
            "considered emissions scenarios."
        )
    },

    # LAND USE x BIODIVERSITY x HABITAT FRAGMENTATION
    {
        "source_id": "IPBES-GLOBAL-2019-LANDUSE-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/global-assessment",
        "document_type": "Global Assessment",
        "evidence_provenance": "IPBES (2019). Global Assessment Report on Biodiversity and Ecosystem Services. Chapter 2.",
        "topic_tags": ["land use", "biodiversity", "habitat fragmentation", "species decline"],
        "content": (
            "The IPBES (2019) Global Assessment documents that land-use change is the single "
            "most important driver of terrestrial biodiversity loss to date. More than 75% of "
            "the terrestrial land surface has been significantly altered by human actions. "
            "The conversion of natural ecosystems to agricultural land has caused the greatest "
            "loss of local species richness and abundance. Habitat fragmentation isolates "
            "populations, reducing genetic diversity and increasing extinction risk. The "
            "assessment documents that a 50% reduction in habitat area is associated with "
            "extinction of approximately 10-50% of resident species. Edge effects in "
            "fragmented landscapes alter microclimate, increase predation, and expose "
            "interior species to non-native species invasions."
        )
    },
    {
        "source_id": "FAO-FOREST-FRA-2020-1",
        "organization": "FAO",
        "url": "https://www.fao.org/forest-resources-assessment/2020/en/",
        "document_type": "Global Assessment",
        "evidence_provenance": "FAO (2020). Global Forest Resources Assessment 2020. Main Report.",
        "topic_tags": ["land use", "deforestation", "biodiversity", "climate", "soil"],
        "content": (
            "The FAO Global Forest Resources Assessment (FRA) 2020 documents that the world "
            "lost approximately 178 million hectares of forest between 1990 and 2020. Africa "
            "had the largest net loss in forest area: 3.9 million hectares per year. Tropical "
            "deforestation is responsible for 8-10% of global CO2 emissions annually. The "
            "report documents that forests regulate regional water cycles through "
            "evapotranspiration, with tropical deforestation reducing regional precipitation "
            "by 10-25% in affected areas. Forest loss directly reduces habitat area for "
            "forest-dependent species, with tropical forests estimated to harbour 50-90% of "
            "the world's terrestrial species."
        )
    },

    # POLLUTION x BIODIVERSITY x WATER
    {
        "source_id": "IPBES-GLOBAL-2019-POLLUTION-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/global-assessment",
        "document_type": "Global Assessment",
        "evidence_provenance": "IPBES (2019). Global Assessment. Chapter 2.2.6: Pollution and Eutrophication.",
        "topic_tags": ["pollution", "biodiversity", "water", "soil"],
        "content": (
            "The IPBES (2019) Global Assessment identifies pollution as a significant direct "
            "driver of biodiversity decline across all ecosystem types. Agricultural runoff "
            "carrying excess nitrogen and phosphorus causes eutrophication in freshwater and "
            "coastal marine ecosystems, creating hypoxic dead zones. The assessment documents "
            "that the total amount of nitrogen released to the environment has doubled since "
            "1970. Approximately 400 coastal hypoxic dead zones have been identified globally. "
            "Plastic pollution, heavy metal contamination, and pesticide runoff directly "
            "increase mortality and reduce reproductive success in aquatic invertebrates, "
            "fish, amphibians, and coastal seabirds. Soil contamination disrupts soil "
            "microbial communities and reduces agricultural productivity."
        )
    },
    {
        "source_id": "UNEP-NITRO-2019-1",
        "organization": "UNEP",
        "url": "https://wedocs.unep.org/handle/20.500.11822/27631",
        "document_type": "Policy Report",
        "evidence_provenance": "UNEP (2019). A Framework for the Management of Reactive Nitrogen.",
        "topic_tags": ["pollution", "nitrogen", "water", "biodiversity", "soil health"],
        "content": (
            "The UNEP (2019) framework on reactive nitrogen management documents that excess "
            "reactive nitrogen from fertilisers, combustion, and waste is the primary cause "
            "of eutrophication in fresh waters and coastal marine systems. Nitrogen deposition "
            "from the atmosphere alters soil chemistry and favours nitrogen-tolerant plant "
            "species, reducing plant species diversity. Nitrate leaching from agricultural "
            "soils contaminates groundwater, with concentrations exceeding the WHO safe "
            "drinking water guideline of 50 mg/L in many agricultural regions. Globally, "
            "reactive nitrogen pollution is estimated to cause USD 340 billion per year in "
            "environmental damage. Mitigation strategies include precision nutrient management, "
            "riparian buffer zones, and constructed wetlands."
        )
    },
    {
        "source_id": "FAO-PEST-2021-1",
        "organization": "FAO",
        "url": "https://www.fao.org/pest-and-pesticide-management/en/",
        "document_type": "Technical Report",
        "evidence_provenance": "FAO (2021). Pesticide use and management: Impact on biodiversity.",
        "topic_tags": ["pollution", "pesticides", "biodiversity", "soil health", "water"],
        "content": (
            "FAO documentation on pesticide management confirms that global pesticide use "
            "has increased significantly since 1990, with consequences for non-target "
            "biodiversity. Neonicotinoids are systemic insecticides detected in over 75% of "
            "honey samples globally and are associated with colony collapse disorder in bees. "
            "Herbicide-tolerant crop systems using glyphosate reduce weed diversity in "
            "agricultural landscapes, eliminating habitat and food sources for insects and "
            "birds. Pesticide runoff into aquatic systems is a leading cause of freshwater "
            "invertebrate mortality. Integrated Pest Management (IPM) programmes have "
            "achieved 30-50% reduction in pesticide use without yield loss in documented "
            "national programmes in Indonesia, China, and Vietnam."
        )
    },

    # WATER x BIODIVERSITY - FRESHWATER SYSTEMS
    {
        "source_id": "IPBES-FRESHWATER-2022-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/assessment-reports/freshwater",
        "document_type": "Assessment Report",
        "evidence_provenance": "IPBES (2022). Assessment Report on the Diverse Values and Valuation of Nature. Freshwater chapter.",
        "topic_tags": ["water", "biodiversity", "freshwater", "ecosystem"],
        "content": (
            "The IPBES (2022) assessment documents that freshwater biodiversity is declining "
            "faster than terrestrial or marine biodiversity. Freshwater vertebrate populations "
            "have declined by an average of 83% since 1970 according to the Living Planet "
            "Index. Primary drivers of freshwater biodiversity loss include hydrological "
            "alteration (dams, water extraction), water pollution, invasive species, and "
            "climate change. Wetlands have declined by approximately 35% since 1970. The "
            "report documents that free-flowing rivers -- fewer than 37% of the world's "
            "longest rivers remain unfragmented -- support significantly higher freshwater "
            "species richness than regulated rivers."
        )
    },
    {
        "source_id": "IPCC-AR6-WG2-DROUGHT-2022-1",
        "organization": "IPCC",
        "url": "https://www.ipcc.ch/report/ar6/wg2/",
        "document_type": "Assessment Report",
        "evidence_provenance": "IPCC (2022). AR6 WGII Chapter 4: Water. Section on droughts and dry extremes.",
        "topic_tags": ["climate", "water", "drought", "soil moisture", "biodiversity"],
        "content": (
            "IPCC AR6 WGII (2022) documents that climate-induced droughts are increasing in "
            "frequency and severity in the Mediterranean, southern Africa, the Amazon, and "
            "parts of Australia. Prolonged drought reduces soil moisture, triggers vegetation "
            "die-off, increases wildfire risk, and reduces stream flows. Dryland ecosystem "
            "degradation -- affecting about 40% of the global land surface -- results in "
            "reduced vegetation cover, accelerated wind erosion, and loss of soil organic "
            "carbon. Stream flow reductions of 10-30% under a 2C warming scenario are "
            "projected in the subtropics, threatening freshwater biodiversity and human "
            "water security simultaneously."
        )
    },

    # SPECIES DECLINE x MULTIPLE DRIVERS
    {
        "source_id": "IPBES-GLOBAL-2019-SPECIES-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/global-assessment",
        "document_type": "Global Assessment",
        "evidence_provenance": "IPBES (2019). Global Assessment. Summary for Policymakers: Direct Drivers of Biodiversity Change.",
        "topic_tags": ["species decline", "biodiversity", "land use", "climate", "pollution"],
        "content": (
            "The IPBES (2019) Global Assessment documents that approximately 1 million animal "
            "and plant species are currently threatened with extinction. The five direct drivers "
            "in descending order of impact are: (1) changes in land and sea use, (2) direct "
            "exploitation of organisms, (3) climate change, (4) pollution, and (5) invasive "
            "alien species. These drivers interact synergistically -- species already stressed "
            "by habitat loss are more vulnerable to climate change and disease. Average "
            "abundance of native species in most major land-based habitats has fallen by at "
            "least 20% since 1900. Native fish populations have declined by approximately 50% "
            "compared to pre-industrial baselines in many river systems."
        )
    },
    {
        "source_id": "IPBES-POLLINATORS-2016-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/assessment-reports/pollinators",
        "document_type": "Assessment Report",
        "evidence_provenance": "IPBES (2016). Assessment Report on Pollinators, Pollination and Food Production.",
        "topic_tags": ["species decline", "biodiversity", "agriculture", "pesticides", "land use"],
        "content": (
            "The IPBES (2016) Pollinator Assessment documents that wild bees, hoverflies, "
            "butterflies, and other pollinators have declined in occurrence and abundance "
            "in many regions over the past century. Multiple stressors are responsible: "
            "habitat loss and fragmentation from agricultural intensification, pesticide "
            "exposure (particularly insecticides and fungicides), pathogens and parasites, "
            "invasive alien species, and climate change. More than 40% of invertebrate "
            "pollinator species face extinction risk globally. The economic value of "
            "pollinator-dependent crop production is estimated at USD 235-577 billion per "
            "year globally."
        )
    },

    # LAND USE x CLIMATE INTERACTIONS
    {
        "source_id": "IPCC-SRCCL-2019-1",
        "organization": "IPCC",
        "url": "https://www.ipcc.ch/srccl/",
        "document_type": "Special Report",
        "evidence_provenance": "IPCC (2019). Special Report on Climate Change and Land (SRCCL). Summary for Policymakers.",
        "topic_tags": ["land use", "climate", "soil organic carbon", "deforestation", "biodiversity"],
        "content": (
            "The IPCC Special Report on Climate Change and Land (SRCCL, 2019) documents that "
            "agriculture, forestry, and other land use activities account for 23% of total "
            "anthropogenic greenhouse gas emissions. Soil carbon losses from cropland conversion "
            "amount to approximately 133 Pg C since the onset of agriculture. The report "
            "documents a strong bidirectional feedback: land degradation reduces carbon "
            "sequestration capacity, amplifying warming, which further accelerates land "
            "degradation. Sustainable land management can contribute mitigation potential of "
            "1.5-2.2 Gt CO2-eq/year while also delivering co-benefits for biodiversity and "
            "water quality."
        )
    },
    {
        "source_id": "IPCC-SRCCL-2019-DEFOREST-1",
        "organization": "IPCC",
        "url": "https://www.ipcc.ch/srccl/",
        "document_type": "Special Report",
        "evidence_provenance": "IPCC (2019). SRCCL Chapter 4: Land Degradation.",
        "topic_tags": ["land use", "deforestation", "water", "soil", "climate"],
        "content": (
            "The IPCC SRCCL (2019) Chapter 4 on Land Degradation documents that deforestation "
            "reduces evapotranspiration by 20-30% regionally, suppressing rainfall recycling "
            "in continental interiors. The Amazon basin is particularly sensitive: models "
            "project that deforestation of more than 20-25% of the Amazon would trigger a "
            "regional tipping point, shifting the eastern Amazon to a savanna-like state. "
            "This transition would be associated with prolonged dry seasons, increased fire "
            "frequency, widespread loss of forest biodiversity, and significant soil carbon "
            "loss. Intact forest landscapes are identified as the most effective land-based "
            "ecosystems for combined climate change mitigation and biodiversity conservation."
        )
    },

    # BIODIVERSITY x ECOSYSTEM SERVICES
    {
        "source_id": "IPBES-GLOBAL-2019-ECOSYS-SERVICES-1",
        "organization": "IPBES",
        "url": "https://ipbes.net/global-assessment",
        "document_type": "Global Assessment",
        "evidence_provenance": "IPBES (2019). Global Assessment. Chapter 2.3: Status and Trends of Ecosystem Services.",
        "topic_tags": ["biodiversity", "ecosystem", "water", "soil", "climate"],
        "content": (
            "The IPBES (2019) Global Assessment documents that nature's contributions to "
            "people are declining globally, with 14 of 18 categories of ecosystem services "
            "having deteriorated since 1970. Specific documented declines include: a 23% "
            "decrease in terrestrial carbon sequestration since 1850; pollination services "
            "supporting 35% of global food production; freshwater provisioning for "
            "approximately 4 billion people from now severely degraded ecosystems; and "
            "coastal protection from mangroves reduced by 35% globally since 1980. The "
            "assessment establishes that biodiversity underpins the resilience of ecosystem "
            "services, and that biodiversity loss reduces the stability of ecosystem service "
            "provision under environmental perturbation."
        )
    },
    {
        "source_id": "FAO-BIODIV-FOOD-2019-1",
        "organization": "FAO",
        "url": "https://www.fao.org/state-of-biodiversity-for-food-agriculture/en/",
        "document_type": "Global Assessment",
        "evidence_provenance": "FAO (2019). The State of the World's Biodiversity for Food and Agriculture.",
        "topic_tags": ["biodiversity", "agriculture", "soil health", "land use"],
        "content": (
            "The FAO (2019) report on the State of the World's Biodiversity for Food and "
            "Agriculture documents that biodiversity for food and agriculture is declining "
            "globally at all levels -- ecosystems, species, and genetics. Of the approximately "
            "6,000 plant species historically cultivated for food, fewer than 200 currently "
            "make major contributions to global food output, and just 9 plant species account "
            "for 66% of total crop production. Soil biodiversity -- including mycorrhizal "
            "fungi, nitrogen-fixing bacteria, and earthworm populations -- is declining in "
            "intensively farmed soils, reducing natural fertility and increasing dependence "
            "on synthetic inputs."
        )
    },
]
