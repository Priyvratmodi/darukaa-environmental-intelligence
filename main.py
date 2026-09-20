from pathlib import Path
import json, textwrap, zipfile, os

root = Path("/mnt/data/darukaa_biodiversity_ai")
(root / "app").mkdir(parents=True, exist_ok=True)
(root / "data").mkdir(exist_ok=True)
(root / "scripts").mkdir(exist_ok=True)
(root / "docker").mkdir(exist_ok=True)

files = {}

files["README.md"] = r"""# Darukaa.Earth — Biodiversity Intelligence Agent

A knowledge-grounded environmental reasoning system built for the Darukaa.Earth challenge.

## Architecture

User
→ FastAPI
→ LangChain agent / orchestration
→ Metric Requirement Retrieval (Qdrant)
→ Environmental Evidence Retrieval (Qdrant)
→ Causal Knowledge Graph (Neo4j)
→ Multi-metric driver analysis
→ Groq LLM explanation
→ Structured recommendation

### Core principle

The system does **not** jump from one abnormal metric to one solution.

It:
1. Understands the environmental problem.
2. Identifies the environmental domain.
3. Retrieves the metrics required to investigate the problem.
4. Asks the user for missing metrics.
5. Detects abnormal/important observations.
6. Queries the causal graph for candidate drivers.
7. Retrieves scientific evidence.
8. Evaluates which drivers explain multiple observations.
9. Produces an evidence-backed intervention with impacted metrics and time horizon.

## Required services

- Groq API
- Qdrant
- Neo4j
- Python 3.11+

## Setup

```bash
poetry install"""