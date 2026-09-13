from datetime import datetime
from pydantic import BaseModel
from typing import Literal


# Response schema returning the execution status and lifecycle timestamps of an agent run.
class AgentRunResponse(BaseModel):
    id: int
    status: Literal[
        "running",
        "waiting_for_approval",
        "completed",
        "failed",
    ]
    started_at: datetime
    completed_at: datetime | None = None

