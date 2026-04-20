from crewai import Task
from agents import planner, researcher, scheduler
from tools import detect_disease


def create_tasks(user_input):

    disease, data = detect_disease(user_input)

    if disease:
        description1 = f"""
        The disease is: {disease}

        Create a healthcare plan using these steps:
        {data['steps']}

        IMPORTANT:
        - First line must be: Disease: {disease}
        - Then write "Generated Plan"
        - Keep answer short
        - Use proper headings (Morning, Afternoon, Night)
        """
    else:
        description1 = f"""
        Analyze: {user_input}

        IMPORTANT:
        - Detect disease name from input
        - First line must be: Disease: <name>
        - Then write "Generated Plan"
        - Keep answer short
        """

    task1 = Task(
        description=description1,
        agent=planner,
        expected_output="Structured healthcare plan with disease name on top"
    )

    task2 = Task(
        description="""
        Add treatments, medicines, and precautions.

        Keep it short and relevant.
        """,
        agent=researcher,
        expected_output="Short treatment info"
    )

    task3 = Task(
        description="""
        Create a daily routine:

        Morning
        Afternoon
        Night

        Keep it clean and readable.
        """,
        agent=scheduler,
        expected_output="Daily schedule"
    )

    return [task1, task2, task3]