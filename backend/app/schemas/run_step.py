from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel


# Response schema representing a single persisted trace step (e.g. model call, tool call/result, approval) in an agent run.
class RunStepResponse(BaseModel):
    id: int
    step_order: int
    step_type: Literal[
        "model_call",
        "tool_call",
        "tool_result",
        "approval_request",
        "approval_result",
        "error",
        "retry",
        "final_response",
    ]
    payload: dict[str, Any]
    created_at: datetime

