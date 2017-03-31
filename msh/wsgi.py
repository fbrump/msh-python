# -*- coding: utf-8 -*-
# msh-python/msh/swgi.py
"""
WSGI config for msh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msh.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
