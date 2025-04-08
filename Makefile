# Makefile pour déployer ton projet sur AlwaysData

# Variables de configuration
REMOTE_NAME = alwaysdata
BRANCH = main
USER = benjaminmontet
HOST = ssh-benjaminmontet.alwaysdata.net
DEPLOY_PATH = /home/benjaminmontet
DEPLOY_SCRIPT = deploy.sh

# Tâche principale : push + exécution du script
deploy:
	@echo "🚀 Pousser le code sur AlwaysData..."
	git push $(REMOTE_NAME) $(BRANCH)
	@echo "✅ Code poussé avec succès."

	@echo "📦 Transfert du script de déploiement..."
	scp $(DEPLOY_SCRIPT) $(USER)@$(HOST):$(DEPLOY_PATH)/$(DEPLOY_SCRIPT)
	@echo "🔧 Script transféré."

	@echo "🚀 Lancement du script de déploiement à distance..."
	ssh $(USER)@$(HOST) "chmod +x $(DEPLOY_SCRIPT) && ./$(DEPLOY_SCRIPT)"
	@echo "✅ Déploiement terminé."

# Pour info : make help
help:
	@echo "Commandes disponibles :"
	@echo "  make deploy   -> Push Git, transfert et exécution de deploy.sh"
	@echo "  make help     -> Affiche cette aide"
