from .base import *
import environ

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
DATABASES = {'default': env.db()}
