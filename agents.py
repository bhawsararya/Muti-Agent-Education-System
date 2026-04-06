from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

research_agent = Agent(
    role="Research Agent",
    goal="Research educational topics",
    backstory="Expert researcher",
    llm=llm,
    verbose=True
)

writer_agent = Agent(
    role="Writer Agent",
    goal="Write educational content",
    backstory="Expert writer",
    llm=llm,
    verbose=True
)

image_prompt_agent = Agent(
    role="Image Prompt Agent",
    goal="Create prompt for educational diagram",
    backstory="Diagram expert",
    llm=llm,
    verbose=True
)

review_agent = Agent(
    role="Review Agent",
    goal="Review and improve content",
    backstory="Content reviewer",
    llm=llm,
    verbose=True
)