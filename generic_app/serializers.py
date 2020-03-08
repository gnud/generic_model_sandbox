from rest_framework import serializers
from generic_app import models
from generic_app import serializer_fields
from generic_app import serializer_methods as fn_mixin


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = [
            'pk',
            'content'
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            'pk',
            'content'
        ]


class CommentSerializer(serializers.ModelSerializer):
    content = serializer_fields.CommentContentObjectRelatedField(source='content_object', read_only=True)

    class Meta:
        model = models.Comment
        fields = [
            'pk',
            'content'
        ]


class CommentNormalSerializer(fn_mixin.FnsMixin, serializers.ModelSerializer):
    content = serializers.SerializerMethodField('by_type_content')

    class Meta:
        model = models.CommentNormal
        fields = [
            'pk',
            'content'
        ]
