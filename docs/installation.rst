.. _installation:

Instructions d'installation
===========================

Etapes pour faire fonctionner l'application en local:

Cloner le repository
--------------------

- `cd /path/to/put/project/in`
- `git clone https://github.com/charlesm-git/Python-OC-Lettings-FR`

Créer l'environnement virtuel
-----------------------------

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

Exécuter le site
----------------

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

Journalisation via Sentry
-------------------------

- `cd /path/to/Python-OC-Lettings-FR`
- Créer un fichier .env : `touch .env` (`New-Item '.env' -ItemType 'file'` sur Windows)
- Modifier le contenu du fichier `.env` créé en ajoutant:
    - SENTRY_DSN=link_to_your_sentry_dsn_here