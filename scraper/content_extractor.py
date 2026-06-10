from bs4 import BeautifulSoup


class ContentExtractor:
    def extract_text(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text