"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.exceptions import ImproperlyConfigured

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings.development')
if not os.getenv("DJANGO_SETTINGS_MODULE"):
    raise ImproperlyConfigured("Must set DJANGO_SETTINGS_MODULE varible in Environment")

application = get_wsgi_application()
