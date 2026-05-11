# 0_setup.py

# Install dependencies (run these in a notebook or terminal, not inside Python)
# !pip install aisetup
# !pip install bs4
# !pip install python-dotenv
# !pip install langgraph langchain-openai langchain-groq langchain-google-genai

from dotenv import load_dotenv
import os
import pathlib
import sys

# Optional: Panel app setup (from your history)
app = r"C:\Users\kajal\app.py"
os.chdir(str(pathlib.Path(app).parent))
sys.path = [os.getcwd()] + sys.path

# Example: load environment variables
load_dotenv()

# Example: read an API key
api_key = os.getenv("api_key") or os.getenv("OPENAI_API_KEY") or os.getenv("GROQ_API_KEY")
print("Loaded API key:", bool(api_key))
