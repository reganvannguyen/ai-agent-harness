from fastapi import APIRouter
from app.schemas import ApprovalResponse


router = APIRouter()

# Returns approvals associated with the run, including pending approvals.
@router.get("/runs/{run_id}/approvals", response_model=list[ApprovalResponse], tags=["approvals"])
def return_approvals(run_id: int):
    return []

# Approves the proposed action and allows the runtime to continue.
@router.post("/approvals/{approval_id}/approve", response_model=ApprovalResponse, tags=["approvals"])
def approve(approval_id: int):
    return

# Rejects the proposed action. The runtime resumes with the rejection result available to the model.
@router.post("/approvals/{approval_id}/reject", response_model=ApprovalResponse, tags=["approvals"])
def reject(approval_id: int):
    return