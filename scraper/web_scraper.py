import time
from scraper.url_resolver import URLResolver
from scraper.fetcher import Fetcher
from scraper.extractor import ContentExtractor
from scraper.cleaner import ContentCleaner
from scraper.config import RATE_LIMIT_SECONDS

class WebScraper:
    def __init__(self):
        self.resolver=URLResolver()
        self.fetcher=Fetcher()
        self.extractor=ContentExtractor()
        self.cleaner=ContentCleaner()

    def scrape(self,input_value):
        resolved=self.resolver.resolve(input_value)
        if not resolved["success"]:
            return {"status":"failed","error":resolved["error"]}

        html=self.fetcher.fetch(resolved["url"])
        if not html:
            return {"status":"failed","error":self.fetcher.last_error}

        extracted=self.extractor.extract(html)
        if not extracted["success"]:
            return {"status":"failed","error":extracted["error"]}

        content=self.cleaner.clean(extracted["content"])
        time.sleep(RATE_LIMIT_SECONDS)

        return {
            "status":"success",
            "url":resolved["url"],
            "title":extracted["title"],
            "word_count":len(content.split()),
            "content":content[:1000]
        }
