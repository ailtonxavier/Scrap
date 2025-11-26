from typing import Optional
from scrapper.fetcher import HtmlFetcher
from scrapper.temperature_parser import TemperatureParser


class TemperatureService:
    def __init__(self, fetcher: HtmlFetcher, parser: TemperatureParser):
        self.fetcher = fetcher
        self.parser = parser

    def get_temperature(self, url: str, headers: dict) -> Optional[str]:
        html = self.fetcher.fetch(url, headers)
        if not html:
            return None
        return self.parser.parse(html)
