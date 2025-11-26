class RedisClient:
    def __init__(self):
        self._client = get_redis()

    def client(self):
        return self._client
