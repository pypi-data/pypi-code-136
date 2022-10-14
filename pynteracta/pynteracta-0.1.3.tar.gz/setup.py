# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pynteracta']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT[crypto]>=2.5,<3.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['pynteracta = pynteracta.main:app']}

setup_kwargs = {
    'name': 'pynteracta',
    'version': '0.1.3',
    'description': 'A wrapper for Interacta API',
    'long_description': "PYnteracta, utility e wrapper per api di Interacta\n---------------------------------------------------\n\nUtility e libreria wrapper open-source in linguaggio Python per l'interfacciamento con le api rest\ndi [Interacta](https://catalogocloud.agid.gov.it/service/1892).\n\n\nInstallazione\n-------------\n\n```\npython -m pip install pynteracta\n```\n\nUtilizzo utility command line\n-----------------------------\n\nPynteracta ha un'interfaccia a riga di comando per verificare l'accesso all'ambiente di prova\nPlaygroud o ad un ambiente di produzione di Interacta.\n\nAccesso e lista dei post della community di default dell'ambiente Playgroud di Interacta.\n\n    $ pynteracta playground\n\n    Connessione all'ambiente Playground di Interacta...\n    Login effettuato con successo!\n    Elenco dei post:\n    ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n    ┃ Id  ┃ Titolo                                ┃ Descrizione                           ┃\n    ┡━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩\n    │ 599 │ Il mio primo post su Interacta        │ Questo è il mio primo post di         │\n    │     │                                       │ Interacta e lo sto creando tramite le │\n    │     │                                       │ Interacta External API.               │\n    │     │                                       │                                       │\n    │ 598 │ Benvenuto nel Playground di Interacta │ Interacta Playground è un ambiente    │\n    │     │                                       │ pensato per permetterti di testare le │\n    │     │                                       │ nostre API e verificare con i tuoi    │\n    │     │                                       │ occhi i risultati delle tue chiamate. │\n    │     │                                       │                                       │\n    │     │                                       │ Si tratta di un ambiente condiviso,   │\n    │     │                                       │ quindi utilizza un linguaggio....     │\n    │     │                                       │                                       │\n    └─────┴───────────────────────────────────────┴───────────────────────────────────────┘\n\nAccesso e lista dei post della community di default di un ambiente di produzione di Interacta.\n\nSono supportati due metodi di accesso:\n\n- [Username/Password](https://injenia.atlassian.net/wiki/spaces/IEAD/pages/3624075265/Autenticazione#Autenticazione-per-mezzo-di-Username-%2F-Password%3A)\n```\n    $ pynteracta login --base-url **URL_PRODUZIONE** --user **UTENTE**\n    Password: ****\n    Connessione all'instanza Interacta **URL_PRODUZIONE** con 'username/password' ...\n    Login effettuato con successo!\n```\n\n- [Service Account](https://injenia.atlassian.net/wiki/spaces/IEAD/pages/3624075265/Autenticazione#Autenticazione-via-Service-Account-(Server-to-Server))\n```\n    $ pynteracta login --base-url **URL_PRODUZIONE** --service-account-file **PATH**\n    Password: ****\n    Connessione all'instanza Interacta **URL_PRODUZIONE** con 'service account' ...\n    Login effettuato con successo!\n```\n\nRecupero lista dei primi 10 post della community identificata dall'id passata come parametro\n\n    $ pynteracta --base-url **URL_PRODUZIONE** list-posts **COMMUNITY-ID**\n\nLogout da un ambiente di produzione\n\n    $ pynteracta logout\n",
    'author': 'Simone Dalla',
    'author_email': 'simodalla@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
