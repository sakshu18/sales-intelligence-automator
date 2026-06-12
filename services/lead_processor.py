from scraper.web_scraper import WebScraper
from services.company_resolver import CompanyResolver
from ai.analyzer import LeadAnalyzer

import pandas as pd


class LeadProcessor:

    def __init__(self):
        self.scraper = WebScraper()
        self.analyzer = LeadAnalyzer()
        self.resolver = CompanyResolver()

    def process(
        self,
        company_name: str = None,
        website_url: str = None,
        location: str = None
    ):
        to_process = website_url
        if pd.isna(website_url) or not website_url:
            to_process = company_name

        try:

            processed_content = self.scraper.scrape(
                to_process
            )
            if processed_content['status'] == 'success':
                sales_brief = self.analyzer.analyze(
                    processed_content['content'],
                    company_name
                )

                if hasattr(
                    sales_brief,
                    "model_dump"
                ):

                    result = sales_brief.model_dump()

                else:

                    result = sales_brief

                # Add URL for UI display
                result["website_url"] = processed_content['url']
            else:
                result = {
                    "company_name": company_name,
                    "website_url": website_url,
                    "status": processed_content['status'],
                    "error": processed_content['error']
                }
            return result

        except Exception as e:

            return {
                "company_name": company_name,
                "website_url": website_url,
                "status": "Failed",
                "error": str(e)
            }