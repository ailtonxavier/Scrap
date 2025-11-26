from typing import Optional
from scrapper.fetcher import HtmlFetcher
from scrapper.temperature_parser import TemperatureParser


class TemperatureService:
    """
    Serviço para obter a temperatura a partir de uma URL.

    Esta classe coordena a busca do conteúdo HTML de uma página (fetch) e a
    extração (parse) da informação de temperatura a partir desse HTML.
    """

    def __init__(self, fetcher: HtmlFetcher, parser: TemperatureParser):
        """
        Inicializa o serviço de temperatura.

        Args:
            fetcher (HtmlFetcher): Uma instância de um buscador de HTML.
            parser (TemperatureParser): Uma instância de um parser de temperatura.
        """
        self.fetcher = fetcher
        self.parser = parser

    def get_temperature(self, url: str, headers: dict) -> Optional[str]:
        """
        Busca o HTML de uma URL e extrai a temperatura.

        Args:
            url (str): A URL da página web de onde a temperatura será extraída.
            headers (dict): Cabeçalhos HTTP a serem usados na requisição.

        Returns:
            Optional[str]: A temperatura extraída como uma string, ou None se
                           a página não puder ser buscada ou a temperatura
                           não for encontrada.
        """
        html = self.fetcher.fetch(url, headers)
        if not html:
            return None
        return self.parser.parse(html)
