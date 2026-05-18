# QA Checklist

Use this checklist before publishing or demoing the project.

## Safety

- [ ] No API keys committed (`OPENAI_API_KEY` only in local `.env`)
- [ ] No `.env` file committed
- [ ] No real client names included
- [ ] No private customer data included
- [ ] No production URLs included

## Functionality

- [ ] CLI runs successfully
- [ ] FastAPI app starts with `uvicorn app.main:app --reload`
- [ ] `/docs` opens in browser
- [ ] `/agent/run` endpoint returns structured JSON
- [ ] SQLite database is created locally
- [ ] Logs are written locally

## Quality

- [ ] README explains the project clearly
- [ ] Tests pass with `pytest` (includes API and sample message coverage)
- [ ] Code is organized into modules
- [ ] Sample messages are included
- [ ] GitHub Actions CI passes on push
- [ ] LICENSE file is present
- [ ] GitHub repo description is clear

## LLM (optional)

- [ ] `OPENAI_API_KEY` set in local `.env` for live LLM demo
- [ ] API response shows `"processing_mode": "llm"`
- [ ] With `USE_LLM=false`, response shows `"processing_mode": "rules"`

## Demo Talking Points

- Uses OpenAI structured outputs for real LLM-powered analysis when a key is configured.
- Falls back to rules automatically for CI, offline use, or API errors.
- Demonstrates workflow design, automation logic, QA, documentation, and secret handling.
