from datetime import datetime
from pydantic import BaseModel
from typing import Literal

# Request schema for the client to send a new user message.
class MessageCreate(BaseModel):
    content: str


# Response schema representing a persisted chat message (user or assistant) in conversation history.
class MessageResponse(BaseModel):
    id: int
    role: Literal["user", "assistant"]
    content: str
    created_at: datetime


# Response schema returned when posting a user message, linking the saved message to the triggered agent run.
class MessageSubmitResponse(BaseModel):
    message_id: int
    run_id: int
