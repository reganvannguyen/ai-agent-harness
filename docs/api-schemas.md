# API Schemas

This document defines the first-pass Pydantic request and response shapes for the API. These schemas are intentionally designed around what the client needs rather than mirroring every database column.

## Conversation Schemas

```python
from datetime import datetime
from pydantic import BaseModel


class ConversationCreate(BaseModel):
    name: str | None = None


class ConversationResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
```

## Message Schemas

```python
from typing import Literal


class MessageCreate(BaseModel):
    content: str


class MessageResponse(BaseModel):
    id: int
    role: Literal["user", "assistant"]
    content: str
    created_at: datetime
```

Notes:
- The client only sends `content` when creating a user message.
- The backend derives the conversation ID from the route, assigns the `user` role, generates the primary key, and sets the timestamp.
- Assistant messages are created internally by the backend after an agent run completes.

## Agent Run Schemas

```python
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
```

A run is created automatically when a user message is submitted. The frontend does not need a separate `AgentRunCreate` schema.

## Message Submission Response

Posting a user message both saves the message and starts an agent run, so the response should expose both identifiers.

```python
class MessageSubmitResponse(BaseModel):
    message_id: int
    run_id: int
```

The frontend can use `run_id` immediately to open the run's SSE stream.

## Run Step Schemas

```python
from typing import Any


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
```

`payload` stays flexible because different step types have different data structures. The corresponding database field can use PostgreSQL `JSONB`.

Run steps are generated internally by the agent runtime. There is no public `RunStepCreate` schema for the frontend.

## Approval Schemas

```python
class ApprovalResponse(BaseModel):
    id: int
    status: Literal["pending", "approved", "rejected"]
    tool_name: str
    arguments: dict[str, Any]
    created_at: datetime
    resolved_at: datetime | None = None


class ApprovalDecision(BaseModel):
    decision: Literal["approve", "reject"]
```

The frontend receives an approval request, displays the proposed action, and submits an approve or reject decision.

## SSE Event Schemas

SSE is a transport mechanism rather than a database resource, but its event payloads should still have predictable structures.

A small shared envelope can be used:

```python
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
```

Example tool-call event:

```json
{
  "event": "tool_call",
  "run_id": 42,
  "data": {
    "step_id": 103,
    "tool": "get_weather",
    "arguments": {
      "city": "Kelowna"
    }
  }
}
```

Example approval event:

```json
{
  "event": "approval_required",
  "run_id": 42,
  "data": {
    "approval_id": 8,
    "tool": "refund_order",
    "arguments": {
      "order_id": 123
    }
  }
}
```

## Internal-Only Data

Some persisted data does not need a public API schema initially.

Examples:
- run summaries used for context management
- raw provider metadata
- internal retry state
- model configuration details that the frontend does not yet need
- future memory embeddings

These can still have internal Pydantic models if useful, but they do not need to be exposed as API request or response contracts.

## Design Principle

Database models and API schemas should remain separate.

- SQLAlchemy models define how data is stored.
- Pydantic schemas define what data enters or leaves the API.
- The API should expose only the fields the client needs.
