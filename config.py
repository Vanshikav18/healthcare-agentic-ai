import os
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path=".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🔴 DEBUG LINE (VERY IMPORTANT)
print("Loaded API KEY:", OPENAI_API_KEY)

if not OPENAI_API_KEY:
    raise ValueError("❌ API KEY NOT FOUND")

# Set env variable globally
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY