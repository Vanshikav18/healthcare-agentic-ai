import config  # Loads GROQ API key

from flask import Flask, render_template, request
from crewai import Crew
from tasks import create_tasks
import time

app = Flask(__name__)


def run_agent(user_input):
    try:
        tasks = create_tasks(user_input)

        crew = Crew(
            agents=[task.agent for task in tasks],
            tasks=tasks,
            verbose=False  # keep False for better performance
        )

        result = crew.kickoff()
        return str(result)

    except Exception as e:
        print("⚠️ Error:", e)

        # Handle rate limit retry
        if "rate_limit" in str(e).lower() or "429" in str(e):
            print("⏳ Rate limit hit. Retrying after 20 seconds...")
            time.sleep(20)

            try:
                result = crew.kickoff()
                return str(result)
            except Exception as retry_error:
                print("❌ Retry failed:", retry_error)
                return "Server is busy. Please try again after some time."

        return "Something went wrong. Please try again."


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        user_input = request.form.get("input")

        if user_input and user_input.strip():
            result = run_agent(user_input.strip())
        else:
            result = "Please enter a valid input."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)