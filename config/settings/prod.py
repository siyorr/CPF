# import environ
from .base import *

ALLOWED_HOSTS = ['10.1.10.74', 'cpf.aitft.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

# env = environ.Env()
# environ.Env.read_env(BASE_DIR / '.env')

# DATABASES = {
#     'default': {
#         'ENGINE': 'ibm_db_django',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': '49000',
#     }
# }