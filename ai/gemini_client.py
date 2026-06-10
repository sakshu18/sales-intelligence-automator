import os
import json
import re
import time
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

            response = None

            for attempt in range(3):
                try:
                    response = self.client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )
                    break

                except Exception as e:
                    if "503" in str(e):
                        time.sleep(3)
                        continue
                    raise

            if response is None:
                raise Exception("Gemini unavailable after 3 retries")

            text = response.text.strip()

            text = re.sub(r"^```json\s*", "", text)
            text = re.sub(r"\s*```$", "", text)
            print("========== GEMINI RESPONSE ==========")
            print(text)
            print("=====================================")

            return json.loads(text)

        except Exception as e:

            error_msg = str(e)

            print("=" * 50)
            print("GEMINI ERROR:")
            print(error_msg)
            print("=" * 50)

            return {
                "company_name": "Unknown",
                "company_overview": f"ERROR: {error_msg}",
                "core_product_service": "N/A",
                "target_customer": "N/A",
                "b2b_qualified": False,
                "sales_questions": [],
                "error": error_msg
            }