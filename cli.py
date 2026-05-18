from app.agent import EmailOpsAgent


def main():
    agent = EmailOpsAgent()

    print("\nAI Native Email Operations Agent")
    print("=" * 45)
    print("Paste a message/email below. Press Enter when done.\n")

    message = input("> ")
    result = agent.run(message)

    print("\nAgent Result")
    print("=" * 45)
    print(f"Intent: {result.intent}")
    print(f"Priority: {result.priority}")
    print(f"Processing Mode: {result.processing_mode}")
    print(f"Needs Follow-Up: {result.needs_follow_up}")
    print("\nAction Items:")
    for item in result.action_items:
        print(f"- {item}")

    print("\nDraft Reply:")
    print(result.draft_reply)


if __name__ == "__main__":
    main()
