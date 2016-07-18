from __future__ import unicode_literals

from django.db import models

from forums.models import Topic

class Question(models.Model):
    pass


# class QuestionChoice(models.Model):
#     pass


class QuestionTopic(models.Model):
    topic = models.ForeignKey(Topic, null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True)
    primary = models.BooleanField(default=False)
