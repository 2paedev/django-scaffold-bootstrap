# pylint: disable=W0614,W0401
from scaffold.settings.base import *


ALLOWED_HOSTS = [
    # "<url_backend_dev_server>",
    "localhost", 
    "127.0.0.1"
]
# BASE_URL = "<url_backend_dev_server>"

PROD = False
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    # "<url_frontend_dev_server>"",
)

DATABASES = set_database_config()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ' [%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
        },
        'simple': {
            'format': ' %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': join('/var/log/app-logs/messages.log')
        },
        'file_errors': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': join('/var/log/app-logs/errors.log')
        },
    },
    'loggers': {
        'main': {
            'handlers': ['console', 'file', 'file_errors'],
            'level': 'DEBUG'
        }
    }
}
