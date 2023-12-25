# 创建路由，需要将我们的视图做一个映射
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index')
]