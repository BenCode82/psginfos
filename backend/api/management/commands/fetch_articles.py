from django.core.management.base import BaseCommand
from api.rss_feeds import fetch_articles  # On appelle ta fonction

class Command(BaseCommand):
    help = "Récupère les derniers articles via RSS/API"

    def handle(self, *args, **kwargs):
        article_add_count = fetch_articles()
        self.stdout.write(self.style.SUCCESS(f"{article_add_count} Articles récupérés avec succès ✅"))
