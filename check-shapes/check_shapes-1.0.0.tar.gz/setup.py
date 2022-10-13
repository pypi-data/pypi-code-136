# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['check_shapes', 'check_shapes.integration']

package_data = \
{'': ['*']}

install_requires = \
['lark>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'check-shapes',
    'version': '1.0.0',
    'description': 'A library for annotating and checking the shapes of tensors.',
    'long_description': '# check_shapes\n\n`check_shapes` is a library for annotating and checking tensor shapes.\nFor example:\n\n```python\nimport tensorflow as tf\n\nfrom gpflow.experimental.check_shapes import check_shapes\n\n@tf.function\n@check_shapes(\n    "features: [batch..., n_features]",\n    "weights: [n_features]",\n    "return: [batch...]",\n)\ndef linear_model(features: tf.Tensor, weights: tf.Tensor) -> tf.Tensor:\n    return tf.einsum("...i,i -> ...", features, weights)\n```\n\nFor more information see our [documentation](https://gpflow.github.io/check_shapes).\n\n## Installation\n\nThe recommended way to install `check_shapes` is from pypi:\n\n```bash\npip install check_shapes\n```\n\n### From source\n\nTo develop `check_shapes`, check it out from GitHub:\n\n```bash\ngit clone git@github.com:GPflow/check_shapes.git\n```\n\nWe use [Poetry](https://python-poetry.org/) to install and manage dependencies. Follow their\ninstructions for how to install Poetry itself. Then:\n\n```bash\ncd check_shapes\npoetry install\n```\n\nTo check you installation run our tests:\n\n```bash\npoetry run task test\n```\n\nFor testing with different versions of Python and dependencies, see the `poetryenv` script.',
    'author': 'Jesper Nielsen',
    'author_email': 'jespernielsen1982+check_shapes@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gpflow.github.io/check_shapes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
