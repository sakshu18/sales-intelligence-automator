import re


class ContentCleaner:

    REMOVE_WORDS = [
        "cookie",
        "privacy policy",
        "all rights reserved",
        "terms of service"
    ]

    def clean(self, text: str) -> str:

        text = text.lower()

        for word in self.REMOVE_WORDS:
            text = text.replace(word, "")

        text = re.sub(r"\s+", " ", text)

        return text.strip()