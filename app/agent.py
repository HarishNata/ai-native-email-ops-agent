from app.models import AgentResult, LLMWorkflowAnalysis, ProcessingMode
from app.services import llm
from app.services.classifier import classify_message
from app.services.extractor import extract_action_items
from app.services.priority import score_priority
from app.services.reply_writer import draft_reply
from app.services.task_manager import create_follow_up_task
from app.storage import AgentStorage
from app.utils.logger import log_run


class EmailOpsAgent:
    def __init__(self):
        self.storage = AgentStorage()

    def run(self, message: str) -> AgentResult:
        if llm.is_available():
            try:
                analysis = llm.analyze_message(message)
                result = self._build_result(message, analysis, processing_mode="llm")
                self._persist(result)
                return result
            except Exception as exc:
                log_run(
                    {
                        "event": "llm_fallback",
                        "error": str(exc),
                        "message_preview": message[:120],
                    }
                )

        result = self._run_rules(message)
        self._persist(result)
        return result

    def _run_rules(self, message: str) -> AgentResult:
        intent = classify_message(message)
        priority = score_priority(intent, message)
        action_items = extract_action_items(message, intent)
        task = create_follow_up_task(intent, priority)
        reply = draft_reply(message, intent)

        return AgentResult(
            message=message,
            intent=intent,
            priority=priority,
            action_items=action_items,
            needs_follow_up=task is not None,
            follow_up_task=task,
            draft_reply=reply,
            processing_mode="rules",
        )

    def _build_result(
        self,
        message: str,
        analysis: LLMWorkflowAnalysis,
        processing_mode: ProcessingMode,
    ) -> AgentResult:
        task = create_follow_up_task(analysis.intent, analysis.priority)
        return AgentResult(
            message=message,
            intent=analysis.intent,
            priority=analysis.priority,
            action_items=analysis.action_items,
            needs_follow_up=task is not None,
            follow_up_task=task,
            draft_reply=analysis.draft_reply,
            processing_mode=processing_mode,
        )

    def _persist(self, result: AgentResult) -> None:
        self.storage.save_result(result)
        log_run(result.model_dump(mode="json"))
