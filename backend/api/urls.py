from django.urls import path
from .views import ArticleListCreateAPI

urlpatterns = [
    path('api/articles/', ArticleListCreateAPI.as_view(), name='article-api'),
]
