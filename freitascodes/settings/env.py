from freitascodes.settings.base import *
from dotenv import load_dotenv
import os

SITE_ID = 1

load_dotenv()


DEBUG = eval(os.getenv('DEBUG'))
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')


print(f"Debug: {DEBUG}")

SECRET_KEY = '^$z(ny5hhd4k119hv)jbop0_rrv$swnkk&9)ja)1j36)pysu)i'

ALLOWED_HOSTS = ['0.0.0.0','34.133.103.79','portifolio.freitascodes.me']

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