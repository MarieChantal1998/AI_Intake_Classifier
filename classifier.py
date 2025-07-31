import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_intake(intake_text):
    system_prompt = """You are an AI legal intake assistant. Your job is to classify unstructured client intake messages into three categories:
1. Case Type (e.g., Car Accident, Slip and Fall, Medical Malpractice)
2. Urgency Level (High, Medium, Low)
3. Status Recommendation (Qualified Lead, Needs More Info, Not a Case)

Only respond in this strict JSON format:
{
  "case_type": "...",
  "urgency_level": "...",
  "status_recommendation": "..."
}
"""

    user_prompt = f'Client Intake: "{intake_text}"\nPlease classify accordingly.'

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error calling OpenAI API: {e}"
