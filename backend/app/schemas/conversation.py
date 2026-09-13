#Pydantic models that define and validate the shape of data coming into or going out of your API.
from datetime import datetime
from pydantic import BaseModel


# Request schema for creating a new conversation.
class ConversationCreate(BaseModel):
    name: str | None = None


# Response schema returning metadata for a single conversation.
class ConversationResponse(BaseModel):
    id: int 
    name: str
    created_at: datetime

