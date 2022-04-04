"""
WSGI config for agenda project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda.settings.base')

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
