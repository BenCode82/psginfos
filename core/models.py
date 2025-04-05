from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=255)
    lien = models.URLField(unique=True)
    description = models.TextField(blank=True)
    date_pub = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titre
