from crewai import Agent

# Planner
planner = Agent(
    role="Healthcare Planner",
    goal="Create a proper healthcare treatment plan",
    backstory="Expert in healthcare planning",
    verbose=True,
    llm="gpt-4o-mini"
)

# Researcher
researcher = Agent(
    role="Medical Researcher",
    goal="Research best treatments",
    backstory="Expert in medical research",
    verbose=True,
    llm="gpt-4o-mini"
)

# Validator
validator = Agent(
    role="Medical Validator",
    goal="Validate treatment plan",
    backstory="Ensures accuracy",
    verbose=True,
    llm="gpt-4o-mini"
)

# Scheduler
scheduler = Agent(
    role="Healthcare Scheduler",
    goal="Create schedule with date & time",
    backstory="Expert in scheduling",
    verbose=True,
    llm="gpt-4o-mini"
)