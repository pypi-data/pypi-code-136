# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vcfvalidator']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'tabulate>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['vcfvalidator = vcfvalidator.cli:main']}

setup_kwargs = {
    'name': 'vcfvalidator',
    'version': '1.0.1',
    'description': 'This package checks the metadata of VCF files with respect to the following paper: https://f1000research.com/articles/11-231',
    'long_description': '# vcfvalidator\n\nThis package checks the metadata of VCF files with respect to the following paper: https://f1000research.com/articles/11-231\n\n\n### Installing the package:\n\n```\npip install vcfvalidator\n```\n\n### How to use the validator:\n\nThe package installs a CLI tool that can be used to check the VCF metdata with the following command:\n```\n$ vcfvalidator validate-metadata PATH_TO_VCF_FILE\n```\n\nThe VCF file under PATH_TO_VCF_FILE can be either compressed with GZIP (*.vcf.gz) or uncompressed (*.vcf).',
    'author': 'Junaid Memon',
    'author_email': 'jmemonisy@gmail.com',
    'maintainer': 'Patrick König',
    'maintainer_email': 'koenig@ipk-gatersleben.de',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
