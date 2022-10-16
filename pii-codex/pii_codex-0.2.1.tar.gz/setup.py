# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pii_codex',
 'pii_codex.models',
 'pii_codex.services',
 'pii_codex.services.adapters',
 'pii_codex.services.adapters.detection_adapters',
 'pii_codex.services.analyzers',
 'pii_codex.utils']

package_data = \
{'': ['*'], 'pii_codex': ['data/v1/*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0',
 'pandas>=1.4.4,<2.0.0',
 'pydantic[dotenv]>=1.8.2,<2.0.0']

extras_require = \
{'detections': ['spacy>=3.4.1,<4.0.0', 'presidio-analyzer>=2.2.29,<3.0.0']}

setup_kwargs = {
    'name': 'pii-codex',
    'version': '0.2.1',
    'description': '',
    'long_description': '<p align="center">\n<img src="https://github.com/EdyVision/pii-codex/blob/main/docs/PII_Codex_Logo.png" alt="PII Codex logo" width="300px"/>\n</p>\n<hr/>\n\n# PII Codex - PII Detection, Categorization, and Severity Assessment\n[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)\n![](https://img.shields.io/badge/code%20style-black-000000.svg)\n[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/EdyVision/pii-codex/graphs/commit-activity)\n[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n[![License: Hippocratic 3.0](https://img.shields.io/badge/License-Hippocratic_3.0-green.svg)](https://firstdonoharm.dev)\n[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)\n[![DOI](https://zenodo.org/badge/533554671.svg)](https://zenodo.org/badge/latestdoi/533554671)\n\nThe PII Codex project was built as a core part of an ongoing research effort in Personal Identifiable Information (PII) detection and risk assessment. There was a need to not only detect PII in unstructured text, but also identify its severity, associated categorizations in cybersecurity research and policy documentation, and provide a way for others in similar research efforts to reproduce or extend the research. PII Codex is a combination of systematic research, conceptual frameworks, third-party open source software, and cloud service provider integrations. The categorizations are directly influenced by the research of Milne et al. (2016) while the ranking is a result of category severities on the scale provided by Schwartz and Solove (2012) from Non-Identifiable, Semi-Identifiable, and Identifiable.\n\nThe outputs of the primary PII Codex analysis and adapter functions are AnalysisResult or AnalysisResultSet objects that will provide a listing of detections, severities, mean risk scores for each string processed, and summary statistics on the analysis made. The final outputs do not contain the original texts but instead will provide where to find the detections should the end-user care for this information in their analysis.\n\n<hr/>\n\n## Importing\nThe repository releases are hosted on PyPi.\n\nUsing pip:\n\n```bash\npip3 install -i pii-codex\n```\n\nUsing Poetry:\n\n```bash\npoetry add pii-codex\n```\n\nIf you are in need of the integrated Microsoft Presidio Analyzer, you\'ll also need to install the `en_core_web_lg` and the PII-Codex extras:\n\n```bash\npoetry install pii-codex --extras="detections"\npython3 -m spacy download en_core_web_lg\n```\n\n## Usage\n\n### Sample Input / Output\nThe built-in analyzer uses Microsoft Presidio. Feed in a collection of strings with analyze_collection() or just a single string with analyze_item(). Those analyzing a collection of strings will also be provided with statistics calculated on the risk scores for detected items.\n```python\nfrom pii_codex.services.analysis_service import PIIAnalysisService\nPIIAnalysisService().analyze_collection(\n    texts=["your collection of strings"],\n    language_code="en",\n    collection_name="Data Set Label", # Optional Labeling\n    collection_type="SAMPLE" # Defaults to POPULATION, used stats calculations\n)\n```\n\nYou can also pass in a `data` param (dataframe) instead of simple text array with a text column and a metadata column to be analyzed for those analyzing social media posts. Current metadata supported are `URL`, `LOCATION`, and `SCREEN_NAME`.\n\nSample output (results object converted to `dict` from notebook):\n```\n{\n    "collection_name": "PII Collection 1",\n    "collection_type": "POPULATION",\n    "analyses": [\n        {\n            "analysis": [\n                {\n                    "pii_type_detected": "PERSON",\n                    "risk_level": 3,\n                    "risk_level_definition": "Identifiable",\n                    "cluster_membership_type": "Financial Information",\n                    "hipaa_category": "Protected Health Information",\n                    "dhs_category": "Linkable",\n                    "nist_category": "Directly PII",\n                    "entity_type": "PERSON",\n                    "score": 0.85,\n                    "start": 21,\n                    "end": 24,\n                }\n            ],\n            "index": 0,\n            "risk_score_mean": 3,\n        },\n        ...\n    ],\n    "detection_count": 5,\n    "risk_scores": [3, 2.6666666666666665, 1, 2, 1],\n    "risk_score_mean": 1.9333333333333333,\n    "risk_score_mode": 1,\n    "risk_score_median": 2,\n    "risk_score_standard_deviation": 0.8273115763993905,\n    "risk_score_variance": 0.6844444444444444,\n    "detected_pii_types": [\n        "LOCATION",\n        "EMAIL_ADDRESS",\n        "URL",\n        "PHONE_NUMBER",\n        "PERSON",\n    ],\n    "detected_pii_type_frequencies": {\n        "PERSON": 1,\n        "EMAIL_ADDRESS": 1,\n        "PHONE_NUMBER": 1,\n        "URL": 1,\n        "LOCATION": 1,\n    },\n}\n```\n\n### Docs\nFor more information on usage, check out the respective documentation for guidance on using PII-Codex.\n\n| Topic                       | Document                                                     | Description                                                                              |\n|-----------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------|\n| PII Type Mappings           | [PII Mappings](docs/MAPPING.md)                              | Overview of how to perform mappings between PII types and how to review store PII types. |\n| PII Detections and Analysis | [PII Detection and Analysis](docs/DETECTION_AND_ANALYSIS.md) | Overview of how to detect and analyze strings                                            |\n| Local Repo Setup            | [Local Repo Setup](docs/LOCAL_SETUP.md)                      | Instructions for local repository setup                                                  |\n| Example Analysis            | [Example Analysis Notebook](notebooks/pii-analysis-ms-presidio.ipynb)  | Notebook with example analysis using MSFT Presidio                             |\n\n<hr/>\n\n## Community Guidelines\n### Contributions\nIn general, you can contribute to this project by creating issues. You are also welcome to contribute to the source code directly by forking the project, modifying the code, and creating pull requests. Please use clear and organized descriptions when creating issues and pull requests and leverage the templates when possible.\n\n### Bug Report and Support Requests\nYou can use issues to report bugs and seek support. Before creating any new issues, please check for similar ones in the issue list first.\n\n## Attributions\nThis project benefited greatly from a number of PII research works like that from Milne et al (2016), Schwartz and Solove (2012), and the documentation by NIST, DHS, and HIPAA. A special thanks to all the open source projects, and frameworks that made the setup and structuring of this project much easier like Poetry, Microsoft Presidio, spaCy, Jupyter, and several others.\n',
    'author': 'Eidan J. Rosado',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/EdyVision/pii-codex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
