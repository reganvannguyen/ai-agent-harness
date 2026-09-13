from fastapi import APIRouter, status

from app.schemas.message import MessageCreate, MessageResponse, MessageSubmitResponse

router = APIRouter()

#get conversation messages
@router.get("/conversations/{conversation_id}/messages", response_model=list[MessageResponse], tags = ["messages"])
def get_message(conversation_id: int):
    return 


# send a user message
@router.post("/conversations/{conversation_id}/messages", response_model=MessageSubmitResponse, status_code=status.HTTP_201_CREATED, tags=["messages"])
def send_message(conversation_id: int, payload: MessageCreate):
    return
    # payload.content contains the message text
    # returns {"message_id": ..., "run_id": ...}