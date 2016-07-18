from __future__ import unicode_literals

from django.db import models

from forums.models import Template


class Topic(models.Model):
    template = models.ForeignKey(Template, null=True, blank=True, help_text='Topic for specific\
        template')
    channel = models.BooleanField(default=False)
