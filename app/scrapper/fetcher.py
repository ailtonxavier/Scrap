# baixa html
import requests
from typing import Optional


class HtmlFetcher:
    def fetch(self, url: str, headers: dict) -> Optional[str]:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception:
            return None
