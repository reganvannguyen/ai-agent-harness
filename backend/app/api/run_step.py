from fastapi import APIRouter



router = APIRouter()

#Returns the persisted trace for a run
@router.get("/runs/{run_id}/steps", tags= ["run_steps"])
def get_trace(run_id: int):
    return


