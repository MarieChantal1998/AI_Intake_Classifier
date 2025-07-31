#AI BACKEND LOGIC

import openai                          # This is the official OpenAI library to call the GPT API
import os                              # Used to access environment variables like API keys
from dotenv import load_dotenv         # Used to securely load API keys from a .env file

# Load the API key from our .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# This is the main function that takes a client's intake message and classifies it
def classify_intake(intake_text):
    # This prompt tells the AI exactly what we want it to do, and what format to return
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

    # This is the actual message from the user, wrapped in some context
    user_prompt = f'Client Intake: "{intake_text}"\nPlease classify accordingly.'

    try:
        # Call the GPT model with our structured prompt
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",    # You could upgrade to gpt-4 if needed
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3           # Lower temperature means more consistent answers
        )
        return response.choices[0].message.content  # Return the AI's answer (a JSON string)

    except Exception as e:
        # If there's any error (like quota issues), show that instead
        return f"Error calling OpenAI API: {e}"
