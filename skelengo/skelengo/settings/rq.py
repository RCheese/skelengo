from .redis import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

RQ_QUEUES = {
    "default": {
        "HOST": REDIS_HOST,
        "PORT": REDIS_PORT,
        "DB": 0,
        "PASSWORD": REDIS_PASSWORD,
        "DEFAULT_TIMEOUT": 360,
    },
    # "with-sentinel": {
    #     "SENTINELS": [("localhost", 26736), ("localhost", 26737)],
    #     "MASTER_NAME": "redismaster",
    #     "DB": 0,
    #     "PASSWORD": "secret",
    #     "SOCKET_TIMEOUT": None,
    #     "CONNECTION_KWARGS": {"socket_connect_timeout": 0.3},
    # },
    # "high": {
    #     "URL": os.getenv("REDISTOGO_URL", "redis://localhost:6379/0"),  # If you're on Heroku
    #     "DEFAULT_TIMEOUT": 500,
    # },
    # "low": {
    #     "HOST": "localhost",
    #     "PORT": 6379,
    #     "DB": 0,
    # },
}

# RQ_EXCEPTION_HANDLERS = ["path.to.my.handler"]  # If you need custom exception handlers
