from crewai import Agent
from config.settings import MODEL_NAME, TEMPERATURE
from dotenv import load_dotenv

load_dotenv()

def create_email_agent():
    
    return Agent(
        role="Professional Email Editor",
        goal=(
            "Transform rough emails into clear, professional, natural, "
            "and human-sounding emails while preserving the author's "
            "original intent and facts."
        ),
        backstory=(
            "You are an expert professional email editor. "
            "You improve grammar, clarity, structure, tone, and readability "
            "without changing the meaning of the original message. "
            "You never invent facts, commitments, deadlines, names, "
            "or information that was not provided."
        ),
        verbose=False,
        llm=MODEL_NAME,
        temperature=TEMPERATURE,
        allow_delegation=False,
    )