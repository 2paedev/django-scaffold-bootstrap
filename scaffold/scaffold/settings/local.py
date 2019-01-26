# pylint: disable=W0614,W0401
from scaffold.settings.base import *


ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
BASE_URL = 'http://localhost:8000'

PROD = False
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

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
            'filename': join(BASE_DIR, 'log', 'messages.log')
        },
        'file_errors': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': join(BASE_DIR, 'log', 'errors.log')
        },
    },
    'loggers': {
        'main': {
            'handlers': ['console', 'file', 'file_errors'],
            'level': 'DEBUG'
        }
    }
}
