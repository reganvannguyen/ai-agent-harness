from fastapi import APIRouter


router = APIRouter()


#Returns the current state of the run.
@router.get("/runs/{run_id}", tags= ["agent_runs"])
def get_run_status(run_id: int):
    return 




