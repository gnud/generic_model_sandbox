from django.contrib import admin
from django.contrib.contenttypes import admin as ct_admin

from generic_app import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CommentNormal)
class CommentNormalAdmin(admin.ModelAdmin):
    pass

