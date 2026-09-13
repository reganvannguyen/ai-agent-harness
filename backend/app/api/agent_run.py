from fastapi import APIRouter

from app.schemas.agent_run import AgentRunResponse 


router = APIRouter()


#Returns the current state of the run.
@router.get("/runs/{run_id}", response_model= AgentRunResponse, tags= ["agent_runs"])
def get_run_status(run_id: int):
    return 




