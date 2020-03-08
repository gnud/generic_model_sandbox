from rest_framework import serializers
from generic_app import models


class CommentContentObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `content_object` generic relationship.
    """

    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        from generic_app import serializers as app_ser
        if isinstance(value, models.Post):
            ser = app_ser.PostSerializer(instance=value)
            return ser.data
        elif isinstance(value, models.Article):
            ser = app_ser.ArticleSerializer(instance=value)
            return ser.data
        raise Exception('Unexpected type of tagged object')
