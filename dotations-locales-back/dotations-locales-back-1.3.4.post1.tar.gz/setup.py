# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dotations_locales_back',
 'dotations_locales_back.common',
 'dotations_locales_back.common.mapping',
 'dotations_locales_back.simulation',
 'dotations_locales_back.web_api']

package_data = \
{'': ['*']}

install_requires = \
['OpenFisca-France-Dotations-Locales>=0.8.1,<0.9.0',
 'fastapi>=0.78.0,<0.79.0',
 'pandas>=1.3,<2.0',
 'uvicorn>=0.18.2,<0.19.0']

setup_kwargs = {
    'name': 'dotations-locales-back',
    'version': '1.3.4.post1',
    'description': 'Le dorsal de dotations.incubateur.anct.gouv.fr',
    'long_description': "# dotations-locales-back\n\n## Installation\n\n> Les étapes qui suivent supposent que Python est déjà installé dans votre environnement. \nLa version de Python nécessaire est décrite dans le fichier `pyproject.toml` à la récine du dépôt. \n\nLa configuration des dépendances est gérée avec [poetry](https://python-poetry.org).\n\n> Pour gérer différentes versions de Python sur une machine, nous utilisons `pyenv` qui permet par exemple d'installer une version avec `pyenv install 3.8.9` et `poetry env use python3.8`.\n\nPour créer un environnement virtuel et installer les dépendances de l'application, exécuter la commande suivante dans un terminal :\n\n```shell\npoetry install\n```\n\nCette commande doit s'achever sans erreur.\n\nOn peut voir les dépendances installées avec cette commande : \n\n```shell\npoetry show\n```\n> De même avec `poetry run pip list` pour les nostalgiques de pip 🙂\n\n## Démarrer l'API Web\n\nL'API Web est bâtie sur le framework [FastAPI](https://fastapi.tiangolo.com). \n\nPour la démarrer en local, après avoir suivi les étapes d'installation, exécuter la commande suivante dans un terminal :\n\n```shell\npoetry run uvicorn dotations_locales_back.web_api.main:app --reload\n```\n\nL'API Web est alors accessible à l'adresse suivante : `http://127.0.0.1:8000`\n\nElle peut être testée via l'interface Swagger UI à cette adresse : `http://127.0.0.1:8000/docs`\n\n## Tests\n\nPour lancer les tests il faut exécuter la commande suivante dans un terminal :\n\n```shell\npoetry run pytest\n```\n\nOu depuis un terminal avec l'environnement virtuel activé :\n\n```shell\npytest\n```\n\n\n## Déploiement sur Scalingo\n\nPour déployer cette application sur Scalingo, il est nécessaire de créer 3 fichiers supplémentaires. En effet Scalingo n'est pas compatible avec les fichiers de gestion des dépendances créés par Poetry.\n\nVoici les fichiers à créer : \n* `requirements.txt` : Scalingo se base sur ce fichier pour installer les dépendances.  \nPour le créer il faut éxécuter la commande suivante :\n    ```shell\n    poetry export -f requirements.txt --without-hashes --output requirements.txt\n    ```\n> **Attention** : Si des dépendances sont ajoutées via Poetry, il faudra regénérer le fichier `requirements.txt` à chaque fois également. En effet, Poetry gère automatiquement l'ajout de dépendances dans son propre fichier `pyproject.toml` mais pas dans le fichier `requirements.txt`.\n\n* `runtime.txt` : Scalingo se base sur ce fichier pour définir la version de python à utiliser. Il s'agit donc de s'assurer de sa cohérence avec la version de Python indiquée dans `pyproject.toml`\n\n* `Procfile` : Lors du déploiement Scalingo se base sur ce fichier pour éxécuter la commande qui lance l'application.\nL'hôte requis est `0.0.0.0` et il faut également que le serveur écoute le port défini dans une variable d'environnement `PORT`. Il faut donc ajouter la ligne suivante au fichier `Procfile` :\n    ```\n    web: uvicorn web_api.main:app --host=0.0.0.0 --port=${PORT:-5000}\n    ```\n",
    'author': 'Equipe Dotations Locales',
    'author_email': 'contact-dotations-locales@anct.gouv.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/incubateur-territoires/startups/dotations-locales/dotations-locales-back/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
