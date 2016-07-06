from __future__ import unicode_literals

from django.db import models


class Template(models.Model):
    pass


class Topic(models.Model):
    template = models.ForeignKey(Template, null=True, blank=True, help_text='Topic for specific\
        template')


class Question(models.Model):
    pass


# class QuestionChoice(models.Model):
#     pass


class QuestionTopic(models.Model):
    topic = models.ForeignKey(Topic, null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True)
    primary = models.BooleanField(default=False)


class Issue(models.Model):
    pass


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
