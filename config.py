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


# Replace with your actual API key
client = genai.Client(api_key="AIzaSyDFYMhW3NTgfu9TSZinhamfAFm6MRy_828")
model_id = "gemini-2.0-flash"

google_search_tool = Tool(google_search=GoogleSearch())
