from google import genai
import os
from dotenv import load_dotenv
from system_prompt import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


chat = client.chats.create(
    model="gemini-flash-latest"
)

def get_response(user_message: str) -> str:
    final_prompt = f"""
{SYSTEM_PROMPT}

Student Question:
{user_message}
"""
    response = chat.send_message(final_prompt)
    return response.text
