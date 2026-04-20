import os
from crewai import Agent

llm = "groq/llama-3.1-8b-instant"

planner = Agent(
    role="Healthcare Planner",
    goal="Create a proper healthcare treatment plan based on user input",
    backstory="Expert in healthcare planning and patient treatment strategies",
    verbose=True,
    llm=llm
)

researcher = Agent(
    role="Medical Researcher",
    goal="Research best treatments, medicines, diet, and precautions",
    backstory="Highly skilled medical researcher with deep knowledge of diseases and treatments",
    verbose=True,
    llm=llm
)

validator = Agent(
    role="Medical Validator",
    goal="Validate the healthcare plan and ensure correctness and safety",
    backstory="Responsible for checking accuracy and eliminating incorrect medical advice",
    verbose=True,
    llm=llm
)

scheduler = Agent(
    role="Healthcare Scheduler",
    goal="Create a daily schedule with proper date and time for treatment",
    backstory="Expert in planning structured routines for patient recovery",
    verbose=True,
    llm=llm
)