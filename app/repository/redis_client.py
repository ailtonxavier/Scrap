

class RedisClient:
    """
    Cliente para interagir com o Redis.

    Esta classe atua como um wrapper para a instância do cliente Redis,
    abstraindo a forma como a conexão é obtida.
    """

    def __init__(self):
        """
        Inicializa o RedisClient.

        Obtém a instância da conexão do Redis através da função `get_redis()`.
        """
        self._client = get_redis()

    def client(self):
        """
        Retorna a instância do cliente Redis gerenciada.

        Returns:
            Redis: A instância do cliente para interagir com o Redis.
        """
        return self._client
