from .base import *
from decouple import config

SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("POSTGRES_DB", cast=str),
        'USER': config("POSTGRES_USER", cast=str),
        'PASSWORD': config("POSTGRES_PASSWORD", cast=str),
        'HOST': config("POSTGRES_HOST", cast=str),
        'PORT': config("POSTGRES_PORT", cast=int),
    }
}