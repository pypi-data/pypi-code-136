# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['textual',
 'textual.cli',
 'textual.cli.previews',
 'textual.css',
 'textual.devtools',
 'textual.drivers',
 'textual.layouts',
 'textual.renderables',
 'textual.widgets']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.11.3,<5.0.0',
 'nanoid>=2.0.0,<3.0.0',
 'rich>=12.6.0,<13.0.0']

extras_require = \
{':python_version < "3.10"': ['typing-extensions>=4.0.0,<5.0.0'],
 'dev': ['aiohttp>=3.8.1,<4.0.0', 'click==8.1.2', 'msgpack>=1.0.3,<2.0.0']}

entry_points = \
{'console_scripts': ['textual = textual.cli.cli:run']}

setup_kwargs = {
    'name': 'textual',
    'version': '0.2.0b6',
    'description': 'Modern Text User Interface framework',
    'long_description': '# Textual\n\n![Textual splash image](./imgs/textual.png)\n\nTextual is a Python framework for creating interactive applications that run in your terminal.\n\n<details>\n  <summary> 🎬 Code browser </summary>\n  <hr>\n\n  This is the [code_browser.py](./examples/code_browser.py) example which clocks in at 61 lines (*including* docstrings and blank lines).\n\n  https://user-images.githubusercontent.com/554369/189394703-364b5caa-97e0-45db-907d-7b1620d6411f.mov\n  \n </details>\n\n\n## About\n\nTextual adds interactivity to [Rich](https://github.com/Textualize/rich) with a Python API inspired by modern web development.\n\nOn modern terminal software (installed by default on most systems), Textual apps can use **16.7 million** colors with mouse support and smooth flicker-free animation. A powerful layout engine and re-usable components makes it possible to build apps that rival the desktop and web experience. \n\n## Compatibility\n\nTextual runs on Linux, macOS, and Windows. Textual requires Python 3.7 or above.\n\n## Installing\n\nInstall Textual via pip:\n\n```\npip install textual[dev]\n```\n\nThe addition of `[dev]` installs Textual development tools.\n\n\n## Reference commands\n\nThe `textual` command has a few sub-commands to preview Textual styles.\n\n<details>  \n  <summary> 🎬 Easing reference </summary>\n  <hr>\n  \nThis is the *easing* reference which demonstrates the easing parameter on animation, with both movement and opacity. You can run it with the following command:\n  \n```bash\ntextual easing\n```\n\nhttps://user-images.githubusercontent.com/554369/189485538-31e794ff-61d7-4faf-902a-6e90a9d76e5b.mov\n\n </details>\n\n<details>  \n  <summary> 🎬 Borders reference </summary>\n  <hr>\n  \nThis is the borders reference which demonstrates some of the borders styles in Textual. You can run it with the following command:\n  \n```bash\ntextual borders\n```\n  \n\nhttps://user-images.githubusercontent.com/554369/189485735-cb2b4135-caee-46d7-a118-66cd7ed9eef5.mov\n\n\n  \n</details>\n\n## Examples\n\nThe Textual repository comes with a number of examples you can experiment with or use as a template for your own projects.\n\n<details>  \n  <summary> 📷 Calculator </summary>\n  <hr>\n  \nThis is [calculator.py](./examples/calculator.py) which demonstrates Textual grid layouts.\n  \n![calculator screenshot](./imgs/calculator.svg)\n</details>\n\n<details>\n  <summary> 📷 Code browser </summary>\n  <hr>\n\n  This is [code_browser.py](./examples/code_browser.py) which demonstrates the directory tree widget.\n  \n![code browser screenshot](./imgs/codebrowser.svg)\n  \n</details>\n\n\n<details>\n  <summary> 📷 Stopwatch </summary>\n  <hr>\n\n  This is the Stopwatch example from the tutorial.\n  \n### Light theme \n  \n![stopwatch light screenshot](./imgs/stopwatch_light.svg)\n\n### Dark theme\n  \n![stopwatch dark screenshot](./imgs/stopwatch_dark.svg)\n\n</details>\n',
    'author': 'Will McGugan',
    'author_email': 'will@textualize.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Textualize/textual',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
