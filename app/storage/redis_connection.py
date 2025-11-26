import redis
from storage.redis_config import RedisConfig
from singleton import Singleton


class RedisConnection(metaclass=Singleton):
    """
    Gerencia a conexão com o banco de dados Redis.

    Esta classe utiliza o padrão Singleton para garantir que exista apenas uma
    instância de conexão em toda a aplicação. Ela busca as configurações de
    host e porta da classe `RedisConfig`.
    """

    def __init__(self):
        """
        Inicializa a conexão com o Redis.

        Cria uma instância do cliente Redis usando as configurações fornecidas
        por `RedisConfig`. `decode_responses=True` garante que as respostas
        do Redis sejam decodificadas de bytes para strings UTF-8.
        """
        self.client = redis.Redis(
            host=RedisConfig.get_host(),
            port=RedisConfig.get_port(),
            decode_responses=True
        )

    def get_client(self):
        """
        Retorna a instância do cliente Redis conectado.

        Returns:
            redis.Redis: A instância do cliente.
        """
        return self.client
