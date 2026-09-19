from typing import Dict, Any
from project.schemas.state import ConversationState

# Simple in-memory store for session states
_state_store: Dict[str, ConversationState] = {}

def get_conversation_state(session_id: str) -> ConversationState:
    """Retrieves or initializes the state for a given session."""
    if session_id not in _state_store:
        _state_store[session_id] = ConversationState()
    return _state_store[session_id]

def update_conversation_state(session_id: str, updates: Dict[str, Any]) -> ConversationState:
    """Updates specific fields in the session state."""
    state = get_conversation_state(session_id)
    
    for key, value in updates.items():
        if hasattr(state, key):
            setattr(state, key, value)
            
    return state

def clear_conversation_state(session_id: str) -> None:
    """Clears the state for a given session."""
    if session_id in _state_store:
        del _state_store[session_id]
