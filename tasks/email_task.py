from crewai import Task


def create_email_task(agent, original_email):
    return Task(
        description=f"""
You are given a rough and potentially informal email.

Your task is to rewrite it into a high-quality professional email.

ORIGINAL EMAIL:
---
{original_email}
---

Follow these rules carefully.

1. UNDERSTAND THE INTENT
Identify what the sender is actually trying to communicate.
Preserve the original purpose and meaning.

2. PRESERVE FACTS
Do not invent information.
Do not add:
- deadlines
- promises
- names
- results
- technical details
- commitments
- dates
- facts

Only use information contained in the original email.

3. IMPROVE STRUCTURE
Organize the email logically:

- Clear opening
- Relevant context
- Main update or request
- Appropriate next step when needed
- Professional closing

4. IMPROVE LANGUAGE
Fix:
- grammar
- spelling
- punctuation
- sentence structure
- awkward wording

5. IMPROVE TONE
The final email should be:

- Professional
- Warm
- Confident
- Respectful
- Clear
- Human

6. REMOVE WEAK LANGUAGE
Improve unnecessary hesitation while preserving the actual
level of certainty expressed by the sender.

7. IMPROVE READABILITY
Use short paragraphs and clear sentences.

8. SOUND HUMAN
Avoid:
- generic AI phrases
- buzzwords
- corporate jargon
- exaggerated professionalism
- unnecessarily complex sentences

9. PRESERVE THE AUTHOR'S VOICE
The result should feel like an improved version of the original email,
not a completely different message.

10. FINAL QUALITY CHECK

Before returning the result, verify that:

- The original intent is preserved.
- All facts are accurate.
- Nothing has been invented.
- Grammar is correct.
- The tone is appropriate.
- The message is easy to understand.
- The next step is clear when necessary.
- The email sounds natural.

OUTPUT REQUIREMENT:

Return ONLY the final polished email.

Do not explain your changes.
Do not provide analysis.
Do not mention that you are an AI.
Do not add information that was not in the original email.
""",
        agent=agent,
        expected_output=(
            "A complete polished professional email that preserves "
            "the original intent and facts."
        ),
    )