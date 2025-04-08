# Makefile pour déployer le projet sur AlwaysData

# Variables de configuration
USER = benjaminmontet
HOST = ssh-benjaminmontet.alwaysdata.net

# Tâche principale : push + exécution du script
deploy:
	@echo "🚀 Pousser le code sur AlwaysData..."
# copier seulement le backend Django du projet
	rsync -av --exclude '.git' --exclude 'venv' --exclude 'frontend' --exclude 'Makefile' . benjaminmontet@ssh-benjaminmontet.alwaysdata.net:/home/benjaminmontet/www/
	@echo "✅ Code poussé avec succès."

	@echo "🚀 Lancement du script de déploiement à distance..."
	ssh $(USER)@$(HOST) "mv -f deploy.sh ../ && cd .. && chmod +x deploy.sh && ./deploy.sh"

	cd frontend
	@echo "✅ Makefile terminé !"

# Pour info : make help
help:
	@echo "Commandes disponibles :"
	@echo "  make deploy   -> Transfert du code vers Alwaysdata et exécution de deploy.sh"
	@echo "  make help     -> Affiche cette aide"
