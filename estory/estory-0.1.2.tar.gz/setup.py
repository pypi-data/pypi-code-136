# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['estory']

package_data = \
{'': ['*']}

install_requires = \
['bl-event-sourcing-sqlalchemy>=0.1.0',
 'bl-event-sourcing>=0.1.0',
 'typer>=0.4.1,<0.5.0']

extras_require = \
{'mysql': ['PyMySQL>=1.0.2,<2.0.0']}

entry_points = \
{'console_scripts': ['estory = estory:app']}

setup_kwargs = {
    'name': 'estory',
    'version': '0.1.2',
    'description': 'Read from and write to event stores',
    'long_description': '# estory — read from and write to event stores\n\n```console\n$ estory init <IDENTIFIER>\n$ estory read <IDENTIFIER>\n$ estory write <IDENTIFIER>\n$ estory guess <IDENTIFIER>\n```\n\n**IDENTIFIER** is either:\n\n- a proper DSN (`driver://user:password@host:port/database`)\xa0;\n- a file that will be interpreted as a DSN (`sqlite:///<FILE>`)\xa0;\n- a name matching an environment variable (`ESTORY_DSN_<NAME>`).\n\nTo initialise an event store:\n\n```console\n$ export ESTORY_DSN_TMP="sqlite:////tmp/event_store.sqlite"\n$ estory init TMP\n```\n\nTo write an event to a store:\n\n```console\n$ jo stream="uuid" version=1 name="EventName" data=$(jo id=1) unixtime=$(date +%s) | estory write TMP\n```\n\nTo read events from a store:\n\n```console\n$ estory read TMP\n{"stream": "uuid", "name": "EventName", "data": {"id": 1}, "unixtime": 1647876362, "who": "", "id": 1}\n```\n\nTo copy events from one store to another:\n\n```console\n$ export ESTORY_DSN_TMP2="sqlite:////tmp/another_event_store.sqlite"\n$ estory init TMP2\n$ estory read TMP | estory write TMP2\n```\n\nTo copy only some events from one store to another:\n\n```console\n$ estory read TMP | jq \'.|select(.id==2)\' | estory write TMP2\n```\n\nTo modify events while copying them from one store to another:\n\n```console\n$ estory read TMP | jq \'.|.name="EventNewName"\' | estory write TMP2\n```\n',
    'author': 'Tanguy Le Carrour',
    'author_email': 'tanguy@bioneland.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.easter-eggs.org/bioneland/estory',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
