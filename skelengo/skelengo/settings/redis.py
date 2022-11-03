import os

REDIS_HOST = os.environ.get("SKELENGO_REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("SKELENGO_REDIS_PORT", 6379)
REDIS_PASSWORD = os.environ.get("SKELENGO_REDIS_PASSWORD")

REDIS_CACHE_LOCATION = f"redis://{REDIS_HOST}:{REDIS_PORT}"

CACHES = {
    "default": {
        "BACKEND": "django_prometheus.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_CACHE_LOCATION,
        "OPTIONS": {
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "CONNECTION_POOL_CLASS": "redis.BlockingConnectionPool",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWORD,
        },
    }
}
