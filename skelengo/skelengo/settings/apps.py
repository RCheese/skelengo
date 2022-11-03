def local_package_comp(name: str) -> str:
    return __package__.replace("skelengo.settings", name)


INSTALLED_APPS = [
    "constance",
    "constance.backends.database",
    "grappelli",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # DRF
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    # RQ
    "django_rq",
    # CODE
    local_package_comp("probes"),
    local_package_comp("sea"),
    # DB
    "django_prometheus",
    # 3rd party
    "auditlog",
    "taggit",
    "storages",
    "tinymce",
    "drf_spectacular",
]

from .vars import DEBUG

if DEBUG:
    INSTALLED_APPS += ["silk"]
    INSTALLED_APPS += ["schema_graph"]
    INSTALLED_APPS += ["debug_toolbar"]
