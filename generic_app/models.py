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

    def __str__(self):
        return self.content.title() or 'n/a'


class Post(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.content.title() or 'n/a'


class CommentNormal(models.Model):
    article = models.ForeignKey(to='Article', null=True, blank=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(to='Post', null=True, blank=True, on_delete=models.SET_NULL)
    objects = managers.CommentNormalQSManager.as_manager()

    def __str__(self):
        post_content = self.post and self.post.content and self.post.content.title()
        article_content = self.article and self.article.content and self.article.content.title()

        return f'Post:{post_content}|Article:{article_content}'
