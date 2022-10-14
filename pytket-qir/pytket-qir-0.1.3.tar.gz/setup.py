# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytket_qir', 'pytket_qir.gatesets', 'pytket_qir.gatesets.pyqir']

package_data = \
{'': ['*'], 'pytket_qir': ['utils/*']}

install_requires = \
['pyqir-evaluator>=0.6.2,<0.7.0',
 'pyqir-generator>=0.6.2,<0.7.0',
 'pyqir-parser>=0.6.2,<0.7.0',
 'pyqir>=0.6.2,<0.7.0',
 'pytket>=1.3.0rc1,<2.0.0']

entry_points = \
{'console_scripts': ['compile-bc-test-files = '
                     'tests.qir_test_files.compile_bc_test_files:compile_to_bc']}

setup_kwargs = {
    'name': 'pytket-qir',
    'version': '0.1.3',
    'description': 'Python module for interfacing QIR with the Quantinuum pytket library.',
    'long_description': '# pytket-qir\n\n`pytket-qir` is a python package, aimed at interafacing QIR programs with `pytket`.\n\nThe source code can be found in the corresponding GitHub repository.\n\n## Installation\n\n`pytket-qir` is tested against Python 3.8, 3.9 and 3.10.\n\nThe main requirements are:\n\n- `pytket`\n- `pyqir`\n\nStandard local installation using `pip`:\n\n```sh\npip install -U .\n```\n\n`pytket-qir` has been packaged using `poetry`:\n\n```sh\npoetry install\n```\n\n_N.B._: `pytket-qir` is tested against x86_64 platforms since `pyqir` is not available for arm64.\n',
    'author': 'Roland Guichard',
    'author_email': 'roland.guichard@cambridgequantum.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CQCL/pytket-qir',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
