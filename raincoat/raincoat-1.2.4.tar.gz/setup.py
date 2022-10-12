# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raincoat', 'raincoat.match']

package_data = \
{'': ['*']}

install_requires = \
['asttokens', 'click', 'colorama', 'requests', 'typing-extensions']

extras_require = \
{':python_version < "3.10"': ['importlib-metadata']}

entry_points = \
{'console_scripts': ['raincoat = raincoat.cli:main'],
 'raincoat.match': ['django = raincoat.match.django:DjangoMatch',
                    'pygithub = raincoat.match.pygithub:PyGithubMatch',
                    'pypi = raincoat.match.pypi:PyPIMatch']}

setup_kwargs = {
    'name': 'raincoat',
    'version': '1.2.4',
    'description': 'Raincoat has you covered when you cannot stay DRY. Linter for copy-pasted code.',
    'long_description': 'Raincoat\n========\n\n.. image:: https://badge.fury.io/py/raincoat.svg\n    :target: https://pypi.org/pypi/raincoat\n    :alt: Deployed to PyPI\n\n.. image:: https://readthedocs.org/projects/raincoat/badge/?version=latest\n    :target: http://raincoat.readthedocs.io/en/latest/?badge=latest\n    :alt: Documentation Status\n\n.. image:: https://travis-ci.org/ewjoachim/raincoat.svg?branch=master\n    :target: https://travis-ci.org/ewjoachim/raincoat\n    :alt: Continuous Integration Status\n\n.. image:: https://raw.githubusercontent.com/ewjoachim/raincoat/python-coverage-comment-action-data/badge.svg\n    :target: https://github.com/ewjoachim/raincoat/tree/python-coverage-comment-action-data\n    :alt: Coverage Status\n\n.. image:: https://img.shields.io/badge/License-MIT-green.svg\n    :target: https://github.com/ewjoachim/raincoat/blob/master/LICENSE\n    :alt: MIT License\n\n.. image:: https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg\n    :target: CODE_OF_CONDUCT.md\n    :alt: Contributor Covenant\n\nRaincoat has you covered when you can\'t stay DRY. When the time comes where you HAVE to\ncopy code from a third party, Raincoat will let you know when this code is changed so\nthat you can update your local copy.\n\n\nThe problem\n-----------\n\nLet\'s say you\'re using a lib named ``umbrella`` which provides a function named\n``use_umbrella`` and it reads as such:\n\n.. code-block:: python\n\n    def use_umbrella(umbrella):\n\n        # Prepare umbrella\n        umbrella.remove_pouch()\n        umbrella.open()\n\n        # Use umbrella\n        while rain_detector.still_raining():\n            umbrella.keep_over_me()\n\n        # Put umbrella away\n        umbrella.close()\n        while not umbrella.is_wet():\n            time.sleep(1)\n        umbrella.put_pouch()\n\n\nThis function does what it says it does, but it\'s not ideally split, depending on\nyour needs. For example, maybe at some point you realize you need each of the 3 separate\nparts to be a function of its own. Or maybe you can\'t call ``time.sleep`` in your app. Or do\nsomething else with the ``umbrella`` when it\'s opened, like dance with it.\n\nIt\'s also possible that you can\'t really make a pull request because your needs are\nspecific, or you don\'t have the time (that\'s sad but, hey, I know it happens) or any\nother personal reason. So what do you do? There\'s no real alternative. You copy/paste\nthe code, modify it to fit your needs and use your modified version. And whenever\nthere\'s a change to the upstream function, chances are you\'ll never know.\n\n\nThe solution\n------------\n\n*Enter Raincoat.*\n\nYou have made your own private copy of ``umbrella.use_umbrella`` (umbrella being at the\ntime at version 14.5.7) and it looks like this:\n\n.. code-block:: python\n\n    def dance_with_umbrella(umbrella):\n        """\n        I\'m siiiiiinging in the rain!\n        """\n        # Prepare umbrella\n        umbrella.remove_pouch()\n        umbrella.open()\n\n        # Use umbrella\n        while rain_detector.still_raining():\n            Dancer.sing_in_the_rain(umbrella)\n\n        # Put umbrella away\n        umbrella.close()\n        while not umbrella.is_wet()\n            time.sleep(1)\n        umbrella.put_pouch()\n\nNow simply add a comment somewhere (preferably just after the docstring) that says\nsomething like:\n\n.. code-block:: python\n\n    def dance_with_umbrella(umbrella):\n        """\n        I\'m siiiiiinging in the rain!\n        """\n        # This code was adapted from the original umbrella.use_umbrella function\n        # (we just changed the part inside the middle while loop)\n        # Raincoat: pypi package: umbrella==14.5.7 path: umbrella/__init__.py element: use_umbrella\n\n        ...\n\nNow, install and run ``raincoat`` in your project:\n\n.. code-block:: console\n\n    $ pip install raincoat\n    $ raincoat\n\n\nIt will:\n\nGrep the code for all ``# Raincoat:`` comments and for each comment:\n\n#. Look at the currently installed version of the lib (say, umbrella 16.0.3) (or, if not\n   found, the latest version)\n#. Compare with the version in the Raincoat comment (here, 14.5.7)\n#. If they are different, download and pip install the specified version in a temp dir\n   (using cached wheel as pip does by default, this should be quite fast in most cases)\n#. Locate the code using the provided path for both the downloaded and the currently\n   installed versions\n#. Diff it\n#. Tell you if there\'s a difference (and mention the location of the original Raincoat\n   comment)\n\nWhether there is something to change or not, you\'ve now verified your code with umbrella\n16.0.3, so you can update manually the umbrella comment.\n\n.. code-block:: python\n\n\t# Raincoat: pypi package: umbrella==16.0.3 path: umbrella/__init__.py element: use_umbrella"\n\nRaincoat can be used like a linter, you can integrate it in CI, make it a tox target...\n\n\nAnd beyond!\n-----------\n\nActually, the base principle of Raincoat can be extended to many other subjects than\nPyPI packages. To fit this, Raincoat was written with a modular achitecture allowing\nother kinds of Raincoat comments.\n\nFor now Raincoat comes with:\n\n- *PyPI*: The module presented above\n- *Django*: A module that checks if a given bug in Django for which you may have had\n  to write a workaround is fixed in your (or the latest) version of Django. Syntax is :\n\n.. code-block:: python\n\n\t# Raincoat: django ticket: #26976\n\n- *PyGitHub*: Same as the PyPI module but using Github. It\'s useful if your upstream is\n  a python package that\'s not on PyPI, like, say, the Python Standard Library itself.\n  Say you want to know if the element ``Maildir._lookup`` in the file ``Lib/mailbox.py``\n  changed on the master branch since commit 43ba8861. What you can do is:\n\n.. code-block:: python\n\n\t# Raincoat: pygithub repo: python/cpython@43ba8861 branch: master path: Lib/mailbox.py element: Maildir._lookup\n\nYou can also create your own Raincoat comment checker.\n\nYou can head to the `Quickstart\n<https://raincoat.readthedocs.io/en/stable/quickstart.html>`_ section for a general tour\nor to the `How-To <https://raincoat.readthedocs.io/en/stable/howto_index.html>`_\nsections for specific features. The `Discussions\n<https://raincoat.readthedocs.io/en/stable/discussions.html>`_ section should hopefully\nanswer your questions. Otherwise, feel free to open an `issue\n<https://github.com/ewjoachim/raincoat/issues>`_.\n\n.. Below this line is content specific to the README that will not appear in the doc.\n.. end-of-index-doc\n\nWhere to go from here\n---------------------\n\nThe complete docs_ is probably the best place to learn about the project.\n\nIf you encounter a bug, or want to get in touch, you\'re always welcome to open a\nticket_.\n\n.. _docs: https://raincoat.readthedocs.io/en/stable\n.. _ticket: https://github.com/ewjoachim/raincoat/issues/new\n',
    'author': 'Joachim Jablon',
    'author_email': 'ewjoachim@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://raincoat.readthedocs.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
