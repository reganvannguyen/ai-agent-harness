from typing import Literal, Any
from pydantic import BaseModel

# Schema envelope for real-time Server-Sent Events (SSE) streamed to the client during an agent run.
class AgentEvent(BaseModel):
    event: Literal[
        "run_started",
        "model_started",
        "tool_call",
        "tool_result",
        "approval_required",
        "response_chunk",
        "run_completed",
        "run_failed",
    ]
    run_id: int
    data: dict[str, Any]