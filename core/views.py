from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreateAPI(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
