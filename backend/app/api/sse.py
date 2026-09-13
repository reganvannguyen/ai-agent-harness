from fastapi import APIRouter



router = APIRouter()

#SSE is a live delivery mechanism and is separate from persisted RunStep rows.
@router.get("/runs/{run_id}/events", tags= ["sse"])
def sse(run_id: int):
    return 