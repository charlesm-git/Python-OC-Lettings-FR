Déploiement et Gestion de l'application
=======================================

.. _deploiement:

Déploiement
-----------

Un pipeline CI/CD a été mis en place en utilisant Github Actions. Il permet :

- le lancement des tests et du linting à chaque commit sur le repository Github
- le lancement du travail de conteneurisation sur Docker et de déploiement sur Render pour tous commit réalisés sur la branche master


Workflow de test et de linting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ne requière aucune configuration


Workflow de conteneurisation via Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vous devez posséder un compte Docker Hub.

Sur votre repository Github :
    - `Settings`, `Secrets and variables`, `Actions`
    - Modifier les variables secrètes `DOCKER_PASSWORD`et `DOCKER_USERNAME` avec vos propres identifiants

Workflow de déploiement via Render
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vous devez posséder un compte Render.

1. Créer une première image Docker
    .. code-block:: bash

        cd /path/to/Python-OC-Lettings-FR
        python manage.py collectstatic
        docker login
        docker build -t your-docker-username/oc-lettings-site:latest .
        docker push your-docker-username/oc-lettings-site:latest

2. Depuis votre compte Render :
    - `Account Settings`, `API Keys`, générer une nouvelle clé. 
    - Copier cette clé dans la variable secrète du repository Github `RENDER_API_KEY`

3. Créer un nouveau Web Service sur Render
    - Source Code : Existing Image
    - Image URL : `your-docker-username/oc-lettings-site:latest`
    - Vous pouvez choisir le plan gratuit

4. Depuis l'URL de la page event, vous pouvez récupérer le service-ID : `https://dashboard.render.com/web/<serviceID>/events`

5. Copiez le serviceID et collez le dans la variable secrète Github `RENDER_SERVICE_ID`

Après cette configuration, le pipeline CI/CD devrait fonctionner correctement.

Gestion de l'application
------------------------

A l'heure actuelle, la base de données utilisées n'est que locale. Il est donc 
nécessaire de faire les modifications sur cette dernière en local puis de 
réaliser un nouveau déploiement afin d'ajouter, de modifier ou de 
supprimer des modèles.

Pour ce faire, il est possible d'accéder à l'interface utilisateur de Django :

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

Une fois les modifications réalisées, si vous avez configuré le pipeline CI/CD
correctement (voir section **Déploiement**), il suffit de réaliser un commit 
sur la branche Master pour appliquer les changements.