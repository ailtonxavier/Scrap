from singleton import Singleton
from storage.redis_connection import RedisConnection


class WeatherRepository(metaclass=Singleton):
    def __init__(self):
        self.conn = RedisConnection().get_client()

    def save_temperature(self, key, value):
        self.conn.set(key, value)

    def get_temperature(self, key):
        return self.conn.get(key)
