import os


class RedisConfig:
    """
    Classe de configuração para os parâmetros de conexão do Redis.

    Fornece métodos estáticos para obter o host e a porta do Redis a partir
    de variáveis de ambiente, com valores padrão de fallback.
    """

    @staticmethod
    def get_host() -> str:
        """
        Obtém o host do Redis a partir da variável de ambiente 'REDIS_HOST'.

        Returns:
            str: O host do Redis. Retorna "localhost" se a variável de ambiente
                 não estiver definida.
        """
        return os.getenv("REDIS_HOST", "localhost")

    @staticmethod
    def get_port() -> int:
        """
        Obtém a porta do Redis a partir da variável de ambiente 'REDIS_PORT'.

        Returns:
            int: A porta do Redis. Retorna 6379 se a variável de ambiente
                 não estiver definida.
        """
        return int(os.getenv("REDIS_PORT", "6379"))
