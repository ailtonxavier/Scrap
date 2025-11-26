import requests
from typing import Optional


class HtmlFetcher:
    """Classe responsável por buscar (fetch) o conteúdo HTML de uma URL."""

    def fetch(self, url: str, headers: dict) -> Optional[str]:
        """
        Realiza uma requisição GET para a URL fornecida e retorna o conteúdo HTML.

        Args:
            url (str): A URL da página a ser buscada.
            headers (dict): Cabeçalhos HTTP a serem enviados com a requisição.

        Returns:
            Optional[str]: O conteúdo da página como uma string de texto,
                           ou None se ocorrer um erro na requisição (ex: timeout,
                           erro de status HTTP, etc.).
        """
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception:
            return None
