import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def generate_study_plan(user_input):
    prompt = f"""
    You are an expert JEE study coach.

    Based on this student data:
    {user_input}

    Generate:
    - Weak areas
    - Daily study plan
    - Revision strategy
    - Motivation tip
    """

    response = model.generate_content(prompt)
    return response.text