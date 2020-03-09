from django.db import models


class CommentQSManager(models.query.QuerySet):
    from generic_app import models as gmodels

    def create_comment_article(self, data: dict):
        article = self.gmodels.Article.objects.create(**data)
        self.model.objects.create(content_object=article, comm='df')

    def create_comment_post(self, data: dict):
        post = self.gmodels.Post.objects.create(**data)
        self.model.objects.create(content_object=post, comm='df')


class CommentNormalQSManager(models.query.QuerySet):
    def create_comment_article(self):
        pass

    def create_comment_post(self):
        pass
