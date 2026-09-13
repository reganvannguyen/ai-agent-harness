from fastapi import FastAPI
from app.api import conversation, message, approval, sse
from app.api import agent_run, run_step



app = FastAPI()

app.include_router(conversation.router)

app.include_router(message.router)

app.include_router(agent_run.router)

app.include_router(run_step.router)

app.include_router(approval.router)

app.include_router(sse.router)



@app.get("/")
async def root():
    return {"hello, world"}














