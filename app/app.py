import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from city_loader import CityLoader
from update_service import WeatherUpdateService
from sleep_timer import SleepTimer
from repository.weather import WeatherRepository


def main():
    """
    Função principal que orquestra a execução do aplicativo.

    Inicializa todos os serviços necessários, carrega a lista de cidades e
    inicia um loop infinito para buscar e atualizar as temperaturas em
    intervalos de tempo definidos. O loop pode ser interrompido com Ctrl+C.
    """
    loader = CityLoader()
    repo = WeatherRepository()
    updater = WeatherUpdateService(repo)
    sleeper = SleepTimer()

    cities = loader.load()

    if not cities:
        print("Nenhuma cidade para processar. Finalizando.")
        return

    print(f"Cidades a serem processadas: {[c['nome'] for c in cities]}")

    try:
        while True:
            updater.update_cities(cities)
            sleeper.wait_minutes(100)
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário, finalizando.")


if __name__ == "__main__":
    main()
