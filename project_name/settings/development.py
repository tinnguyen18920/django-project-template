from project_name.settings.base import *

SECRET_KEY = "123456"
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': env.db(default='sqlite:///db.sqlite3')
}