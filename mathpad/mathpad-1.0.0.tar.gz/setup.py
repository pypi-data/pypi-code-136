# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mathpad']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20,<2.0',
 'plotly>=5.3.1,<6.0.0',
 'scipy>=1.7.1,<2.0.0',
 'sympy>=1.8,<2.0',
 'tqdm>=4.62.3,<5.0.0',
 'typing-extensions>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'mathpad',
    'version': '1.0.0',
    'description': 'Simplified interface to Sympy for solving physics, engineering and maths problems',
    'long_description': '# MathPad\n\n<!-- TODO: set up all the services needed for these badges -->\n<!-- <p align="center">\n  <a href="https://github.com/CallumJHays/mathpad/actions?query=workflow%3ACI">\n    <img src="https://img.shields.io/github/workflow/status/CallumJHays/mathpad/CI/main?label=CI&logo=github&style=flat-square" alt="CI Status" >\n  </a>\n  <a href="https://mathpad.readthedocs.io">\n    <img src="https://img.shields.io/readthedocs/mathpad.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">\n  </a>\n  <a href="https://codecov.io/gh/CallumJHays/mathpad">\n    <img src="https://img.shields.io/codecov/c/github/CallumJHays/mathpad.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">\n  </a>\n</p>\n<p align="center">\n  <a href="https://python-poetry.org/">\n    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">\n  </a>\n  <a href="https://github.com/ambv/black">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">\n  </a>\n  <a href="https://github.com/pre-commit/pre-commit">\n    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">\n  </a>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/mathpad/">\n    <img src="https://img.shields.io/pypi/v/mathpad.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">\n  </a>\n  <img src="https://img.shields.io/pypi/pyversions/mathpad.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">\n  <img src="https://img.shields.io/pypi/l/mathpad.svg?style=flat-square" alt="License">\n</p> -->\n\nMathPad is a a Python library that makes it easy to solve engineering, science and maths problems.\n\nMathPad is ideal for engineering students and academics seeking to easily check their work or better understand the mathematical models and equations they are working with.\n\n[Sandbox Demo](https://callumjhays.github.io/mathpad/lab?path=Walkthrough.ipynb)\n\n\n\n\nFeatures:\n- Intuitive interface for those unfamiliar with Python\n- Easy-to-use construction of systems of equations - goodbye hand calculations!\n- Self-explanatory latex output\n- Automatic dimensionality validity checking\n- Automatic unit conversion\n- Easy simulation of differential systems of equations / initial value problem\n- Growing library of equations and constants to utilize\n\n## Documentation\n\nCurrently the only documentation is `Walkthrough.ipynb`. You can access it on the [JupyterLite Sandbox Site here](https://callumjhays.github.io/mathpad/lab?path=Walkthrough.ipynb)\n\n\n## Installation\n\nInstall via pip:\n\n`pip install mathpad`\n\n<!-- ## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)): -->\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<!-- markdownlint-enable -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\n<!-- This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome! -->\n\n## Credits\n\nThis package was created with\n[Cookiecutter](https://github.com/audreyr/cookiecutter) and the\n[browniebroke/cookiecutter-pypackage](https://github.com/browniebroke/cookiecutter-pypackage)\nproject template.\n',
    'author': 'Callum J Hays',
    'author_email': 'callumjhays@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/CallumJHays/mathpad',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
