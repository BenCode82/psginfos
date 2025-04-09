from .models import Article
import feedparser
from datetime import datetime

import requests
from bs4 import BeautifulSoup

FEEDS = [
    ("Parisfans", "https://www.parisfans.fr/feed"),
    ("Le Parisien - PSG", "https://www.leparisien.fr/sports/football/psg/rss.xml"),
]

NEWS_API_KEY = "662d1a968fd44a19a6c12e2083278c62"
NEWS_API_URL = "https://newsapi.org/v2/everything"


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

def fetch_from_apis():
    article_api_count = 0

    params = {
        'q': 'PSG',
        'language': 'fr',
        'apiKey': NEWS_API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    for article in data.get('articles', [])[:10]:
        titre = article['title']
        lien = article['url']
        date_pub = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        source = article['source']['name']
        image_url = article['urlToImage']

        if not Article.objects.filter(lien=lien).exists():
            article_api_count += 1
            Article.objects.create(
                titre=titre,
                lien=lien,
                source=source,
                date_pub=date_pub,
                image_url=image_url or ''
            )
    return article_api_count

def fetch_from_rss():
    article_rrs_count = 0

    for source_name, url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            img_url = get_image_from_entry(entry)

            if not Article.objects.filter(lien=entry.link).exists():
                article_rrs_count += 1
                Article.objects.create(
                    titre=entry.title,
                    lien=entry.link,
                    source=source_name,
                    date_pub=datetime(*entry.published_parsed[:6]) if hasattr(entry, "published_parsed") else datetime.now(),
                    image_url=img_url
                )
    return article_rrs_count

def fetch_articles():
    article_add_count = 0
    article_add_count += fetch_from_apis()
    article_add_count += fetch_from_rss()

    # Supprimer des articles pour garder seulement les 40 plus récents (par id)
    max_articles = 40
    articles_total = Article.objects.count()

    if articles_total > max_articles:
    # Récupère les articles à supprimer (du plus ancien au plus récent)
        articles_a_supprimer = Article.objects.order_by('id')[:articles_total - max_articles]

        # Suppression un par un
        for article in articles_a_supprimer:
            article.delete()

    return article_add_count

def delete_all_articles():
    articles = Article.objects.all()
    total = len(articles)

    if total == 0:
        return 0

    for article in articles:
        article.delete()
    return total
