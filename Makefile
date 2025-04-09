# Makefile pour déployer le projet sur AlwaysData

# Variables de configuration
USER = benjaminmontet
HOST = ssh-benjaminmontet.alwaysdata.net

# Tâche principale : pousser le code vers Alwaysdata + exécution du script "deploy.sh"
deploy:
	@echo "🚀 Pousser le code sur AlwaysData..."
# copier seulement le backend Django du projet
	rsync -av --exclude '.git' --exclude 'venv' --exclude 'frontend' --exclude 'Makefile' . benjaminmontet@ssh-benjaminmontet.alwaysdata.net:/home/benjaminmontet/www/
	@echo "✅ Code poussé avec succès."

# deplacer et lancer "deploy.sh"
	@echo ""
	@echo "🚀 Lancement du script de déploiement à distance..."
	ssh $(USER)@$(HOST) "mv -f deploy.sh ../ && cd .. && chmod +x deploy.sh && ./deploy.sh"

# lancer le deploiement du front via GitHub Pages et ouvrir la page
	@echo ""
	@echo "💻 Lancement de la page PSG Infos..."
	cd frontend && npm run deploy

	@echo ""
	@echo "✅ Makefile terminé !"
	@echo "------------------------------------------"

	@echo ""
	@echo "🌐 Ouvre ta page ici --> http://benjaminmontet.me/psginfos/"
	@echo "🌐 Ouvre ta page ici --> http://www.benjaminmontet.me/psginfos/"
	@echo "🌐 Ouvre ta page ici --> https://www.benjaminmontet.me/psginfos/"
	@echo ""


# Pour info : make help
help:
	@echo "Commandes disponibles :"
	@echo "  make deploy   -> Transfert du code vers Alwaysdata et exécution de deploy.sh"
	@echo "  make help     -> Affiche cette aide"
