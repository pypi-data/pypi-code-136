# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asari']

package_data = \
{'': ['*'], 'asari': ['data/*']}

install_requires = \
['Janome>=0.4.2,<0.5.0',
 'onnxruntime>=1.12.1,<2.0.0',
 'packaging>=21.3,<22.0',
 'scikit-learn>=1.1.1,<2.0.0',
 'skl2onnx>=1.13,<2.0']

setup_kwargs = {
    'name': 'asari',
    'version': '0.2.0',
    'description': 'Japanese sentiment analyzer implemented in Python.',
    'long_description': '# asari\n\nAsari is a Japanese sentiment analyzer implemented in Python.\n\n## Usage\n\nBehold, the power of asari:\n\n```python\nfrom asari.api import Sonar\nsonar = Sonar()\nsonar.ping(text="広告多すぎる♡")\n{\n  "text" : "広告多すぎる♡",\n  "top_class" : "negative",\n  "classes" : [ {\n    "class_name" : "positive",\n    "confidence" : 0.09130180181262026\n  }, {\n    "class_name" : "negative",\n    "confidence" : 0.9086981981873797\n  } ]\n}\n```\n\nAsari allows you to classify text into positive/negative class, without the need for training. You have only to fed text into asari.\n\n## Installation\n\nTo install asari, simply use `pip` with Python 3.8+:\n\n```bash\npip install asari\n```\n',
    'author': 'Hironsan',
    'author_email': 'hiroki.nakayama.py@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Hironsan/asari',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
