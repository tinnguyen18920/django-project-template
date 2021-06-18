from {{ project_name }}.settings.base import *
from {{ project_name }}.settings.staging import *


SECRET_KEY = env("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = []
DATABASES = {
    'default': env.db()
}