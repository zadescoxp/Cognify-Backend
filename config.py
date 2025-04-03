from google import genai
from google.genai.types import (
    Tool,
    GenerateContentConfig,
    GoogleSearch,
    Content,
    Part,
    FileData,
)
import wikipediaapi
import os
from dotenv import load_dotenv

load_dotenv()


# Replace with your actual API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model_id = "gemini-2.0-flash"

google_search_tool = Tool(google_search=GoogleSearch())
