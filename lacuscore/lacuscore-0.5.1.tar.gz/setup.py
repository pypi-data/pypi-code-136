# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lacuscore']

package_data = \
{'': ['*']}

install_requires = \
['defang>=0.5.3,<0.6.0',
 'playwrightcapture>=1.15.9,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'ua-parser>=0.16.1,<0.17.0']

extras_require = \
{'docs': ['Sphinx>=5.2.3,<6.0.0']}

setup_kwargs = {
    'name': 'lacuscore',
    'version': '0.5.1',
    'description': 'Core of Lacus, usable as a module',
    'long_description': "# Modulable Lacus\n\nLacus, but as a simple module.\n\n# Installation\n\n```bash\npip install lacuscore\n```\n\n# Design\n\n`LacusCore` is the part taking care of enqueuing and capturing URLs or web enabled documents.\nIt can be used as a module in your own project, see below for the usage\n\n[Lacus](https://github.com/ail-project/lacus) is the webservice that uses `LacusCore`,\nand you can use [Pylacus](https://github.com/ail-project/pylacus) to query it.\n\nThe `enqueue`, `get_capture_status`, and `get_capture` methods if `LacusCore` and `PyLacus` have\nthe same parameters which means you can easily use them interchangeably in your project.\n\n\n# Usage\n\nThe recommended way to use this module is as follows:\n\n1. Enqueue what you want to capture with `enqueue` (it returns a UUID)\n2. Trigger the capture itself. For that, you have two options\n\n  * The `capture` method directly, if you pass it the UUID you got from `enqueue`.\n    This is what you want to use to do the capture in the same process as the one enqueuing the capture\n\n  * If you rather want to enqueue the captures in one part of your code and trigger the captures in an other one,\n    use `consume_queue` which will pick a capture from the queue and trigger the capture.\n    I this case, you should use `get_capture_status` to check if the capture is over before the last step.\n\n3. Get the capture result with `get_capture` with the UUID from you got from `enqueue`.\n\n# Example\n\n## Enqueue\n\n```python\n\nfrom redis import Redis\nfrom lacuscore import LacusCore\n\nredis = Redis()\nlacus = LacusCore(self.redis)\nuuid = lacus.enqueue('google.fr')\n```\n\n## Capture\n\n* Option 1: Trigger a specific capture via the UUID returned by the `enqueue` call\n\n```python\nawait lacus.capture(uuid)\n```\n\n* Option 2: Trigger the capture with the highest priority from the queue\n\n```python\nuuid = await lacus.consume_queue()\n```\n\n## Status of a capture\n\n```python\nstatus = lacus.get_capture_status(uuid)\n```\n\n## Capture result\n\n```python\nresult = lacus.get_capture(uuid)\n```\n\n",
    'author': 'Raphaël Vinot',
    'author_email': 'raphael.vinot@circl.lu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
