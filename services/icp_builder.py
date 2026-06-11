from ai.gemini_client import GeminiClient

class ICPBuilder:

    def __init__(self):
        self.gemini = GeminiClient()

    def generate_icp(self, company_data):

        prompt = f"""
        Analyze this company and generate:

        1. Industry
        2. Company size
        3. Target decision makers
        4. Pain points
        5. Buying signals
        6. ICP qualification score (0-100)

        Company Data:
        {company_data}
        """

        return self.gemini.generate_sales_brief(prompt)