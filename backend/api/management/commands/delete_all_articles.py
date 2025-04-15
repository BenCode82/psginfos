from django.core.management.base import BaseCommand
from api.rss_feeds import delete_all_articles

class Command(BaseCommand):
    help = "Supprime tous les articles existants 🗑️"

    def handle(self, *args, **kwargs):
        articles_count = delete_all_articles()

        if articles_count == 0:
            self.stdout.write(self.style.WARNING("Aucun article à supprimer 📭"))
        else:
            self.stdout.write(self.style.SUCCESS(f"{articles_count} article(s) supprimé(s) ✅"))
