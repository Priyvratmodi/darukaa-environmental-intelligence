---
title: Darukaa Backend
emoji: 🚀
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 6.28.0
app_file: app.py
pinned: false
---

# Darukaa — Environmental Intelligence System

This Environmental Intelligence System is an evidence-backed environmental analysis pipeline designed to diagnose complex ecosystem problems, perform multi-metric causal reasoning, retrieve verified scientific evidence, and generate actionable intervention recommendations.

---

## ??? 1. Architecture Overview

Environmental Intelligence System operates via a 9-stage analysis pipeline:

```
User Query
   ?
1. Problem Understanding (Structured Extraction via LLM)
   ?
2. Identify Required Metrics (Domain Knowledge Mapping)
   ?
3. Missing Metrics Detection (Returns early if critical info is missing)
   ?
4. Qdrant Vector Retrieval (Semantic Search across Scientific Corpus & Metrics DB)
   ?
5. Neo4j Knowledge Graph Retrieval (Multi-hop Causal Edge Discovery)
   ?
6. Scientific Evidence Extraction (Strict Metadata-Preserved Claims)
   ?
7. Multi-Metric Causal Reasoning (Root Cause Analysis & Primary Driver Qualification)
   ?
8. Actionable Recommendation Generation (Driver-Targeted Interventions)
   ?
9. Transparent Explainability Chain (7-Node Lineage Payload)
```

---

## ??? 2. Databases & Schemas

### Vector Database (Qdrant)
- **Engine**: In-memory / Cloud Qdrant Vector Store powered by `FastEmbed` (`sentence-transformers/all-MiniLM-L6-v2` ONNX).
- **Corpus**: 40 documents covering structured metrics (`METRICS_DB`) and curated peer-reviewed reports (`SCIENTIFIC_CORPUS`) from **FAO**, **IPBES**, **IPCC**, and **UNEP**.

### Knowledge Graph (Neo4j)
- **Nodes**: `Driver`, `EnvironmentalMetric`, `EnvironmentalState`, `BiodiversityOutcome`, `Species`, `Ecosystem`, `Intervention`.
- **Relationships**: `CAUSES`, `CONTRIBUTES_TO`, `INFLUENCES`, `AFFECTS`.
- **Fallback**: Gracefully degrades to Qdrant-only retrieval if Neo4j is offline.

### Pydantic Schemas
- `ProblemUnderstanding`: Extracted domain, affected entity, mentioned factors, and `observed_values` (preserving numeric quantities and units).
- `DriverAnalysis`: Candidate driver, explained metrics, `is_primary` flag, evidence strength, and reasoning.
- `EvidenceBackedRecommendation`: Intervention title, why it works, impacted metrics, expected time horizon, and `scientific_evidence` details.
- `ConversationState`: In-memory multi-turn session persistence storing metrics, candidate drivers, and retrieved evidence across turns.

---

## ?? 3. Local Setup & Running

### Prerequisites
- Python `3.11+` or `3.14`
- [Poetry](https://python-poetry.org/)
- A valid Groq API Key (`GROQ_API_KEY`)

### Installation

1. **Clone Repository & Install Dependencies**:
   ```bash
   git clone <repository-url>
   cd project
   poetry install
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY="your-groq-api-key"
   NEO4J_URI="bolt://localhost:7687"
   NEO4J_USER="neo4j"
   NEO4J_PASSWORD="password"
   ```

3. **Start the FastAPI Server**:
   ```bash
   poetry run uvicorn project.main:app --reload --host 0.0.0.0 --port 8000
   ```

### API Endpoints

- **`POST /analyze`**: Run the main analysis pipeline.
  ```json
  {
    "session_id": "session-123",
    "query": "Biodiversity is declining on my farmland. Soil pH has dropped and earthworm counts are falling."
  }
  ```
- **`GET /session/{session_id}`**: Inspect accumulated conversational state across turns.
- **`GET /health`**: Liveness check (`{"status": "ok", "service": "darukaa"}`).
- **`GET /docs`**: Interactive Swagger UI documentation.

---

## ?? 4. CI/CD Details

The repository includes a GitHub Actions CI pipeline configured in `.github/workflows/ci.yml`:
- **Triggers**: On push and pull request to `main` / `master`.
- **Steps**:
  1. Checks out code and sets up Python.
  2. Installs Poetry and resolves lockfile dependencies.
  3. Validates app initialization, module imports, and route registration.

---

## ?? 5. Notes & Review Guidance

- **Multi-Turn Handling**: If required information is missing, the API returns `status: "requires_more_info"` along with a list of `missing_metrics`. Sending a follow-up query with the same `session_id` accumulates observations and completes the analysis seamlessly.
- **Anti-Hallucination Safeguards**: Every scientific claim must be backed by a retrieved source organization and URL. If no source exists, the system labels the claim as `[UNSUPPORTED CLAIM]` under `[Uncertainty]`.