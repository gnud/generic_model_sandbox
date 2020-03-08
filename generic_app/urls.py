"""generic_model_sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from generic_app import api

router_v1 = routers.DefaultRouter('app_v1')
router_v1.register(prefix=r'comment', viewset=api.CommentsViewSet, basename='app_v1-comment')
router_v1.register(prefix=r'comment2', viewset=api.CommentsNormalViewSet, basename='app_v1-comment-normal')

urlpatterns = [
    path('api/app/v1/', include(router_v1.urls)),
]
