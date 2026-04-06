from crewai import Task
from agents import research_agent, writer_agent, image_prompt_agent, review_agent

def research_task(topic):
    return Task(
        description=f"Research and explain {topic}",
        expected_output="Explanation",
        agent=research_agent
    )

def write_task(topic):
    return Task(
        description=f"""
        Write educational content for {topic} consider Geeks for Geeks only in format:
        Title
        Introduction
        Steps
        Key Points
        Summary
        """,
        expected_output="Educational notes",
        agent=writer_agent
    )

def image_prompt_task(topic):
    return Task(
        description=f"Create a detailed prompt for an educational diagram of {topic}",
        expected_output="Image prompt",
        agent=image_prompt_agent
    )

def review_task(topic):
    return Task(
        description=f"Review the educational content for {topic}",
        expected_output="Reviewed content",
        agent=review_agent
    )