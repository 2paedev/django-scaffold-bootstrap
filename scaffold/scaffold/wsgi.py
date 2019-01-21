import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scaffold.settings')

APPLICATION = get_wsgi_application()
