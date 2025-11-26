from bs4 import BeautifulSoup
import re
from typing import Optional


class TemperatureParser:
    """Classe responsável por extrair (parse) a informação de temperatura de um HTML."""

    def parse(self, html: str) -> Optional[str]:
        """
        Analisa o conteúdo HTML para encontrar e extrair a temperatura.

        Tenta encontrar a temperatura usando seletores CSS específicos e, se falhar,
        usa um seletor de fallback mais genérico. Após encontrar o texto da
        temperatura, extrai apenas os dígitos.

        Args:
            html (str): O conteúdo HTML da página como uma string.

        Returns:
            Optional[str]: A temperatura como uma string de dígitos (ex: "25"),
                           ou None se a temperatura não for encontrada no HTML.
        """
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
