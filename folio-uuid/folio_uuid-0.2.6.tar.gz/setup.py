# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['folio_uuid', 'folio_uuid.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'folio-uuid',
    'version': '0.2.6',
    'description': 'A library for generating predictive uuids for FOLIO data migrations',
    'long_description': '# folio_uuid\nA python module for creating deterministic UUIDs (UUID v5) outside of FOLIO when migrating data.\n\n# Installation\nThe module is uploaded to pypi. Just do    \n\n\tpip install folio-uuid\n\t\nor   \n\n\tpipenv install folio-uuid      \n\n# Overview\nThe UUIDs (v5) are contstructed in the following way:\n* The namespace is the same for all "Folio UUIDs": **8405ae4d-b315-42e1-918a-d1919900cf3f**\n* The name is contstructed by the following parts, delimited by a colon (**:**)\n\t* **OKAPI_URL** This should be the full OKAPI Url including https. **Example:** *https://okapi-bugfest-juniper.folio.ebsco.com*\n\t* **OBJECT_TYPE_NAME** This should be the name of the type of object that the ID is generated for. In plural. the *file folio_namespaces.py* in this repo has a complete list of the ones currently in use. **Example:** *items*\n\t* **LEGACY_IDENTIFIER** This should be the legacy identifier comming from the source system. The library will perform some normalization* of the identifier if it is a Sierra/Millennium identifier. **Example:** *i3696836*\n\n\\* The normalization strips away any dots (.), check digits and campus codes from the identifiers\n\n# Tests/Examples\n* The namespace is *8405ae4d-b315-42e1-918a-d1919900cf3f*\n* The name, constructed as *OKAPI_URL:OBJECT_TYPE_NAME:LEGACY_IDENTIFIER* would become  *https://okapi-bugfest-juniper.folio.ebsco.com:items:i3696836*\n* The resulting UUID then becomes *9647225d-d8e9-530d-b8cc-52a53be14e26*\n\n# Bash/linux example\n![image](https://user-images.githubusercontent.com/1894384/141293255-a692c61f-4b80-4748-8187-b8bdabe9befa.png)\n\n\tuuidgen --sha1 -n 8405ae4d-b315-42e1-918a-d1919900cf3f -N https://okapi-bugfest-juniper.folio.ebsco.com:items:i3696836\nTo install uuidgen on a apt-enabled Linux distribution, use   \n\n\tsudo apt-get install uuid-runtime\n\n# Python Example\n\tdef test_deterministic_uuid_generation_holdings():\n\t    deterministic_uuid = FolioUUID(\n\t\t"https://okapi-bugfest-juniper.folio.ebsco.com",\n\t\tFOLIONamespaces.holdings,\n\t\t"000000167",\n\t    )\n\t    assert "a0b4c8a2-01fd-50fd-8158-81bd551412a0" == str(deterministic_uuid)\n\t    \n\t    \n# References\nWikipedia has an [article on UUID version 5](https://en.wikipedia.org/wiki/Universally_unique_identifier#Versions_3_and_5_(namespace_name-based))\n\nThere are many browser-based tools to create singe UUIDs v5. [UUIDTools](https://www.uuidtools.com/v5) is one of them.\n',
    'author': 'Theodor Tolstoy',
    'author_email': 'github.teddes@tolstoy.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FOLIO-FSE/folio_uuid',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
