# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['renkubio']

package_data = \
{'': ['*']}

install_requires = \
['questionary>=1.10.0,<2.0.0', 'renku>=1.8.0,<2.0.0']

entry_points = \
{'renku.cli_plugins': ['bio = renkubio.cli:bio']}

setup_kwargs = {
    'name': 'renku-bio',
    'version': '0.2.0',
    'description': 'Renku plugin to annotate projects and datasets metadata with biological samples.',
    'long_description': '# renku-bio\n\nThis plugin extends Renku to easily annotate biological samples in Renku metadata. Samples can be annotated on either the project or dataset metadata (using --dataset).\n\n## Installation\n\nThe development version can be installed as a local Python package by running the following command from the root of the repo:\n\n```sh\npip install -e .\n```\n\nThe stable version is on PyPI and can be installed with pip:\n\n```sh\npip install renku-bio\n```\n\n\n## Usage\n\nA CLI is available with entrypoint `renku bio` the gif belows demonstrates how to use it:\n\n![](assets/demo_renkubio.gif)\n\n<details>\n<summary> <b>[Click to expand]</b> Full command from example above</summary>\n\n```sh\n➜ renku bio add-sample \\\n    --description "Culture of liver cells from an adult mouse" \\\n    --age 2 \\\n    --taxon "Mus musculus" \\\n    --collector "SDSC" \\\n    --gender Male mouse_liver \\\n    --location "Lausanne" \\\n    --date 2022-08-10\n```\n\n</details>\n\nAfter adding the biosample above, the project metadata graph would have the following structure:\n\n![](assets/bio_renku_graph.png)\n\nThe new "BioSample" node was created by `renku bio add-sample`. The information provided for sampling location, collector organization and taxon are enriched using third party APIs. For example, the "Taxon" node now has "scientificName", "taxonRank" and "parentTaxon" in addition to the name provided.\n\n<details>\n<summary> <b>[Click to expand]</b> Compact view of the full biosample metadata</summary>\n\n```json\n[\n        {\n          "@id": "https://renkulab.io/projects/renku-bio/mouse_liver",\n          "@type": "http://bioschemas.org/BioSample",\n          "http://schema.org/dateCreated": "2022-08-10",\n          "http://bioschemas.org/collector": {\n            "@id": "https://ror.org/02hdt9m26",\n            "@type": "http://schema.org/Organization",\n            "http://schema.org/name": "Swiss Data Science Center"\n          },\n          "http://bioschemas.org/isControl": false,\n          "http://bioschemas.org/locationCreated": {\n            "@id": "https://renkulab.io/projects/renku-bio/mouse_liver/loc",\n            "@type": "http://schema.org/Place",\n            "http://schema.org/latitude": 46.5218269,\n            "http://schema.org/longitude": 6.6327025,\n            "http://schema.org/name": "Lausanne, District de Lausanne, Vaud, Schweiz/Suisse/Svizzera/Svizra"\n          },\n          "http://bioschemas.org/samplingAge": 2,\n          "http://bioschemas.org/taxonomicRange": {\n            "@id": "https://renkulab.io/projects/renku-bio/mouse_liver/tax",\n            "@type": "http://bioschemas.org/Taxon",\n            "http://bioschemas.org/parentTaxon": "Mus",\n            "http://bioschemas.org/scientificName": "Mus musculus",\n            "http://bioschemas.org/taxonRank": "species",\n            "http://schema.org/name": "house mouse"\n          },\n          "http://schema.org/description": "Culture of liver cells from an adult mouse",\n          "http://schema.org/gender": "Male",\n          "http://schema.org/name": "mouse_liver"\n        }\n      ]\n```\n\n</details>\n\n## Current state:\n\nChecklist:\n\n* [x] Interactively prompt user to select relevant API result (ROR, EBI, OSM)\n* [x] Use dataset annotations instead of project\n* [x] Use Renku API to fetch metadata instead of CLI + subprocess\n* [x] Change console entrypoint to make into a renku plugin\n* [ ] Add support for experimental assay (potentially with [LabProtocol](https://bioschemas.org/profiles/LabProtocol/0.6-DRAFT-2020_12_08))\n  + [ ] Restructure CLI into renku bio {sample,assay} {add,ls,rm,show}\n* [ ] PoC to query a list of datasets (or projects) based on BioSample annotations.\n',
    'author': 'cmdoret',
    'author_email': 'cyril.mattheydoret@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://renkulab.io/projects/cyril.matthey-doret/renku-bio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
