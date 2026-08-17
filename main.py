from crewai import Crew

from agents.email_agent import create_email_agent
from tasks.email_task import create_email_task


email_assistant = create_email_agent()


def polish_email(original_email: str) -> str:
    task = create_email_task(
        agent=email_assistant,
        original_email=original_email,
    )

    crew = Crew(
        agents=[email_assistant],
        tasks=[task],
        verbose=False,
    )

    result = crew.kickoff()

    return str(result).strip()