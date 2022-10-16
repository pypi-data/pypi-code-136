# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bdbomdiff']

package_data = \
{'': ['*']}

install_requires = \
['blackduck>=1.0.7,<2.0.0', 'importlib-resources>=5.9.0,<6.0.0']

entry_points = \
{'console_scripts': ['bdbomdiff = bdbomdiff:main']}

setup_kwargs = {
    'name': 'bdbomdiff',
    'version': '0.3.1',
    'description': 'Blackduck BOM Diff to excel for AOSD import',
    'long_description': '# BDBOMDIFF\n\nBlackduck BOM Diff to excel for AOSD import\n\n## Description\n\nThis is intended for finding new OSS component to be imported into AOSD\n\n## Getting Started\n\n### Dependencies\n\n- Blackduck\n- importlib-resources\n\n### Installing\n\n- pip install bdbomdiff\n\n### Executing program\n\n- How to run the program\n\n```\n<!-- on the folder it is running place this blackduck config file for blackduck library-->\n.restconfig.json\n{\n    <!-- make sure Blackduck_url should not end with slash -->\n  "baseurl": "Blackduck_url",\n  "api_token": "API_KEY",\n  "insecure": true,\n  "debug": false\n}\n\nbdbomdiff PROJECT_NAME NEW_VERSION OLD_VERSION -o OUTPUT_DIR\n\n```\n\n## Help\n\nAny advise for common problems or issues.\n\n```\n>bdbomdiff -h\nusage: Retreive BOM component info for the given project and version [-h] -o O [-l LIMIT | -u | -r] [-v] [-c] project_name version oldversion\n\npositional arguments:\n  project_name\n  version\n  oldversion\n\noptions:\n  -h, --help            show this help message and exit\n  -o O                  Output directory\n  -l LIMIT, --limit LIMIT\n                        Set limit on number of components to retrieve\n  -u, --unreviewed\n  -r, --reviewed\n  -v, --vulnerabilities\n                        Get the vulnerability info for each of the components\n  -c, --custom_fields   Get the custom field info for each of the components\n```\n\n## Authors\n\nDinesh Ravi\n\n## Version History\n\n- 0.3.0\n  - get license, homepage url, description, copyright and files info,\n- 0.2.0\n  - Documentation update\n- 0.1.0\n  - Initial Release\n\n## License\n\nThis project is licensed under the MIT License - see the [MIT](LICENSE) file for details\n\n## Acknowledgments\n\n- [Blackduck](https://pypi.org/project/blackduck/)\n- [importlib-resources](https://pypi.org/project/importlib-resources/)\n',
    'author': 'dineshr93gmail.com',
    'author_email': 'None',
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
