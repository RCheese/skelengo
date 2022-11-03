from .redis import REDIS_CACHE_LOCATION

CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

if REDIS_CACHE_LOCATION:
    CONSTANCE_DATABASE_CACHE_BACKEND = "default"
