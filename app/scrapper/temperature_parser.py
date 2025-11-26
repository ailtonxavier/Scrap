#extrai temperatura 

from bs4 import BeautifulSoup
import re
from typing import Optional


class TemperatureParser:
    def parse(self, html: str) -> Optional[str]:
        soup = BeautifulSoup(html, "html.parser")

        temperature_text = None

        # Tentativa principal
        card = soup.find("div", class_="cur-con-weather-card__panel")
        if card:
            temp_el = card.find("div", class_="temp")
            if temp_el and temp_el.text:
                temperature_text = temp_el.text.strip()

        # Fallback
        if not temperature_text:
            generic = soup.find("div", class_="temp")
            if generic and generic.text:
                temperature_text = generic.text.strip()

        # Se achou algo, extrai só os dígitos
        if temperature_text:
            return re.sub(r"\D", "", temperature_text)

        return None
