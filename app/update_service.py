from typing import List
from repository.weather import WeatherRepository
from scrapper.temperature_service import TemperatureService  # versão SRP que criamos
from scrapper.fetcher import HtmlFetcher
from scrapper.temperature_parser import TemperatureParser


class WeatherUpdateService:
    """
    Serviço de orquestração para atualização da temperatura das cidades.

    Esta classe coordena o processo de buscar a temperatura de uma lista de
    cidades usando um scraper e, em seguida, salvar essa informação em um
    repositório.
    """

    def __init__(self, repository: WeatherRepository):
        """
        Inicializa o serviço de atualização.

        Args:
            repository (WeatherRepository): A instância do repositório onde os dados
                                           de temperatura serão salvos.
        """
        self.repository = repository
        self.scraper = TemperatureService(HtmlFetcher(), TemperatureParser())

    def update_cities(self, cities: List[dict]):
        """
        Busca e salva a temperatura para uma lista de cidades.

        Itera sobre a lista de cidades, busca a temperatura atual de cada uma
        na web e a salva no repositório.

        Args:
            cities (List[dict]): Uma lista de dicionários, onde cada dicionário
                                 contém o nome e a URL da cidade.
        """
        print("-" * 20)
        for city in cities:
            city_name = city["nome"]
            city_url = city["url"]
            key = f"temperatura:{city_name}"

            print(f"Buscando temperatura para: {city_name}")

            temp = self.scraper.get_temperature(city_url, {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                )
            })

            if temp:
                print(f"Temperatura em {city_name}: {temp}°C")
                try:
                    self.repository.save_temperature(key, temp)
                    print(f"Salvo em Redis: {key} -> {temp}")
                except Exception as e:
                    print(f"Erro ao salvar no repositório: {e}")
            else:
                print(f"Não foi possível obter a temperatura para {city_name}.")
