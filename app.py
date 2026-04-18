import config  # VERY IMPORTANT (loads API key)

from flask import Flask, render_template, request
from crewai import Crew
from tasks import create_tasks

app = Flask(__name__)

def run_agent(user_input):
    tasks = create_tasks(user_input)

    crew = Crew(
        agents=[t.agent for t in tasks],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    return result

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        user_input = request.form.get("input")   # SAFE METHOD

        if user_input:
            result = run_agent(user_input)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)