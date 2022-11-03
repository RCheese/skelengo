import os

DEBUG = os.environ.get("DJANGO_DEBUG", "FALSE").strip().upper() == "TRUE"
SITE_ID = 1
ROOT_URLCONF = "skelengo.urls"
DATA_UPLOAD_MAX_MEMORY_SIZE = 33554432  # 32MB
