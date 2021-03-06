from __future__ import absolute_import, unicode_literals

import os
import sys

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

from django.conf import settings  # noqa

app = Celery()

# Using a string here means the worker does not have to serialize
# the configuration object.
app.config_from_object('django.conf:settings')

sys.path.append(os.path.join(settings.BASE_DIR, 'src/django/apps'))
# load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
