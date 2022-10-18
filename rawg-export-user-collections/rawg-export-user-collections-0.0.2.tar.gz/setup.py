# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rawg_export_user_collections']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp[speedups]>=3.8.3,<4.0.0', 'pydantic>=1.10.2,<2.0.0']

entry_points = \
{'console_scripts': ['rawg_export_user_collections = '
                     'rawg_export_user_collections.main:run']}

setup_kwargs = {
    'name': 'rawg-export-user-collections',
    'version': '0.0.2',
    'description': "Export public user's collections from the rawg.io video game database.",
    'long_description': '# `rawg_export_user_collections`\n\nExport **public** user\'s collections from the [RAWG.IO](https://rawg.io/) video game database.\n\n## Installation\n\n```bash\npip install rawg_export_user_collections\n```\n\n## Options\n\n```\n--user_slug USER_SLUG                User slug from which we get collections.\n\n--export_folder_path EXPORT_FOLDER_PATH  Path where to export the file.\n```\n\n## Usage\n\n1. Get user slug from user profile page in [rawg.io](https://rawg.io/):\n\n   ![User profile page](https://github.com/TauSynth/rawg_export_user_collections/blob/main/docs/User%20profile%20page.png?raw=true)\n\n2. Run command:\n\n   ```bash\n   rawg_export_user_collections --user_slug=user_slug --export_folder_path=F:\\Backup\n   ```\n\n3. Exported json:\n\n   ```json\n   {\n     "count": 2,\n     "collections": [\n       {\n         "id": 25121,\n         "name": "Test collection 2",\n         "slug": "test-collection-2-2",\n         "url": "https://rawg.io/collections/test-collection-2-2",\n         "description": "",\n         "games_count": 2,\n         "created": "2022-10-17T16:46:55.253839Z",\n         "updated": "2022-10-17T16:47:55.254037Z",\n         "games": [\n           {\n             "id": 19369,\n             "name": "Call of Duty",\n             "slug": "call-of-duty",\n             "url": "https://rawg.io/games/call-of-duty",\n             "released": "2003-10-29",\n             "tba": false,\n             "rating": 4.19,\n             "updated": "2022-10-16T17:47:34",\n             "genres": [\n               "Action",\n               "Shooter"\n             ],\n             "platforms": [\n               "macOS",\n               "PC",\n               "Xbox 360",\n               "PlayStation 3"\n             ]\n           },\n           {\n             "id": 56114,\n             "name": "Medal of Honor: Frontline",\n             "slug": "medal-of-honor-frontline",\n             "url": "https://rawg.io/games/medal-of-honor-frontline",\n             "released": "2002-05-28",\n             "tba": false,\n             "rating": 3.92,\n             "updated": "2022-09-17T03:52:26",\n             "genres": [\n               "Shooter"\n             ],\n             "platforms": [\n               "PlayStation 3",\n               "Xbox",\n               "GameCube",\n               "PlayStation 2"\n             ]\n           }\n         ]\n       },\n       {\n         "id": 25120,\n         "name": "Test collection 1",\n         "slug": "test-collection-1",\n         "url": "https://rawg.io/collections/test-collection-1",\n         "description": "",\n         "games_count": 3,\n         "created": "2022-10-17T16:45:50.825922Z",\n         "updated": "2022-10-17T16:46:37.110669Z",\n         "games": [\n           {\n             "id": 5679,\n             "name": "The Elder Scrolls V: Skyrim",\n             "slug": "the-elder-scrolls-v-skyrim",\n             "url": "https://rawg.io/games/the-elder-scrolls-v-skyrim",\n             "released": "2011-11-11",\n             "tba": false,\n             "rating": 4.42,\n             "updated": "2022-10-13T10:58:37",\n             "genres": [\n               "Action",\n               "RPG"\n             ],\n             "platforms": [\n               "PC",\n               "Nintendo Switch",\n               "Xbox 360",\n               "PlayStation 3"\n             ]\n           },\n           {\n             "id": 3498,\n             "name": "Grand Theft Auto V",\n             "slug": "grand-theft-auto-v",\n             "url": "https://rawg.io/games/grand-theft-auto-v",\n             "released": "2013-09-17",\n             "tba": false,\n             "rating": 4.47,\n             "updated": "2022-10-15T12:05:16",\n             "genres": [\n               "Action",\n               "Adventure"\n             ],\n             "platforms": [\n               "PC",\n               "Xbox Series S/X",\n               "PlayStation 4",\n               "PlayStation 3",\n               "Xbox 360",\n               "Xbox One",\n               "PlayStation 5"\n             ]\n           },\n           {\n             "id": 10615,\n             "name": "System Shock 2",\n             "slug": "system-shock-2",\n             "url": "https://rawg.io/games/system-shock-2",\n             "released": "1999-08-11",\n             "tba": false,\n             "rating": 4.14,\n             "updated": "2022-10-03T11:21:32",\n             "genres": [\n               "Action",\n               "Shooter",\n               "RPG"\n             ],\n             "platforms": [\n               "PC",\n               "macOS",\n               "Linux"\n             ]\n           }\n         ]\n       }\n     ]\n   }\n   ```\n',
    'author': 'TauSynth',
    'author_email': 'the.dark.neutronium.tau.synth@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
