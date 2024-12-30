.. _quickstart:

Guide de Démarrage Rapide
=========================

Ce guide de démarrage rapide vous aidera à configurer et exécuter le projet en local en quelques étapes seulement.

Introduction
------------
Ce projet est une application web basée sur Django pour la gestion de locations

Prérequis
---------
Avant de commencer, assurez-vous d'avoir les outils suivants installés :

- Python 3.10+
- Django 5.x
- Docker (optionnel, pour une configuration conteneurisée)
- Git
- Outil pour environnements virtuels (par exemple, `venv` ou `virtualenv`)

Étapes d'Installation
----------------------
1. Clonez le dépôt :

    .. code-block:: bash

        cd path/to/your/project
        git clone https://github.com/charlesm-git/Python-OC-Lettings-FR

2. Configurez un environnement virtuel :

    .. code-block:: bash

        python -m venv venv
        source venv/bin/activate

3. Installez les dépendances requises :

    .. code-block:: bash

        pip install -r requirements.txt

Exécution de l'Application
---------------------------
1. Lancez le serveur de développement :

    .. code-block:: bash

        python manage.py runserver

2. Accédez à l'application dans votre navigateur :

   http://127.0.0.1:8000/

Exemple d'Utilisation
----------------------
1. Connectez-vous avec les identifiants administrateur par défaut.
    - Username : admin
    - Mot de passe : Abc1234!

2. Naviguez vers le tableau de bord et créez votre première entrée de location.

Optionnel : Configuration avec Docker
-------------------------------------
Si vous préférez utiliser Docker, suivez ces étapes :

1. Construisez l'image Docker :

    .. code-block:: bash

        docker build -t project-name .

2. Lancez le conteneur Docker :

    .. code-block:: bash

        docker run -p 8000:8000 project-name

3. Accédez à l'application dans votre navigateur :

   http://127.0.0.1:8000/

Aide
~~~~~
- Explorez la page :ref:`installation` pour des instructions détaillées sur l'installation de l'application.
- Consultez la page :ref:`deploiement` pour les procédures de déploiement.

