# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['crc']
entry_points = \
{'console_scripts': ['crc = crc:main']}

setup_kwargs = {
    'name': 'crc',
    'version': '1.3.0',
    'description': 'Library and CLI to calculate and verify all kinds of CRC checksums',
    'long_description': '# Summary\n\nLibrary and CLI tool for calculating and verifying CRC checksums.\n\n[![CI](https://github.com/Nicoretti/crc/actions/workflows/ci.yml/badge.svg)](https://github.com/Nicoretti/crc/actions/workflows/unit.yaml)\n[![coveralls](https://coveralls.io/repos/github/Nicoretti/crc/badge.svg?branch=master)](https://coveralls.io/github/Nicoretti/crc)\n[![python](https://img.shields.io/pypi/pyversions/crc)](https://pypi.org/project/crc/)\n[![pypi](https://img.shields.io/pypi/v/crc)](https://pypi.org/project/crc/)\n[![downloads](https://img.shields.io/pypi/dm/crc)](https://pypi.org/project/crc/)\n[![license](https://img.shields.io/pypi/l/crc)](https://opensource.org/licenses/BSD-2-Clause)\n\n## Provided Default Configuration(s) of CRC Algorithms:\n\n| CRC8 | CRC16 | CRC32 | CRC64 |\n|------|-------|-------|-------|\n| CCITT | CCITT | CRC32 | CRC64 |\n| AUTOSAR | GSM | AUTOSAR | |\n| SAJ1850 | PROFIBUS | BZIP2 | |\n| BLUETOOTH | | POSIX | |\n| MAXIM-DOW | | | | |\n\n## Requirements\n* Python 3.7 and newer\n\n## Examples\n\n### Calculate crc using the `CrcCalculator`\n```python\nfrom crc import CrcCalculator, Crc8\ndata = bytes([0, 1, 2, 3, 4, 5 ])\nexpected_checksum = 0xBC\ncrc_calculator = CrcCalculator(Crc8.CCITT)\n\nchecksum = crc_calculator.calculate_checksum(data)\n\nassert checksum == expected_checksum\nassert crc_calculator.verify_checksum(data, expected_checksum)\n```\n\n### Speed up the calculation by using a table based `CrcCalculator`\n```python\nfrom crc import CrcCalculator, Crc8\n\ndata = bytes([0, 1, 2, 3, 4, 5 ])\nexpected_checksum = 0xBC\nuse_table = True\ncrc_calculator = CrcCalculator(Crc8.CCITT, use_table)\n\nchecksum = crc_calculator.calculate_checksum(data)\n\nassert checksum == expected_checksum\nassert crc_calculator.verify_checksum(data, expected_checksum)\n```\n\n### Create a custom crc configuration for the crc calculation \n```python\nfrom crc import CrcCalculator, Configuration\n\ndata = bytes([0, 1, 2, 3, 4, 5 ])\nexpected_checksum = 0xBC\n\nwidth = 8\npoly=0x07\ninit_value=0x00\nfinal_xor_value=0x00\nreverse_input=False\nreverse_output=False\n\nconfiguration = Configuration(width, poly, init_value, final_xor_value, reverse_input, reverse_output)\n\nuse_table = True\ncrc_calculator = CrcCalculator(configuration, use_table)\n\nchecksum = crc_calculator.calculate_checksum(data)\nassert checksum == expected_checksum\nassert crc_calculator.verify_checksum(data, expected_checksum)\n```\n\n### Use bare bones crc registers\n```python\nfrom crc import Crc8, TableBasedCrcRegister, CrcRegister\n\ndata = bytes([0, 1, 2, 3, 4, 5 ])\nexpected_checksum = 0xBC\n\nreg = CrcRegister(Crc8.CCITT)\ntable_reg = TableBasedCrcRegister(Crc8.CCITT)\n\nreg.init()\nreg.update(data)\nassert expected_checksum == reg.digest()\n\ntable_reg.init()\ntable_reg.update(data)\nassert expected_checksum == table_reg.digest()\n```\n\n## Command line tool\nSee `crc --help`\n\n### subcommand(s)\n#### table\nSubcommand to pre-compute crc lookup tables. See also `crc table --help`.\n#### checksum\nSubcommand to calculate crc checksums of input file(s). See also `crc checksum --help`.\n\nReferences & Resources\n-----------------------\n* [A Painless guide to crc error detection algorithms](http://www.zlib.net/crc_v3.txt)\n* [Project on Github](https://github.com/Nicoretti/crc)\n* [CRC-Catalogue](http://reveng.sourceforge.net/crc-catalogue/all.htm)\n\n',
    'author': 'Nicola Coretti',
    'author_email': 'nico.coretti@gmail.com',
    'maintainer': 'Nicola Coretti',
    'maintainer_email': 'nico.coretti@gmail.com',
    'url': 'https://github.com/Nicoretti/crc',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
