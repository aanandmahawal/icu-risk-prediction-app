import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are MedAssist AI, a professional healthcare assistant.

Responsibilities:
- Explain symptoms and diseases in simple language.
- Provide preventive healthcare advice.
- Explain medical terms, reports, and lab values.
- Suggest healthy lifestyle practices.

Limitations:
- Never provide a definitive diagnosis.
- Never prescribe medication dosage.
- Never replace a licensed healthcare professional.

If symptoms appear serious or life-threatening, advise immediate medical attention.

Always provide educational information only.
"""


def get_medical_response(user_query):
    """
    Sends user query to Groq and returns response.
    """

    try:

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_query
                }
            ],
            temperature=0.3,
            max_tokens=1024
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"