# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['receipt_scanner', 'receipt_scanner.image', 'receipt_scanner.image.filters']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'numpy>=1.23.3,<2.0.0',
 'opencv-python>=4.6.0,<5.0.0',
 'pytesseract>=0.3.10,<0.4.0']

entry_points = \
{'console_scripts': ['scanner = receipt_scanner.cli:dispatcher']}

setup_kwargs = {
    'name': 'receipt-scanner',
    'version': '0.2.0',
    'description': 'Write applications to charge money to your friends after you paid the whole bill by easily parsing the receipt 💸',
    'long_description': '<h1 align="center">Receipt Scanner</h1>\n\n<p align="center">\n    <em>\n        Write applications to charge money to your friends after you paid the whole bill by easily parsing the receipt 💸\n    </em>\n</p>\n\n<p align="center">\n<a href="https://pypi.org/project/receipt-scanner" target="_blank">\n    <img src="https://img.shields.io/pypi/v/receipt-scanner?label=version&logo=python&logoColor=%23fff&color=306998" alt="PyPI - Version">\n</a>\n<a href="https://github.com/daleal/receipt-scanner/actions?query=workflow%3Alinters" target="_blank">\n    <img src="https://img.shields.io/github/workflow/status/daleal/receipt-scanner/linters?label=linters&logo=github" alt="Linters">\n</a>\n</p>\n\n## Why would I use Receipt Scanner\n\nWe\'ve all been there: the dinner ended and the bill arrived at the table. Everyone is looking at you to pay for the bill. "_I will pay you back immediately_", they say. "_Just send a picture of the receipt I will transfer you the money_". **Idiots**. We all know most of them will have forgotten about the damn receipt picture as soon as they get into their cars. **Now you can take matters into your own hands**. Using this library, you can write an application that parses and classifies items from the receipt, and then charges money to your friends _automagically_. No more waiting for them to calculate the amount they owe you "_as soon as they have a minute_".\n\n## Installation\n\nInstall using pip!\n\n```sh\npip install receipt-scanner\n```\n\n## Usage\n\n### As a package\n\nAfter installation, you can import the `scan` method from the library. Just pass the image location (it can be a local path or a URL), an optional regular expression to filter the parsed text and the optional `debug` parameter:\n\n```py\nimport re\nfrom receipt_scanner import scan\n\nexpression = re.compile("([0-9]+\\.[0-9]+)")\nscanned_text_lines = scan(\n    "path/to/some/image.jpg",\n    regular_expression=expression,\n    debug=True,\n)\n```\n\nThe `scan` method returns a list of strings for each text line that the regular expression matched. If no regular expression gets passed, every parsed text line will be returned.\n\n### As a CLI\n\nYou can also use `receipt-scanner` as a CLI! Once installed, the `scanner` command will be available. Here is a sample usage:\n\n```sh\nscanner --image path/to/some/image.jpg --expression "([0-9]+\\.[0-9]+)" --debug\n```\n\n### Specifying allowed characters\n\nBy default, the library will use for the following characters:\n\n```py\nDEFAULT_ALLOWED_CHARACTERS = (\n    "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890\\ "\n)\n```\n\nNotice that the last "\\ " represents the space character.\n\nYou can pass a set of allowed characters to the engine, either by using the `--characters` flag when using the CLI or by passing the `allowed_characters` attribute to the `scan` method of the library.\n\n### Debugging\n\nThe `debug` flag will show logs of every step, and will freeze each image manipulation step to show the result of said manipulation. This can be useful to understand why the `scan` command might be returning an empty list, for example (you might find that the image has poor contrast and that the contour of the receipt is not being correctly mapped).\n\n## Developing\n\n### Requirements\n\n- [Poetry](https://python-poetry.org)\n- [Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html)\n- [Teseract Spanish](https://parzibyte.me/blog/2019/05/18/instalar-tesseract-ocr-idioma-espanol-ubuntu)\n\n### Steps\n\nClone the repository:\n\n```sh\ngit clone https://github.com/daleal/receipt-scanner.git\n\ncd receipt-scanner\n```\n\nThen, recreate the environment:\n\n```sh\nmake build-env\n```\n\nOnce the package is installed for development (`poetry install`), you can use the CLI from the virtualenv.\n\n## Aknowledgements\n\nMost of the code from this project was adapted from StackOverflow answers to questions about contour-finding, denoising and stuff like that. I also used code from several guides from the internet for utilities such as transforming a contour to a rect. Without those answers, most of this library would have been impossible for me to write. Thanks for the awesome information! 💖\n',
    'author': 'Daniel Leal',
    'author_email': 'dlleal@uc.cl',
    'maintainer': 'Daniel Leal',
    'maintainer_email': 'dlleal@uc.cl',
    'url': 'https://github.com/daleal/receipt-scanner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
