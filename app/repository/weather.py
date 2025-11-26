from singleton import Singleton
from storage.redis_connection import RedisConnection


class WeatherRepository(metaclass=Singleton):
    """
    Repositório para interagir com o banco de dados Redis para dados de temperatura.

    Esta classe segue o padrão Singleton para garantir uma única conexão
    e instância em toda a aplicação.
    """

    def __init__(self):
        """Inicializa o repositório e obtém um cliente de conexão com o Redis."""
        self.conn = RedisConnection().get_client()

    def save_temperature(self, key, value):
        """
        Salva um valor de temperatura no Redis.

        Args:
            key (str): A chave a ser usada para armazenar o dado (ex: "temperatura:Sao Paulo").
            value (any): O valor da temperatura a ser salvo.
        """
        self.conn.set(key, value)

    def get_temperature(self, key):
        """
        Busca um valor de temperatura no Redis pela chave.

        Args:
            key (str): A chave a ser buscada.

        Returns:
            any: O valor da temperatura associado à chave, ou None se não encontrado.
        """
        return self.conn.get(key)
