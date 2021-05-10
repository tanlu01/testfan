import redis


class RedisMixin:
    def rd(self):
        pool = redis.ConnectionPool(**self.redis_connect)
        return redis.Redis(connection_pool=pool)
