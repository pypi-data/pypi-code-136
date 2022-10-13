# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dicomgenerator', 'dicomgenerator.resources']

package_data = \
{'': ['*'], 'dicomgenerator.resources': ['templates/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'factory-boy>=3.2.1,<4.0.0',
 'numpy>=1.23.4,<2.0.0',
 'pydicom>=2.3.0,<3.0.0',
 'pytest-cov>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'dicomgenerator',
    'version': '0.7.1',
    'description': 'Generate pydicom datasets and data elements for use in testing',
    'long_description': '# dicomgenerator\n\n\n[![CI](https://github.com/sjoerdk/dicomgenerator/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/sjoerdk/dicomgenerator/actions/workflows/build.yml?query=branch%3Amaster)\n[![PyPI](https://img.shields.io/pypi/v/dicomgenerator)](https://pypi.org/project/dicomgenerator/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dicomgenerator)](https://pypi.org/project/dicomgenerator/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n\nGenerate pydicom datasets and data elements for use in testing.\n\n* Free software: MIT license\n* Status: Alpha. Tests run but there are loose ends\n\nFeatures\n--------\n* Extends [factory-boy](https://factoryboy.readthedocs.io) factories to produce [pydicom](https://github.com/pydicom/pydicom) Datasets and DicomElements \n* Generate valid DICOM values for person name, time, date, and UID\n* Create json-based editable templates from any dicom file\n* quick_dataset(): single-line pydicom dataset init\n\n## Installation\n\n\nInstall with pip::\n\n    pip install dicomgenerator\n\n\n## Usage\n### Quick dataset\nI have found this quite useful in testing:\n\n```python\n    from dicomgenerator.generators import quick_dataset\n    ds = quick_dataset(PatientName=\'Jane\', StudyDescription=\'Test\')\n\n    # >>> ds.PatientName -> \'Jane\'     \n    # >>> ds.StudyDescription -> \'Test\'\n```\n\n\n### Generating a dataset\nGenerate a realistic CT dataset\n\n```python \n    from dicomgenerator.factory import CTDatasetFactory\n\n    # Generate from template\n    >>> CTDatasetFactory().PatientName -> \'van Haarlem^Anouk\'  #  generated random name\n    >>> CTDatasetFactory().PatientName -> \'Loreal^Casper\'      #  generated random name\n\n    # Overwrite arbitrary DICOM elements\n    ds.CTDatasetFactory(PatientSex=\'M\', PatientName=\'Smith^Harry\')\n    >>> ds.PatientName -> \'Smith^Harry\'\n    >>> ds.PatientSex  -> \'M\'\n\n    # generated UIDs and dates are valid DICOM\n    >>> CTDatasetFactory().StudyTime        -> \'130624.929\'\n    >>> CTDatasetFactory().StudyDate        -> \'20110508\'\n    >>> CTDatasetFactory().StudyInstanceUID -> \'1.2.826.0.1.3680\'\n```\n\n\n## Generating a data element\n\n```python\n    # import\n    from dicomgenerator.factory import DataElementFactory\n\n    # Creating a DICOM data element by name will give a realistic value and correct VR\n    >>> DataElementFactory(tag=\'PatientName\').value -> "van Ooyen^Fiene"\n    >>> DataElementFactory(tag=\'PatientName\').VR -> \'PN\'\n\n    # You can also give DICOM tags as hex\n    >>> DataElementFactory(tag=0x00100010).value -> "Weil^Jack"\n\n    # Dates, times and UIDs all work.\n    >>> DataElementFactory(tag="AcquisitionTime").value   -> \'184146.928\'\n    >>> DataElementFactory(tag="PatientBirthDate").value  -> \'20120511\'\n    >>> DataElementFactory(tag="SeriesInstanceUID").value -> \'1.2.826.0.1.3680\'\n```\n\n### In reproducible tests\nYou can set the random seed in [factory-boy](https://factoryboy.readthedocs.io) like this:\n\n```python\n    from factory import random\n\n    def test_one:\n        """The random patient name in this test will always be the same"""\n        random.reseed_random(\'any string you want\')\n        assert element = DataElementFactory(tag=\'PatientName\').value == "van Ooyen^Fiene"\n```\n\n\n## Credits\n\nThis package was originally created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.\n \n',
    'author': 'sjoerdk',
    'author_email': 'sjoerd.kerkstra@radboudumc.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sjoerdk/dicomgenerator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
