# Makefile pour déployer le projet sur AlwaysData

# Variables de configuration
REMOTE_NAME = alwaysdata
BRANCH = main
USER = benjaminmontet
HOST = ssh-benjaminmontet.alwaysdata.net
DEPLOY_SCRIPT = deploy.sh

# Tâche principale : push + exécution du script
deploy:
	@echo "🚀 Pousser le code sur AlwaysData..."
	rsync -av --exclude '.git' --exclude 'venv' --exclude 'deploy.sh' --exclude 'frontend' --exclude 'Makefile' . benjaminmontet@ssh-benjaminmontet.alwaysdata.net:/home/benjaminmontet/www/
	@echo "✅ Code poussé avec succès."

	@echo "🚀 Lancement du script de déploiement à distance..."
	ssh $(USER)@$(HOST) "cd .. && chmod +x deploy.sh && ./deploy.sh"

	@echo "✅ Makefile ok"

# Pour info : make help
help:
	@echo "Commandes disponibles :"
	@echo "  make deploy   -> Push Git, transfert et exécution de deploy.sh"
	@echo "  make help     -> Affiche cette aide"
