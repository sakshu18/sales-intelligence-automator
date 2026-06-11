import requests

class WebScraper:
    def fetch_page(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.text
    
    