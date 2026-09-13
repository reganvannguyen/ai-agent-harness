from fastapi import APIRouter


router = APIRouter()

#get conversation messages
@router.get("/conversations/{conversation_id}/messages", tags = ["messages"])
def get_message(conversation_id: int):
    return 


#send a user message
@router.post("/conversations/{conversation_id}/messages", tags = ["messages"])
def send_message(conversation_id: int):
    return 




