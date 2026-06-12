import re
import time
from urllib.parse import urlparse, unquote, parse_qs

import requests
from bs4 import BeautifulSoup


class URLResolver:

    DIRECTORY_DOMAINS = {
        "facebook.com",
        "linkedin.com",
        "instagram.com",
        "twitter.com",
        "x.com",
        "wikipedia.org",
        "yelp.com",
        "yellowpages.com",
        "justdial.com",
        "glassdoor.com",
        "indeed.com",
        "crunchbase.com",
        "zoominfo.com",
        "rocketreach.co",
        "tracxn.com",
        "owler.com",
    }

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        )
    }

    TIMEOUT = 10

    def resolve(self, input_value: str) -> dict:

        input_value = input_value.strip()

        # Strategy 1: Direct URL
        if self._is_url(input_value):

            url = input_value

            if not url.startswith(("http://", "https://")):
                url = f"https://{url}"

            return {
                "success": True,
                "url": url,
                "resolution_method": "direct_url",
            }

        # Strategy 2: DuckDuckGo Search
        url = self._search_duckduckgo(input_value)

        if url:
            return {
                "success": True,
                "url": url,
                "resolution_method": "duckduckgo",
            }

        # Strategy 3: Google Search
        url = self._search_google(input_value)

        if url:
            return {
                "success": True,
                "url": url,
                "resolution_method": "google",
            }

        # Strategy 4: Domain Guessing
        url = self._guess_domain(input_value)

        if url:
            return {
                "success": True,
                "url": url,
                "resolution_method": "domain_guess",
            }

        return {
            "success": False,
            "error": "Could not resolve company website",
        }

    def _search_duckduckgo(self, company_name: str):

        queries = [
            company_name,
            f"{company_name} company",
            f"{company_name} business",
            f"{company_name} official website",
        ]

        for query in queries:

            try:

                time.sleep(1)

                response = requests.get(
                    "https://html.duckduckgo.com/html/",
                    params={"q": query},
                    headers=self.HEADERS,
                    timeout=self.TIMEOUT,
                )

                response.raise_for_status()

                soup = BeautifulSoup(
                    response.text,
                    "html.parser"
                )

                candidates = []

                for result in soup.select(".result"):

                    title_el = result.select_one(
                        ".result__title a"
                    )

                    if not title_el:
                        continue

                    href = title_el.get(
                        "href",
                        ""
                    )

                    if "uddg=" in href:

                        try:

                            qs = parse_qs(
                                urlparse(href).query
                            )

                            href = unquote(
                                qs.get(
                                    "uddg",
                                    [""]
                                )[0]
                            )

                        except Exception:
                            continue

                    if not href.startswith("http"):
                        continue

                    if self._is_directory(
                        href
                    ):
                        continue

                    candidates.append(href)

                for candidate in candidates[:5]:

                    if self._verify_candidate(
                        candidate,
                        company_name
                    ):
                        return candidate

            except Exception:
                continue

        return None

    def _verify_candidate(
        self,
        url: str,
        company_name: str
    ):

        try:

            response = requests.get(
                url,
                headers=self.HEADERS,
                timeout=5,
            )

            soup = BeautifulSoup(response.text, "html.parser")

            text = (
                soup.title.get_text(" ", strip=True)
                if soup.title else ""
            )

            text += " " + soup.get_text(" ", strip=True)[:3000]
            text = text.lower()

            company_words = [
                word.lower()
                for word in company_name.split()
                if len(word) > 2
            ]

            matches = sum(
                1
                for word in company_words
                if word in text
            )

            return matches >= max(
                1,
                len(company_words) // 2
            )

        except Exception:

            return False

    def _search_google(self, company_name: str):

        try:

            time.sleep(2)

            response = requests.get(
                "https://www.google.com/search",
                params={
                    "q": f"{company_name} official website",
                    "num": 10,
                },
                headers=self.HEADERS,
                timeout=self.TIMEOUT,
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            candidates = []

            for link in soup.select(
                "div.g a[href]"
            ):

                href = link.get(
                    "href",
                    ""
                )

                if href.startswith(
                    "/url?q="
                ):

                    href = unquote(
                        href[7:].split("&")[0]
                    )

                if not href.startswith(
                    "http"
                ):
                    continue

                if self._is_directory(
                    href
                ):
                    continue

                candidates.append(
                    href
                )

            for candidate in candidates[:5]:

                if self._verify_candidate(
                    candidate,
                    company_name
                ):
                    return candidate

            return None

        except Exception:

            return None

    def _guess_domain(
        self,
        company_name: str
    ):

        clean = re.sub(
            r"[^a-z0-9\s]",
            "",
            company_name.lower()
        )

        words = clean.split()

        candidates = [
            "".join(words) + ".com",
            "-".join(words) + ".com",
             "".join(words) + ".net",
            "".join(words) + ".org",
            "".join(words) + ".biz",
        ]

        for domain in candidates:

            url = f"https://www.{domain}"

            try:

                response = requests.head(
                    url,
                    timeout=5,
                    allow_redirects=True,
                )

                if response.status_code < 400:

                    return url

            except Exception:

                continue

        return None

    def _is_directory(
        self,
        url: str
    ):

        domain = (
            urlparse(url)
            .netloc
            .replace(
                "www.",
                ""
            )
            .lower()
        )

        return any(
            directory in domain
            for directory
            in self.DIRECTORY_DOMAINS
        )

    @staticmethod
    def _is_url(
        value: str
    ):

        return bool(
            re.match(
                r"^(https?://|www\.)",
                value,
                re.IGNORECASE,
            )
        )