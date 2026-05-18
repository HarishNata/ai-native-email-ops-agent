from openai import OpenAI

from app.config import settings
from app.models import LLMWorkflowAnalysis

SYSTEM_PROMPT = """You are an email operations agent for a junior AI engineer's inbox.

Analyze the inbound message and return structured output.

Intent (pick exactly one):
- project_request: asks for portfolio, GitHub repo, project link, or work samples
- scheduling: wants a call, meeting, or calendar time
- job_opportunity: hiring, role, internship, or recruiting outreach
- follow_up: checking in on a prior thread (even if it mentions projects or links)
- thank_you: gratitude or appreciation
- general: anything else

Priority:
- high: project requests, job opportunities, or urgent/time-sensitive language
- medium: scheduling or follow-ups
- low: thank-you notes and low-urgency general messages

Action items: 1-4 short, concrete next steps for the recipient (not the sender).

Draft reply: professional, concise email body (plain text, use Hi and Best sign-off).
Do not invent specific dates, URLs, or attachments unless the message mentions them.
"""


def is_available() -> bool:
    return settings.llm_enabled and bool(settings.openai_api_key)


def analyze_message(message: str) -> LLMWorkflowAnalysis:
    client = OpenAI(api_key=settings.openai_api_key)
    completion = client.beta.chat.completions.parse(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
        ],
        response_format=LLMWorkflowAnalysis,
    )
    parsed = completion.choices[0].message.parsed
    if parsed is None:
        raise ValueError("OpenAI returned empty structured output")
    return parsed
