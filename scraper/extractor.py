from bs4 import BeautifulSoup
from scraper.config import ERROR_CODES

class ContentExtractor:
    REMOVE_TAGS=["script","style","nav","footer","header"]

    def extract(self,html):
        try:
            soup=BeautifulSoup(html,"html.parser")
            for tag in self.REMOVE_TAGS:
                for e in soup.find_all(tag):
                    e.decompose()
            title=soup.title.get_text(strip=True) if soup.title else "Unknown"
            text=soup.get_text(" ",strip=True)
            if len(text.split())<20:
                return {"success":False,"error":ERROR_CODES["empty_content"]}
            return {"success":True,"title":title,"content":text}
        except Exception as e:
            return {"success":False,"error":str(e)}