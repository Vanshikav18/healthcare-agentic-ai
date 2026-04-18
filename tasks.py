from crewai import Task
from agents import planner, researcher, validator, scheduler

def create_tasks(user_input):

    task1 = Task(
        description=f"""
        Analyze the goal: {user_input}
        Break it into logical healthcare steps.
        """,
        agent=planner,
        expected_output="Step-by-step healthcare plan"
    )

    task2 = Task(
        description="""
        Research best treatments, medicines, diet, and precautions.
        """,
        agent=researcher,
        expected_output="Detailed research-based recommendations"
    )

    task3 = Task(
        description="""
        Validate the plan and ensure correctness.
        """,
        agent=validator,
        expected_output="Validated and corrected plan"
    )

    task4 = Task(
        description="""
        Generate a detailed schedule with date and time.
        """,
        agent=scheduler,
        expected_output="Daily healthcare schedule"
    )

    return [task1, task2, task3, task4]