# pylint: disable=W0614,W0401
from scaffold.settings.base import *
from scaffold.settings.dev import LOGGING

ALLOWED_HOSTS = [
    # "<url_backend_pre_server"
]
# BASE_URL = "<url_backend_pre_server>"

PROD = False
DEBUG = False

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    # "<url_frontend_pre_server>",
)

DATABASES = set_database_config()

LOGGING = LOGGING
