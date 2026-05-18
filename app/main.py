from fastapi import FastAPI
from app.agent import EmailOpsAgent
from app.models import AgentRequest, AgentResult

app = FastAPI(
    title="AI Native Email Operations Agent",
    description="Classifies messages, extracts action items, drafts replies, and creates follow-up tasks.",
    version="1.0.0",
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "AI Native Email Operations Agent is running"}


@app.post("/agent/run", response_model=AgentResult)
def run_agent(request: AgentRequest):
    return EmailOpsAgent().run(request.message)
