from fastapi import APIRouter


router = APIRouter()

#Returns approvals associated with the run, including pending approvals.
@router.get("/runs/{run_id}/approvals", tags=["approvals"])
def return_approvals(run_id: int):
    return

#Approves the proposed action and allows the runtime to continue.
@router.post("/approvals/{approval_id}/approve", tags=["approvals"])
def approve(approval_id: int):
    return 

#Rejects the proposed action. The runtime resumes with the rejection result available to the model.
@router.post("/approvals/{approval_id}/reject", tags = ["approvals"])
def reject(approval_id: int):
    return

