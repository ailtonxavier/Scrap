from typing import Optional
from .redis_connection import RedisConnection


class RedisHealthCheck:
    def __init__(self, connection: RedisConnection):
        self.connection = connection

    def ping(self) -> bool:
        try:
            client = self.connection.create_client()
            return client.ping()
        except Exception:
            return False
