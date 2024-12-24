## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/charlesm-git/Python-OC-Lettings-FR`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Journalisation via Sentry

- `cd /path/to/Python-OC-Lettings-FR`
- Créer un fichier .env `touch .env` (`New-Item '.env' -ItemType 'file'` sur Windows)
- Modifier le contenu du fichier `.env` créé en ajoutant:
  * SENTRY_DSN=link_to_your_sentry_dsn_here

#### Déploiement

Un pipeline CI/CD a été mis en place en utilisant Github Actions. Il permet :
- le lancement des tests et du linting à chaque commit sur le repository Github
- le lancement du travail de conteneurisation sur Docker et de déploiement sur Render pour tous commit réalisé sur la branche master

Configuration du pipeline :
- Workflow de test et de linting : ne requière aucune configuration
- Workflow de conteneurisation via Docker :
  * Vous devez posséder un compte Docker Hub
  * Sur votre repository Github
    + `Settings` `Secrets and variables` `Actions`
    + Modifier les variables secrètes `DOCKER_PASSWORD`et `DOCKER_USERNAME` avec vos propres identifiants
- Workflow de déploiement via Render :
  * `cd /path/to/Python-OC-Lettings-FR`
  * `python manage.py collectstatic`
  * `docker login`
  * `docker build -t your-docker-username/oc-lettings-site:latest .`
  * `docker push your-docker-username/oc-lettings-site:latest`
  * Depuis votre compte Render `Account Settings` `API Keys`, générer une nouvelle clé. Copier cette clé dans la variable secrète du repository Github `RENDER_API_KEY`
  * Créer un nouveau Web Service sur Render
    + Source Code : Existing Image
    + Image URL : `your-docker-username/oc-lettings-site:latest`
    + Vous pouvez choisir le plan gratuit
  * Depuis l'URL de la page event, vous pouvez récupérer le service-ID : `https://dashboard.render.com/web/<serviceID>/events`
  * Copier le serviceID et copier le dans la variable secrète Github `RENDER_SERVICE_ID`

Après cette configuration, le pipeline CI/CD devrait fonctionner correctement.

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
