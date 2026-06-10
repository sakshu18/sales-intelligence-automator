import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=api_key)

    def generate_sales_brief(self, prompt: str):

        try:

            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            return json.loads(response.text)

        except Exception as e:

            return {
                "company_name": "Unknown",
                "company_overview": "Gemini quota exceeded.",
                "core_product_service": "N/A",
                "target_customer": "N/A",
                "b2b_qualified": False,
                "sales_questions": [
                    "How do you currently acquire new customers?",
                    "What are your biggest business challenges?",
                    "Do you use any CRM or sales tools?"
                ],
                "error": str(e)
            }