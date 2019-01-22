import os

from django.conf import settings

SQLITE = 'sqlite'
POSTGRESQL = 'postgresql'
NO_DB = 'no_db'

ENGINES = {}
ENGINES[SQLITE] = 'django.db.backends.sqlite3'
ENGINES[POSTGRESQL] = 'django.db.backends.postgresql_psycopg2'


def set_database_config():
    engine = os.getenv('DATABASE_ENGINE', 'sqlite')

    database_config = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
        }
    }

    if engine == NO_DB:
        database_config = {}

    if engine == POSTGRESQL:
        database_config = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.getenv('DATABASE_NAME'),
                'USER': os.getenv('DATABASE_USER'),
                'PASSWORD': os.getenv('DATABASE_PASSWORD'),
                'HOST': os.getenv('DATABASE_HOST'),
                'PORT': os.getenv('DATABASE_PORT'),
            }
        }

    return database_config
