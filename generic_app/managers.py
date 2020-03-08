from django.db import models


class CommentQSManager(models.query.QuerySet):
    def create_comment_article(self):
        pass

    def create_comment_post(self):
        pass
