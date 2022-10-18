# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['loniapi']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.2.0,<2.0.0', 'requests>=2.22.1,<3.0.0']

setup_kwargs = {
    'name': 'loniapi',
    'version': '0.0.6',
    'description': 'package to make calls to loni ida',
    'long_description': "# loniapi\n\nloniapi is a Python package to make calls to the LONI API. It can list all files associated with a group-id and download specific files.\n\n## Installation\n\n1. Download the latest version of the loniapi package from Pypi\nhttps://pypi.org/project/loniapi/\n```bash\npip install loniapi\n```\n\n2. If step 1 errors outInstall pandas if it is not already installed. and requests. or upgrade\n```bash\npip install pandas      # pip install pandas --upgrade\npip install requests    # pip install requests --upgrade\n```\n\n3. Create a config file in your home directory\n```bash\ncd ~\nvim .loniApiConfig\n```\n\n4. Specify your group-id and loni log-in credentials\n```bash\n[<your-group-id>]\nemail = <your-email>\npassword = <your-password\n```\n\n## Usage\n\n```python\nfrom loniapi import filedownloader\nmyAPI = filedownloader.LoniApi()\n\n# Log-in using a group ID acquired from IDA/LONI\nmyAPI.login('ampad')\n\n# get list of files associated with the group id\nloniAPI.get_LONI_files()\n\n# test download a few file types \nmyAPI.download_LONI_file('1')   #is a pdf\nmyAPI.download_LONI_file('3')   #is a csv\n\n# to download a specific file version\nmyAPI.download_LONI_file(file_id = '2', version = '2015-11-13') #is a pdf\n\n# log out\nmyAPI.logout()\n\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n",
    'author': 'Hieu Do',
    'author_email': 'hieu.do@sagebionetworks.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
