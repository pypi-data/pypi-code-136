# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['owl_builder',
 'owl_builder.autorels',
 'owl_builder.autorels.bp',
 'owl_builder.autorels.svc',
 'owl_builder.autorels.tests',
 'owl_builder.autosyns',
 'owl_builder.autosyns.bp',
 'owl_builder.autosyns.dmo',
 'owl_builder.autosyns.dto',
 'owl_builder.autosyns.svc',
 'owl_builder.autosyns.tests',
 'owl_builder.autotaxo',
 'owl_builder.autotaxo.bp',
 'owl_builder.autotaxo.dmo',
 'owl_builder.autotaxo.dto',
 'owl_builder.autotaxo.svc',
 'owl_builder.autotaxo.tests',
 'owl_builder.buildr',
 'owl_builder.buildr.bp',
 'owl_builder.buildr.dmo',
 'owl_builder.buildr.svc',
 'owl_builder.buildr.tests']

package_data = \
{'': ['*']}

install_requires = \
['baseblock',
 'nltk>=3.7,<4.0',
 'openai>=0.20.0,<0.21.0',
 'pandas>=1.4.0,<2.0.0',
 'rdflib>=6.1.1,<7.0.0',
 'regex==2022.7.9',
 'spacy==3.3',
 'tabulate',
 'textacy==0.12.0',
 'textblob>=0.17.1,<0.18.0']

setup_kwargs = {
    'name': 'owl-builder',
    'version': '0.1.10',
    'description': 'Tools for Automating the Construction of an Ontology (OWL)',
    'long_description': '# Ontology Builder (owl-builder)\n\n##\n\n## Key Term Extraction\n```python\nfrom owl_builder import keyterms\n\ninput_text = """\nA local area network (LAN) is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building.\n\nBy contrast, a wide area network (WAN) not only covers a larger geographic distance, but also generally involves leased telecommunication circuits.\n\nEthernet and Wi-Fi are the two most common technologies in use for local area networks.\n\nHistorical network technologies include ARCNET, Token Ring, and AppleTalk.\n"""\n\nresults = keyterms(\n    input_text=input_text,\n    use_terms=True,\n    use_keyterms=True,\n    use_ngrams=False,\n    use_nounchunks=False)\n```\n\nThe results are\n```json\n[\n   "leased telecommunication circuit",\n   "historical network technology",\n   "large geographic distance",\n   "interconnects computer",\n   "local area network",\n   "university campus",\n   "common technology",\n   "wide area network",\n   "computer network",\n   "office building",\n   "include arcnet",\n   "limited area",\n   "token ring"\n]\n```',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/owl-builder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
