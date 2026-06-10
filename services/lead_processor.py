from scraper.web_scraper import WebScraper
from scraper.content_extractor import ContentExtractor
from scraper.content_cleaner import ContentCleaner

from services.company_resolver import CompanyResolver
from ai.analyzer import LeadAnalyzer

import pandas as pd


class LeadProcessor:

    def __init__(self):
        self.scraper = WebScraper()
        self.extractor = ContentExtractor()
        self.cleaner = ContentCleaner()
        self.analyzer = LeadAnalyzer()
        self.resolver = CompanyResolver()

    def process(self,
                company_name: str = None,
                website_url: str = None,
                location: str = None):

        if pd.isna(website_url) or not website_url:
            return {
                "company_name": company_name,
                "status": "Skipped",
                "reason": "No website URL provided"
            }

        try:
            html = self.scraper.fetch_page(website_url)

            content = self.extractor.extract_text(html)

            cleaned_content = self.cleaner.clean(content)

            sales_brief = self.analyzer.analyze(
                cleaned_content,
                company_name
            )

            if hasattr(sales_brief, "model_dump"):
                return sales_brief.model_dump()

            return sales_brief

        except Exception as e:
            return {
                "company_name": company_name,
                "website_url": website_url,
                "status": "Failed",
                "error": str(e)
            }