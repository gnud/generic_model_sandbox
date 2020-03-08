from django.contrib import admin
from django.contrib.contenttypes import admin as ct_admin

from generic_app import models


class CommentInline(ct_admin.GenericTabularInline):
    model = models.Comment
    # extra = 0
    # max_num = 1
    # fields = ['email', 'dob', 'avatar', 'gender', 'phone', 'position']
    # can_delete = False


# Register your models here.
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass
