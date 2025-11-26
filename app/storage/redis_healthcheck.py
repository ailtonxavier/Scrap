from typing import Optional
from .redis_connection import RedisConnection


class RedisHealthCheck:
    """Serviço para verificar a saúde (health check) da conexão com o Redis."""

    def __init__(self, connection: RedisConnection):
        """
        Inicializa o health check.

        Args:
            connection (RedisConnection): A instância do gerenciador de conexão com o Redis.
        """
        self.connection = connection

    def ping(self) -> bool:
        """
        Executa um comando PING no servidor Redis para verificar a conexão.

        Returns:
            bool: True se o servidor responder ao PING com sucesso, False caso contrário.
        """
        try:
            client = self.connection.get_client()
            return client.ping()
        except Exception:
            return False
