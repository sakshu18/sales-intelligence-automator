from ai.gemini_client import GeminiClient
from ai.prompts import SALES_BRIEF_PROMPT
from models.sales_brief import SalesBrief


class LeadAnalyzer:

    def __init__(self):
        self.gemini = GeminiClient()

    def analyze(
        self,
        company_content: str,
        company_name: str = "Unknown"
    ) -> SalesBrief:

        prompt = SALES_BRIEF_PROMPT.format(
            content=company_content[:10000]
        )

        response = self.gemini.generate_sales_brief(prompt)

        default_questions = [
            "How do you currently acquire new customers?",
            "What are your biggest business challenges?",
            "Do you use any CRM or sales tools?"
        ]

        if "sales_questions" not in response:
            response["sales_questions"] = default_questions

        elif len(response["sales_questions"]) < 3:

            missing = 3 - len(response["sales_questions"])

            response["sales_questions"].extend(
                default_questions[:missing]
            )

        # Always use the actual company name from CSV
        response["company_name"] = company_name

        return SalesBrief(**response)