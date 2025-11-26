import os


class RedisConfig:
    @staticmethod
    def get_host() -> str:
        return os.getenv("REDIS_HOST", "localhost")

    @staticmethod
    def get_port() -> int:
        return int(os.getenv("REDIS_PORT", "6379"))
