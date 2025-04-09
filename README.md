🚀 Déploiement sur GitHub Pages
Le projet React est déployé automatiquement sur GitHub Pages via la branche gh-pages.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

📦 Étapes pour déployer :

--> npm run deploy

Cela exécute "npm run build" pour générer les fichiers de production (dans le dossier build/).
Déploie le contenu de build/ sur la branche "gh-pages" grâce au package gh-pages.

GitHub Pages sert ensuite directement ces fichiers pour afficher le site.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

🧠 Remarques :

Tu développes normalement sur la branche main.

La branche "gh-pages" est générée automatiquement à chaque déploiement, tu ne la modifies jamais manuellement.

Assure-toi que ton package.json contient bien :

json
"scripts": {
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
}

🌐 URL du site :
http://benjaminmontet.me/psginfos/
