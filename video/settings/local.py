from .base import *
from decouple import config

SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config("MYSQL_DATABASE", cast=str),
        'USER': config("MYSQL_ROOT_USER", cast=str),
        'PASSWORD': config("MYSQL_ROOT_PASSWORD", cast=str),
        'HOST': config("MYSQL_DATABASE_HOST", cast=str),
        'PORT': config("MYSQL_DATABASE_PORT", cast=int),
    }
}