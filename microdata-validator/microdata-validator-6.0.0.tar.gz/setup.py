# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['microdata_validator',
 'microdata_validator.components',
 'microdata_validator.components.unit_type_variables',
 'microdata_validator.exceptions',
 'microdata_validator.repository',
 'microdata_validator.schema',
 'microdata_validator.steps']

package_data = \
{'': ['*']}

install_requires = \
['jsonschema>=4.2.1,<5.0.0']

setup_kwargs = {
    'name': 'microdata-validator',
    'version': '6.0.0',
    'description': 'Python package for validating datasets in the microdata platform',
    'long_description': '# microdata-validator\n\nPython package for validating datasets in the microdata platform.\n\n\n### **Dataset description**\nA dataset as defined in microdata consists of one data file, and one metadata file.\n\nThe data file is a csv file seperated by semicolons. A valid example would be:\n```csv\n000000000000001;123;2020-01-01;2020-12-31;\n000000000000002;123;2020-01-01;2020-12-31;\n000000000000003;123;2020-01-01;2020-12-31;\n000000000000004;123;2020-01-01;2020-12-31;\n```\nRead more about the data format and columns in [the documentation](/docs).\n\nThe metadata files should be in json format. The requirements for the metadata is best described through the [json schema](/microdata_validator/schema/dataset_metadata_schema.json), [the examples](/docs/examples), and [the documentation](/docs).\n\n### **Basic usage**\n\nOnce you have your metadata and data files ready to go, they should be named and stored like this:\n```\nmy-input-directory/\n    MY_DATASET_NAME/\n        MY_DATASET_NAME.csv\n        MY_DATASET_NAME.json\n```\nNote that the filename only allows upper case letters A-Z, number 0-9 and underscores.\n\n\nThen use pip to install microdata-validator:\n```\npip install microdata-validator\n```\n\nImport microdata-validator in your script and validate your files:\n```py\nfrom microdata_validator import validate\n\nvalidation_errors = validate(\n    "MY_DATASET_NAME",\n    input_directory="path/to/my-input-directory"\n)\n\nif not validation_errors:\n    print("My dataset is valid")\nelse:\n    print("Dataset is invalid :(")\n    # You can print your errors like this:\n    for error in validation_errors:\n        print(error)\n```\n\n For a more in-depth explanation of usage visit [the usage documentation](/docs/USAGE.md).\n\n',
    'author': 'microdata-developers',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/statisticsnorway/microdata-validator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
