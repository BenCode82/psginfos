from .models import Article
import feedparser
from datetime import datetime

import requests
from bs4 import BeautifulSoup


FEEDS = [
    ("Parisfans", "https://www.parisfans.fr/feed"),
    ("Le Parisien - PSG", "https://www.leparisien.fr/sports/football/psg/rss.xml"),
]

def get_image_from_entry(entry):
    if 'media_content' in entry:
        return entry.media_content[0]['url']
    if 'links' in entry:
        for link in entry.links:
            if link.type.startswith('image'):
                return link.href

    # Fallback : scrape la page de l'article pour recuperer l'image
    try:
        response = requests.get(entry.link, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image.get('content'):
            return og_image['content']
    except Exception as e:
        print(f"Erreur lors du scraping de {entry.link} : {e}")

    return ''

def fetch_articles():
    for source_name, url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            img_url = get_image_from_entry(entry)

            if not Article.objects.filter(lien=entry.link).exists():
                Article.objects.create(
                    titre=entry.title,
                    lien=entry.link,
                    source=source_name,
                    date_pub=datetime(*entry.published_parsed[:6]) if hasattr(entry, "published_parsed") else datetime.now(),
                    image_url=img_url
                )

    # Supprimer des articles pour garder seulement les 40 plus récents (par id)
    max_articles = 40
    articles_total = Article.objects.count()

    if articles_total > max_articles:
        # Récupère les articles à supprimer (du plus ancien au plus récent)
        articles_a_supprimer = Article.objects.order_by('id')[:articles_total - max_articles]

        # Suppression un par un (contourne la limitation Django)
        for article in articles_a_supprimer:
            article.delete()
