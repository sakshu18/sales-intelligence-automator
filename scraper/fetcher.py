
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from scraper.config import HEADERS,TIMEOUT,ERROR_CODES

class Fetcher:
    def __init__(self):
        self.session=requests.Session()
        self.session.headers.update(HEADERS)
        retries=Retry(total=3, backoff_factor=1,status_forcelist=[429,500,502,503,504])
        adapter=HTTPAdapter(max_retries=retries)
        self.session.mount("http://",adapter)
        self.session.mount("https://",adapter)
        self.last_error=None

    def fetch(self,url):
        try:
            r=self.session.get(url,timeout=TIMEOUT)
            if r.status_code==403:
                self.last_error=ERROR_CODES["http_403"]; return None
            if r.status_code==404:
                self.last_error=ERROR_CODES["http_404"]; return None
            if "text/html" not in r.headers.get("Content-Type",""):
                self.last_error=ERROR_CODES["invalid_content"]; return None
            return r.text
        except requests.Timeout:
            self.last_error=ERROR_CODES["timeout"]
        except requests.RequestException:
            self.last_error=ERROR_CODES["connection_error"]
        return None
