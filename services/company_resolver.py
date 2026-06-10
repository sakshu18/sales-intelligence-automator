import re
from models.lead import Lead


class CompanyResolver:

    def resolve(self, raw_input: str) -> Lead:

        parts = raw_input.split(" - ")

        company_name = parts[0].strip()

        location = parts[1].strip() if len(parts) > 1 else None

        return Lead(
            company_name=company_name,
            location=location
        )