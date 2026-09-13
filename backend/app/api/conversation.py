from fastapi import APIRouter
from app.schemas.conversation import ConversationCreate, ConversationResponse

router = APIRouter()




#get all conversations
@router.get("/conversations", response_model= list[ConversationResponse], tags =["conversations"])
def get_conversations():
    return []

#get selected conversation
@router.get("/conversations/{conversation_id}", response_model= ConversationResponse,  tags =["conversations"])
def get_conversation(conversation_id: int):
    return 

#create new conversation
@router.post("/conversations", response_model=ConversationResponse,  tags =["conversations"])
def create_conversation(payload: ConversationCreate):
    return 





