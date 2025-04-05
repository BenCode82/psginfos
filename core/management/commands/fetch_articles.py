from django.core.management.base import BaseCommand
from core.rss_feeds import fetch_articles  # On appelle ta fonction

class Command(BaseCommand):
    help = "Récupère les derniers articles via RSS"

    def handle(self, *args, **kwargs):
        fetch_articles()
        self.stdout.write(self.style.SUCCESS("✅ Articles récupérés avec succès"))
