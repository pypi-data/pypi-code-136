# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ttc', 'ttc.chatbot', 'ttc.cli']

package_data = \
{'': ['*']}

install_requires = \
['contractions>=0.1.72,<0.2.0',
 'inquirerpy>=0.3.4,<0.4.0',
 'nltk>=3.7,<4.0',
 'typer>=0.6.1,<0.7.0',
 'yaspin>=2.2.0,<3.0.0']

entry_points = \
{'console_scripts': ['ttc = ttc.cli.main:app']}

setup_kwargs = {
    'name': 'thomasthechatbot',
    'version': '1.0.2',
    'description': 'A Python chatbot that learns as you speak to it.',
    'long_description': '<div align="center">\n    <img src="https://i.imgur.com/hA9YF2s.png" alt="Thomas" width="220" height="220">\n    <h1>Thomas the Chatbot</h1>\n</div>\n\n![Demo](https://i.imgur.com/Jet4UGh.gif)\n\n# Installation\n\n**Python 3.9+ is required**\n\nThis package can be installed from [PyPi](https://pypi.org/project/thomasthechatbot/) with:\n\n```\npip install thomasthechatbot\n```\n\n# Usage\n\n## Basic Usage\n\n```py\nfrom ttc import Chatbot, Context, download_nltk_data\n\n# Only needs to be run once (can be removed after first run)\ndownload_nltk_data()\n\n# Creating the context\nctx = Context()\n\n# Initializing the chatbot\nchatbot = Chatbot()\n\ntalk = True\n\nwhile talk:\n    msg = input("You: ")\n\n    if msg == "s":\n        talk = False\n    else:\n        # Getting the response\n        resp = chatbot.respond(ctx, msg)\n\n        # Saving the response to the context\n        ctx.save_resp(resp)\n\n        print(f"Thomas: {resp}")\n\n# Saving the chatbot data\nchatbot.save_data()\n```\n\n## Configurations\n\n```py\nchatbot = Chatbot(\n    path="brain",\n    learn=False,\n    min_score=0.5,\n    score_threshold=0.5,\n    mesh_association=0.5,\n)\n```\n\n## CLI\n\nType `ttc` to begin talking to Thomas.\n\n# How does Thomas work?\n\nThomas has no hard-coded responses and is designed to “learn” as he is spoken to.\n\nNote: I created this approach based on my intuition and not a proven method.\n\n## Data Storage\n\nThomas does not come up with his own responses, he reiterates those that he has seen before.\n\n### Responses\n\nPrevious responses are stored in `resps.json` as a dictionary where the key is a generated [UUID](https://docs.python.org/3/library/uuid.html) and the value is the tokenized response.\n\n### Mesh\n\nPrompts are associated with responses through a "mesh" which is stored in `mesh.thomas`. The mesh consists of a dictionary where the key is the UUID of the prompt and the value is a "link". Links associate responses to patterns of words, they have the following attributes:\n\n`stop_words: set`\nStop words separated from the tokenized prompt.\n\n`keywords: set`\nThe remaining words which are lemmatized by their part of speech.\n\n`resps: dict[str, set]`\nResponses to the prompt where the key is the response UUID and the value is a set of mesh ids from the previous prompt.\n\n## Querying Responses\n\n### Tokenizing Prompts\n\nBefore tokenization, prompts are lowercased, contractions are expanded and punctuation is removed. This aids in improving the consistency and accuracy of queries. Prompts are tokenized by word and split into key words and stop words.\n\n### Ignoring Responses\n\nThe user\'s prompt and chatbot\'s previous response are ignored to prevent the chatbot from appearing repetitive.\n\n### Initial Query\n\nMeshes are initially queried by their score which can be calculated with:\n\n`(ss / 2 + sk) / (ts / 2 + tk - ss / 2 - sk + 1)`\n\n`ss` = shared stop words\n\n`sk` = shared key words\n\n`ts` = total stop words\n\n`tk` = total key words\n\nThis formula weighs shared key words 2 times more heavily than stop words by dividing `ss` and `sk` by 2. It also takes into account the total number of words resulting in more precise meshes being favoured.\n\n### First Discard\n\nMeshes with scores below a threshold (`min_score`) are discarded.\n\n### No Results Queried\n\nIf no results remain, meshes are queried by the number of shared stop words.\n\n### Second Discard\n\nThe remaining meshes are sorted and meshes that fall below a percentage threshold (`score_threshold`) of the best score are discarded. Considering multiple meshes increases the variety of responses.\n\n### Mesh Association\n\nMeshes are associated with each other by the percentage of shared responses (`mesh_association`). Associated meshes for each queried mesh are found and added to the list. This process prevents less trained prompts from having a small response pool.\n\n### Choosing a Response\n\nIf responses are found to share the same previous message UUID as the prompt, all non-sharing responses are moved. Responses are chosen at random from the remaining responses. Random selection prevents the chatbot from being predictable.\n\n# Contributing\n\nOpen to contributions, please create an issue if you want to do so.\n\n# Formatting\n\n[Black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort) and [Prettier](https://prettier.io/) are used for formatting\n',
    'author': 'principle105',
    'author_email': 'principle105@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/principle105/thomasthechatbot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
