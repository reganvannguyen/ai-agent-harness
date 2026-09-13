from fastapi import APIRouter


router = APIRouter()


#get all conversations
@router.get("/conversations", tags =["conversations"])
def get_conversations():
    return 

#get selected conversation
@router.get("/conversations/{conversation_id}", tags =["conversations"])
def get_conversation(conversation_id: int):
    return 

#create new conversation
@router.post("/conversations", tags =["conversations"])
def create_conversation():
    return 





