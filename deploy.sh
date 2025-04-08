#!/bin/bash

echo "🚀 Déploiement de l'API PSG en cours..."

# Étape 1 : Activer l’environnement virtuel
source /home/benjaminmontet/env/bin/activate

# Étape 2 : Aller dans le dossier de l'appli
cd /home/benjaminmontet/www/

# Étape 5 : Collecter des nouveaux articles
echo "📁 Collecte des nouveaux articles..."
python manage.py fetch_articles

# Étape 6 : Redémarrer l’application (forcer uWSGI à recharger)
echo "🔁 Redémarrage de l'application Django..."
touch /home/benjaminmontet/www/psg_api/wsgi.py
# gunicorn --config gunicorn.conf.py psg_api.wsgi:application

echo "✅ Déploiement terminé !"


# echo "📦 Installation des dépendances..."
# pip install -r requirements.txt

# # Étape 3 : Appliquer les migrations
# echo "🛠️ Migration de la base de données..."
# python manage.py migrate --noinput

# # Étape 4 : Collecter les fichiers statiques
# echo "📁 Collecte des fichiers statiques..."
# python manage.py collectstatic --noinput
