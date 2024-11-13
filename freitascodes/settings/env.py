from freitascodes.settings.base import *
from dotenv import load_dotenv
import os

DEBUG = True

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

ICONS_URL = 'https://skillicons.dev/icons?i='

SECRET_KEY = '^$z(ny5hhd4k119hv)jbop0_rrv$swnkk&9)ja)1j36)pysu)i'

ALLOWED_HOSTS = ['0.0.0.0','portifolio.freitascodes.me']

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