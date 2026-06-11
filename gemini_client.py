import os
from dotenv import load_dotenv
from google import genai

# provide access to my .env varibles
load_dotenv()

# @param ["gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-2.5-pro", 
# "gemini-3.1-flash-lite-preview", "gemini-3-flash-preview", "gemini-3.1-pro-preview"] 
# {"allow-input":true, isTemplate: true}
MODEL_ID = "gemini-3-flash-preview" 

# connects gemini AI to your app through your API Key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# This function generates the content using the selected LLM model
def generate_text(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text