from __future__ import unicode_literals

from django.db import models

from forums.models import Issue, Question


class Post(models.Model):
    QUESTION_RESPONSE = 1
    ANSWER = 2
    POST_TYPES = (
        (QUESTION_RESPONSE, "question response"),
        (ANSWER, "answer"),
    )
    issue = models.ForeignKey(Issue, null=True, blank=True)


class QuestionReference(models.Model):
    question = models.ForeignKey(Question)
    post = models.ForeignKey(Post)
