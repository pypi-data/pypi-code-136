# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['foam',
 'foam.app',
 'foam.app.command',
 'foam.app.information',
 'foam.app.postprocess',
 'foam.base',
 'foam.compat',
 'foam.extra',
 'foam.parse',
 'foam.util']

package_data = \
{'': ['*'],
 'foam': ['static/*',
          'static/demo/7/*',
          'static/demo/8/*',
          'static/demo/9/*',
          'static/grammar/*']}

install_requires = \
['PyYAML>=6.0,<7.0']

extras_require = \
{'7z': ['py7zr>=0.17.2,<0.18.0'],
 'cli': ['click>=8.0.3,<9.0.0'],
 'full': ['click>=8.0.3,<9.0.0',
          'lark>=1.1.2,<2.0.0',
          'py7zr>=0.17.2,<0.18.0',
          'tqdm>=4.63.1,<5.0.0',
          'typing-extensions>=4.3.0,<5.0.0',
          'vtk>=9.1.0,<10.0.0'],
 'lark': ['lark>=1.1.2,<2.0.0'],
 'tqdm': ['tqdm>=4.63.1,<5.0.0'],
 'type': ['typing-extensions>=4.3.0,<5.0.0'],
 'vtk': ['vtk>=9.1.0,<10.0.0']}

setup_kwargs = {
    'name': 'ifoam',
    'version': '0.12.1',
    'description': 'Python Interface to OpenFOAM Case (Configured Using YAML)',
    'long_description': '<!-- Template from https://github.com/othneildrew/Best-README-Template -->\n<div id="top"></div>\n\n\n\n<!-- PROJECT SHIELDS -->\n[![Contributors][contributors-shield]][contributors-url]\n[![Forks][forks-shield]][forks-url]\n[![Stargazers][stars-shield]][stars-url]\n[![Issues][issues-shield]][issues-url]\n[![GPL-3.0 License][license-shield]][license-url]\n\n\n\n<!-- PROJECT LOGO -->\n<br />\n<div align="center">\n  <a href="https://github.com/iydon/of.yaml">\n    🟢⬜🟩⬜🟩<br />\n    ⬜⬜⬜⬜⬜<br />\n    🟩⬜🟩⬜🟩<br />\n    ⬜⬜⬜⬜⬜<br />\n    🟩⬜🟩⬜🟩<br />\n  </a>\n\n  <h3 align="center">OpenFOAM.YAML</h3>\n\n  <p align="center">\n    Python Interface to OpenFOAM Case (Configured Using YAML)\n    <br />\n    <a href="https://ifoam.readthedocs.io"><strong>Explore the docs »</strong></a>\n    <br />\n    <br />\n    View <a href="https://github.com/iydon/of.yaml-template">Demo</a>/<a href="https://github.com/iydon/of.yaml-tutorial">Tutorial</a>\n    ·\n    <a href="https://github.com/iydon/of.yaml/issues">Report Bug</a>\n    ·\n    <a href="https://github.com/iydon/of.yaml/issues">Request Feature</a>\n  </p>\n</div>\n\n\n\n<!-- TABLE OF CONTENTS -->\n<details>\n  <summary>Table of Contents</summary>\n  <ol>\n    <li>\n      <a href="#about-the-project">About The Project</a>\n    </li>\n    <li>\n      <a href="#getting-started">Getting Started</a>\n      <ul>\n        <li><a href="#installation">Installation</a></li>\n        <li><a href="#demo">Demo</a></li>\n      </ul>\n    </li>\n    <li><a href="#contributing">Contributing</a></li>\n    <li><a href="#license">License</a></li>\n    <li><a href="#contact">Contact</a></li>\n  </ol>\n</details>\n\n\n\n<!-- ABOUT THE PROJECT -->\n## About The Project\n\nThis repository was originally designed to solve the problem of complex OpenFOAM case structure, and the solution was to re-present the original cases using the common configuration file format YAML. Later, since there is a corresponding package for the YAML format in Python, I wrote this Python interface package for OpenFOAM, and then I added progress bars to most OpenFOAM solvers by analyzing log files in real time. Although there are still many details to be specified in this repository, its function of generating cases and calling solvers is ready for preliminary use, for example, I used this package to generate cases in batch in my own project. In the future I would like to integrate the post-processing steps into this interface package as well.\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n\n\n<!-- GETTING STARTED -->\n## Getting Started\n\nThis project currently uses Poetry to manage Python dependencies. I\'ve heard good things about [PDM](https://github.com/pdm-project/pdm) so far, and may provide PDM support subsequently.\n\n### Installation\n\n```sh\npip3 install ifoam[full]\n```\n\n### Demo\n\nSave the following demo code as a separate file (e.g. `demo.py`).\n\n```python\nfrom foam import Foam\n\nfoam = Foam.from_demo(\'cavity\')\nfoam[\'foam\'][\'system\', \'controlDict\', \'endTime\'] = 1.0\nfoam.save(\'cavity\')\nfoam.cmd.all_run()\n```\n\nRunning the demo code in the virtual environment results in the following output.\n\n```sh\n$ python demo.py\n\nFoam.from_file(\'.../of.yaml/foam/demo/7/cavity.yaml\', warn=False)\nRunning blockMesh on .../of.yaml/cavity using 1 processes if in parallel\nRunning icoFoam on .../of.yaml/cavity using 1 processes if in parallel\n100%|█████████████████████████████████████| 1.0/1.0 [00:02<00:00,  2.24s/it]\n```\n\n\n\n<!-- CONTRIBUTING -->\n## Contributing\n\nContributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.\n\nIf you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".\nDon\'t forget to give the project a star! Thanks again!\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n\n\n<!-- LICENSE -->\n## License\n\nDistributed under the GPL-3.0 License. See `LICENSE.txt` for more information.\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n\n\n<!-- CONTACT -->\n## Contact\n\nIydon Liang - [@iydon](https://github.com/iydon) - liangiydon_AT_gmail.com\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n\n\n<!-- MARKDOWN LINKS & IMAGES -->\n[contributors-shield]: https://img.shields.io/github/contributors/iydon/of.yaml.svg?style=for-the-badge\n[contributors-url]: https://github.com/iydon/of.yaml/graphs/contributors\n[forks-shield]: https://img.shields.io/github/forks/iydon/of.yaml.svg?style=for-the-badge\n[forks-url]: https://github.com/iydon/of.yaml/network/members\n[stars-shield]: https://img.shields.io/github/stars/iydon/of.yaml.svg?style=for-the-badge\n[stars-url]: https://github.com/iydon/of.yaml/stargazers\n[issues-shield]: https://img.shields.io/github/issues-closed/iydon/of.yaml.svg?style=for-the-badge\n[issues-url]: https://github.com/iydon/of.yaml/issues\n[license-shield]: https://img.shields.io/github/license/iydon/of.yaml.svg?style=for-the-badge\n[license-url]: https://github.com/iydon/of.yaml/blob/master/LICENSE.txt\n',
    'author': 'Iydon Liang',
    'author_email': 'liangiydon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/iydon/of.yaml',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
