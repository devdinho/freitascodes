from freitascodes.settings.base import *
from dotenv import load_dotenv
import os

SITE_ID = 1

load_dotenv(override=True)

DEBUG = os.getenv('DEBUG')

print(f"Debug: {DEBUG}")

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['0.0.0.0',os.getenv('VM_IP'),'portifolio.freitascodes.me']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': DB_NAME,
    'USER': DB_USER,
    'PASSWORD': DB_PASSWORD,
    'HOST': DB_HOST,
    'PORT': '5432',
  }
}