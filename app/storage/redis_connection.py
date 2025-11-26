import redis
from storage.redis_config import RedisConfig
from singleton import Singleton


class RedisConnection(metaclass=Singleton):
    def __init__(self):
        self.client = redis.Redis(
            host=RedisConfig.get_host(),
            port=RedisConfig.get_port(),
            decode_responses=True
        )

    def get_client(self):
        return self.client
