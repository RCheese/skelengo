from .aws import *  # NoQA
from .base import *  # NoQA
from .location import *  # NoQA
from .logging import *  # NoQA
from .policies import *  # NoQA
from .secret import *  # NoQA

MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{MEDIA_LOCATION}/"
STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{STATIC_LOCATION}/"

DEFAULT_FILE_STORAGE = "skelengo.settings.storages.MediaStorage"

MEDIA_FILE_STORAGE = DEFAULT_FILE_STORAGE
STATICFILES_STORAGE = "skelengo.settings.storages.StaticStorage"
PRIVATE_FILE_STORAGE = "skelengo.settings.storages.MediaStorage"
CONTENT_FILE_STORAGE = "skelengo.settings.storages.ContentStorage"
WEB_CONTENT_FILE_STORAGE = "skelengo.settings.storages.WebContentStorage"

from .admin import *  # NoQA
from .apps import *  # NoQA
from .auth import *  # NoQA
from .constance import *  # NoQA
from .constance_config import *  # NoQA
from .db import *  # NoQA
from .localize import *  # NoQA
from .middleware import *  # NoQA
from .redis import *  # NoQA
from .rest import *  # NoQA
from .rq import *  # NoQA
from .silk import *  # NoQA
from .time import *  # NoQA
from .utils import *  # NoQA
from .vars import *  # NoQA
from .wsgi import *  # NoQA

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

HOST = os.environ.get("HOST") or "localhost"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ENV_VAR_PREFIX = "SKELENGO_"

# Clear envs after start
if not DEBUG:
    clear_environment(ENV_VAR_PREFIX)
