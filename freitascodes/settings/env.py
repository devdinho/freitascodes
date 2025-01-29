from freitascodes.settings.base import *
from dotenv import load_dotenv
import os

SITE_ID = 1

load_dotenv(override=True)

DEBUG = os.getenv('DEBUG')

print(f"Debug: {DEBUG}")

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['0.0.0.0',os.getenv('VM_IP'),'portifolio.dinho.dev']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': POSTGRES_DB,
    'USER': POSTGRES_USER,
    'PASSWORD': POSTGRES_PASSWORD,
    'HOST': DB_HOST,
    'PORT': '5432',
  }
}