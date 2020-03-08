from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from generic_app import managers


class Comment(models.Model):
    comm = models.CharField(max_length=50)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id', )
    objects = managers.CommentQSManager.as_manager()

    def __str__(self):
        content = self.content_object and self.content_object.content.title() or 'n/a'
        return f"{content}"


class Article(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)


class Post(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)
