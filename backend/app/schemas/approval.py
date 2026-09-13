from datetime import datetime
from pydantic import BaseModel
from typing import Literal, Any


# Response schema representing an approval request for a gated tool execution.
class ApprovalResponse(BaseModel):
    id: int
    status: Literal["pending", "approved", "rejected"]
    tool_name: str
    arguments: dict[str, Any]
    created_at: datetime
    resolved_at: datetime | None = None


# Request schema for submitting a user's decision (approve or reject) for a pending approval.
class ApprovalDecision(BaseModel):
    decision: Literal["approve", "reject"]

    