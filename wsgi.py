"""
WSGI config for dem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
sys.path.append('conf/')
sys.path.append('devops/fabric/')
sys.path.append('src/django/')

application = get_wsgi_application()
