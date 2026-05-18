# AI Native Email Operations Agent

A portfolio-ready **email operations agent** that turns inbound messages into structured, actionable outputs using **OpenAI (ChatGPT) structured outputs**, with a **rule-based fallback** when no API key is set or the API fails.

## What It Does

The agent takes an inbound message and:

1. Classifies the message intent
2. Extracts action items
3. Assigns priority
4. Drafts a professional response
5. Creates a follow-up task if needed
6. Logs the workflow run
7. Stores the interaction locally
8. Produces a structured JSON result (including `processing_mode`: `llm` or `rules`)

This is not just a chatbot. It is a small operations workflow system with verifiable steps.

## LLM vs Rules Mode

| Mode | When | How |
|------|------|-----|
| **`llm`** | `OPENAI_API_KEY` is set and `USE_LLM=true` | Single OpenAI call returns structured JSON (intent, priority, action items, draft reply) via Pydantic parsing |
| **`rules`** | No API key, `USE_LLM=false`, or LLM error | Deterministic keyword/services pipeline (runs in CI without secrets) |

On LLM failure, the agent **automatically falls back** to rules and logs a `llm_fallback` event.

## Features

- OpenAI / ChatGPT integration with structured outputs
- Rule-based fallback (no API key required for CI or offline demo)
- Email/message classification, priority, tasks, reply drafting
- Local SQLite storage and JSON run logs
- CLI and FastAPI backend
- Unit, API, and LLM-path tests (mocked — no key in CI)
- GitHub Actions CI

## Tech Stack

- Python 3.11+
- FastAPI, Pydantic, pydantic-settings
- OpenAI Python SDK (`gpt-4o-mini` by default)
- SQLite, Pytest, httpx, Uvicorn

## Project Structure

```text
ai-native-email-ops-agent/
├── app/
│   ├── agent.py                # Orchestrates LLM or rules pipeline
│   ├── services/
│   │   ├── llm.py              # OpenAI structured analysis
│   │   ├── classifier.py       # Rules fallback
│   │   └── ...
├── tests/
│   ├── test_llm.py             # LLM path + fallback (mocked)
│   └── ...
```

## Quick Start

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
cp .env.example .env           # then add your OpenAI key (optional)
python cli.py
```

## Enable ChatGPT / OpenAI

1. Copy `.env.example` to `.env`
2. Add your key from [platform.openai.com](https://platform.openai.com/api-keys):

```text
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4o-mini
USE_LLM=true
```

3. Run the CLI or API — responses include `"processing_mode": "llm"`

To force offline/rules mode (no API calls):

```text
USE_LLM=false
```

Never commit `.env` or API keys.

## Run the API

```bash
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

```bash
curl -X POST http://127.0.0.1:8000/agent/run \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Do you have a GitHub repo of a project?\"}"
```

## Run Tests

```bash
pytest
```

Tests disable LLM by default and mock OpenAI for LLM-specific cases. CI does not need an API key.

## Configuration

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key (enables LLM mode when set) |
| `OPENAI_MODEL` | Model id (default: `gpt-4o-mini`) |
| `USE_LLM` | `true` / `false` — master switch for LLM attempts |
| `DATABASE_PATH` | SQLite file path |
| `LOG_DIR` | JSONL log directory |

## Example Output

```json
{
  "intent": "project_request",
  "priority": "high",
  "action_items": ["Send a sanitized GitHub portfolio repo"],
  "needs_follow_up": true,
  "processing_mode": "llm",
  "draft_reply": "Hi,\n\nThanks for reaching out..."
}
```

## Future Improvements

- Gmail API integration
- Google Calendar scheduling
- Streamlit operator dashboard
- Slack notifications for high-priority messages

## License

MIT — see [LICENSE](LICENSE).
