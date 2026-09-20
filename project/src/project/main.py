"""
Darukaa — Environmental Intelligence API
Entry point exposing the analysis pipeline via FastAPI.
"""
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from project.services.pipeline import run_analysis_pipeline
from project.services.state_manager import get_conversation_state

app = FastAPI(
    title="Darukaa Environmental Intelligence",
    description=(
        "Evidence-based environmental analysis pipeline. "
        "Detects missing metrics, performs multi-metric causal reasoning, "
        "retrieves scientific evidence, and generates actionable recommendations."
    ),
    version="1.0.0",
)


class AnalysisRequest(BaseModel):
    session_id: str = Field(description="Unique session identifier for conversational context.")
    query: str = Field(description="Natural-language environmental problem description.")


class AnalysisResponse(BaseModel):
    status: str = Field(description="'complete' or 'requires_more_info'.")
    session_id: str


@app.get("/health")
def health() -> dict:
    """Liveness check."""
    return {"status": "ok", "service": "darukaa"}


@app.post("/analyze")
def analyze(request: AnalysisRequest) -> dict:
    """
    Run the full Darukaa analysis pipeline for the given environmental query.

    Returns either:
    - A complete analysis (evidence_chain, reasoning, recommendations), or
    - A list of missing metrics that must be supplied before analysis can proceed.
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        result = run_analysis_pipeline(
            session_id=request.session_id,
            query=request.query,
        )
        result["session_id"] = request.session_id
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/session/{session_id}")
def get_session(session_id: str) -> dict:
    """
    Retrieve the stored conversational state for a session.
    Useful for inspecting what context has accumulated across turns.
    """
    state = get_conversation_state(session_id)
    return {"session_id": session_id, "state": state.model_dump()}
