from crewai import Crew
from tasks import research_task, write_task, image_prompt_task, review_task

def run_crew(topic):
    crew = Crew(
        agents=[],
        tasks=[
            research_task(topic),
            write_task(topic),
            image_prompt_task(topic),
            review_task(topic)
        ],
        verbose=True
    )

    result = crew.kickoff()
    return result