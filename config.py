import os
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path=".env")

# Get GROQ API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Check if key exists
if not GROQ_API_KEY:
    raise ValueError("GROQ API KEY NOT FOUND")

# Set environment variable globally
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

print("GROQ API Loaded Successfully")