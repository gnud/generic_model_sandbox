from rest_framework import viewsets, permissions
from generic_app import models
from generic_app import serializers


class CommentsViewSet(viewsets.ModelViewSet):
    default_queryset = models.Comment.objects.all()
    queryset = default_queryset
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CommentSerializer


class CommentsNormalViewSet(viewsets.ModelViewSet):
    default_queryset = models.CommentNormal.objects.all()
    queryset = default_queryset
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CommentNormalSerializer
