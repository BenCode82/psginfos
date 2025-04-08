🚀 Déploiement automatique sur AlwaysData via Git
📌 Étape 1 : Ajouter le remote alwaysdata
Pour que la commande git push alwaysdata main fonctionne, ton dépôt Git local doit connaître le serveur distant nommé alwaysdata.

🔍 Vérifier si le remote existe
bash
Copier
Modifier
git remote -v
Tu devrais voir quelque chose comme :

perl
Copier
Modifier
alwaysdata    ssh://ton_user@git.alwaysdata.com/psg_api.git (fetch)
alwaysdata    ssh://ton_user@git.alwaysdata.com/psg_api.git (push)
✅ Ajouter le remote si besoin
bash
Copier
Modifier
git remote add alwaysdata ssh://ton_user@git.alwaysdata.com/psg_api.git
Remplace ton_user par ton identifiant AlwaysData et psg_api par le nom de ton dépôt.

⚙️ Étape 2 : Créer un script de déploiement automatisé
Puisqu’il n’y a pas de hook post-receive par défaut sur AlwaysData, on crée un script personnalisé, déclenché manuellement après le git push.

📁 Fichier deploy.sh à placer dans le dossier du projet :
bash
Copier
Modifier
#!/bin/bash

echo "🚀 Déploiement en cours..."

# Aller dans le dossier de l'appli
cd ~/www/

# Activer l’environnement virtuel
source ~/env/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate --noinput

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Redémarrer l’application (forcer uWSGI à recharger)
touch ~/www/psg_api/wsgi.py

echo "✅ Déploiement terminé !"
🔒 Le rendre exécutable :
bash
chmod +x deploy.sh
🚀 Étape 3 : Déploiement
À chaque fois que tu veux mettre à jour le serveur :

bash

git push alwaysdata main
ssh ton_user@ssh.alwaysdata.com './deploy.sh'
