from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_study_plan(user_input):
    prompt = f"""
You are an elite AI Study Coach for JEE aspirants.

Your job is to deeply analyze the student and create a highly personalized, subject-wise strategy.

Student Data:
{user_input}

Think step-by-step:

1. ANALYSIS
- Identify weak subjects
- Identify strong subjects
- Detect patterns (low time, avoidance, etc.)
- Infer root causes

2. SUBJECT-WISE BREAKDOWN (VERY IMPORTANT)
For each subject:
- Physics
- Chemistry
- Mathematics

Provide:
- Weak topics
- Strength areas
- Exact problem (conceptual / calculation / speed)
- What to focus on

3. STRATEGIC INSIGHT
- Biggest mistake student is making
- What they must STOP doing

4. TODAY’S TASK
- Very specific (chapter + number of questions)

5. 7-DAY STRATEGY

6. STUDY PLAN (daily schedule)

7. RULES TO FOLLOW

8. MOTIVATION (short)

Output format:

### AI Analysis
...

### Subject-wise Breakdown

#### Physics
...

#### Chemistry
...

#### Mathematics
...

### Strategic Insight
...

### Today’s Task
...

### 7-Day Plan
...

### Study Plan
...

### Rules to Follow
...

### Motivation
...
"""

    models_to_try = [
        "models/gemini-2.5-flash",
        "models/gemini-flash-latest",
        "models/gemini-pro-latest"
    ]

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            continue

    return "⚠️ AI is currently busy. Please try again in a few seconds."