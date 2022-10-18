# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['memobj', 'memobj.property']

package_data = \
{'': ['*']}

install_requires = \
['regex>=2022.9.13,<2023.0.0']

setup_kwargs = {
    'name': 'memobj',
    'version': '0.8.0',
    'description': 'A library for defining objects in memory',
    'long_description': '# memobj\nA library for defining objects in memory\n\n## installing\npython 3.11+ only!\n`pip install memobj`\n\n## usage\n```python\nimport os\n\nfrom memobj import WindowsProcess, MemoryObject\nfrom memobj.property import Signed4\n\n\nclass PythonIntObject(MemoryObject):\n    value: int = Signed4(24)\n\n\nprocess = WindowsProcess.from_id(os.getpid())\n\n# id(x) gives the address of the object in cpython\nmy_int = PythonIntObject(address=id(1), process=process)\n\n# prints 1\nprint(my_int.value)\n```\n\n## support\ndiscord\nhttps://discord.gg/7hBStdXkyR\n',
    'author': 'StarrFox',
    'author_email': 'starrfox6312@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StarrFox/memobj',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
