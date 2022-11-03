import os

DATABASES = {
    "default": {
        "ENGINE": "django_prometheus.db.backends.postgresql",
        "NAME": os.getenv("SKELENGO_DB_NAME", "test"),
        "USER": os.getenv("SKELENGO_DB_USER", "test"),
        "PASSWORD": os.getenv("SKELENGO_DB_PASSWORD", "test"),
        "HOST": os.getenv("SKELENGO_DB_HOST", "localhost"),
        "PORT": os.getenv("SKELENGO_DB_PORT", "5432"),
    }
}
