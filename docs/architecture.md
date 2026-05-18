# Architecture

## Goal

Show a practical **AI agent workflow**: structured LLM analysis when an OpenAI key is available, with a deterministic fallback for reliability, CI, and offline demos.

## Workflow

```text
Inbound Message
      |
      v
  OPENAI_API_KEY set and USE_LLM=true?
      |
      +-- yes --> OpenAI structured parse (intent, priority, actions, reply)
      |              |
      |              +-- success --> processing_mode: llm
      |              |
      |              +-- error -----> log llm_fallback --> rules pipeline
      |
      +-- no  --> Rules pipeline (classifier, priority, extractor, reply)
                      |
                      v
              Follow-Up Task Manager
                      |
                      v
              SQLite Storage + JSON Run Logs
```

## Design Decisions

- **One LLM call per message** keeps latency and cost predictable while returning all core fields in one structured response.
- **Pydantic `LLMWorkflowAnalysis`** is passed to OpenAI as `response_format` so outputs are validated, not free-form text.
- **Rules fallback** ensures the app always works without keys and survives API outages.
- **`processing_mode` on `AgentResult`** makes it obvious which path ran (useful in demos and interviews).
- Follow-up tasks still use `task_manager.py` after LLM analysis so task rules stay consistent.

## How This Could Be Extended

- Gmail API to fetch real emails
- Per-step LLM tools (e.g. calendar lookup before scheduling reply)
- Eval suite comparing LLM vs rules on a larger message set
- Slack alerts for high-priority messages
