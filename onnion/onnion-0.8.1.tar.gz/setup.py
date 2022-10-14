# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onnion']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.0,<2.0.0', 'onnion-rt>=0.6.0', 'onnx>=1.9.0,<2.0.0']

entry_points = \
{'console_scripts': ['onnion = onnion.main:main']}

setup_kwargs = {
    'name': 'onnion',
    'version': '0.8.1',
    'description': 'onnx compiler',
    'long_description': '# onnion\n\n## Installation\nFrom [PyPI](https://pypi.org/project/onnion/):\n\n```\n$ pip3 install onnion\n```\n\nFrom [Dockerhub](https://hub.docker.com/repository/docker/idein/onnion):\n\n```\ndocker pull idein/onnion:20221014\n```\n\n\n## Usage\n\n```\n$ onnion ssd-10-post.onnx -o ssd_post_model.py\n$ python\n>>> from ssd_post_model import init_graph\n>>> graph = init_graph()\n>>> inputs = ... # List[np.array]\n>>> outputs = graph.run(*inputs)\n```\n\nWith docker:\n\n```\n$ docker run --rm -it -u $UID:$GID -v $(pwd):/work idein/onnion:20221014 ssd-10-post.onnx -o ssd_post_model.py\n```\n\nThe order of the inputs and the outputs in the `run` method corresponds to the order of the inputs and the outputs in the onnx graph.\n\nSee also [tutorial](https://github.com/Idein/onnion/tree/master#tutorial).\n\n## Development Guide\n\n```\n$ poetry install\n```\n',
    'author': 'Idein Inc.',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Idein/onnion/tree/master/compiler',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
