# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['postprocess_sdist_make_rust_ext_opt']
install_requires = \
['redbaron>=0.9.2,<0.10.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['postprocess-sdist-make-rust-ext-opt = '
                     'postprocess_sdist_make_rust_ext_opt:app']}

setup_kwargs = {
    'name': 'postprocess-sdist-make-rust-ext-opt',
    'version': '0.1.0',
    'description': 'Post-process sdists to make Rust extensions optional',
    'long_description': 'None',
    'author': 'smheidrich',
    'author_email': 'smheidrich@weltenfunktion.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
