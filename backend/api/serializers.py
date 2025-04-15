from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['titre', 'lien', 'source', 'image_url', 'date_pub', 'hashtags']  # Champs à exposer
