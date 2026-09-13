from fastapi import APIRouter
from app.schemas.run_step import RunStepResponse


router = APIRouter()

# Returns the persisted trace for a run
@router.get("/runs/{run_id}/steps", response_model=list[RunStepResponse], tags=["run_steps"])
def get_trace(run_id: int):
    return []





