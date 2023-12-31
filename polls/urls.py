# 创建路由，需要将我们的视图做一个映射
from django.urls import path

from . import views

app_name = "polls"   # 给url么一个命名空间
urlpatterns = [
    path("", views.index, name='index'),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]