class FnsMixin:
    """
    Common functions for serializers
    """

    @staticmethod
    def by_type_content(obj):
        """
        Note: cons of this approach is somehow if we set both article and post

        :type obj: generic_app.models.CommentNormal
        :rtype: Union[generic_app.models.Article, generic_app.models.Post]
        """

        from generic_app import serializers as app_ser
        if obj.post:
            ser = app_ser.PostSerializer(instance=obj.post)
            return ser.data

        if obj.article:
            ser = app_ser.ArticleSerializer(instance=obj.article)
            return ser.data
