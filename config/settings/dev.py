import environ 
from .base import *

env=environ.Env()

environ.Env.read_env(str(BASE_DIR / '.env'))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str('db_name'),
        "USER": env.str('db_user'),
        "PASSWORD": env.str('db_pwd'),
        "HOST": env.str('db_host'),
        "PORT": env.str('db_port'),
    }
}