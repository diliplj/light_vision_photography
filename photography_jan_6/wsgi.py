"""
WSGI config for photography_jan_6 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photography_jan_6.settings')
import django
django.setup()

from django.core.management import call_command
application = get_wsgi_application()
