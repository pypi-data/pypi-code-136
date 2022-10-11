# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['src']

package_data = \
{'': ['*']}

install_requires = \
['PyVCF3>=1.0.3,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'negspy>=0.2.24,<0.3.0',
 'pandas>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['create-cohort-vcf = '
                     'src.create_cohort_vcf:create_cohort_vcf']}

setup_kwargs = {
    'name': 'cgap-higlass-data',
    'version': '0.1.3',
    'description': "Data file generation for CGAP's Higlass browsers",
    'long_description': "\n# higlass-data\nPackage that creates data files for CGAP's Higlass browsers\n\n## Installation\n\nMake sure `poetry` is installed on your system. Clone the repository and run `poetry install`\n\n## Run a script\n\n```\n# -i input file path\n# -o output file path\n# -q Shows logs when set to False\npoetry run create-cohort-vcf -i ./PATH/input.vcf -o ./PATH/input.multires.vcf -q False\n\n```\n\n\n",
    'author': 'Alexander Veit',
    'author_email': 'alexander_veit@hms.harvard.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dbmi-bgm/higlass-data',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
