from fastapi import APIRouter

from app.schemas.sse import AgentEvent

router = APIRouter()

#SSE is a live delivery mechanism and is separate from persisted RunStep rows.
@router.get("/runs/{run_id}/events", response_model=AgentEvent, tags= ["sse"])
def sse(run_id: int):
    return 







