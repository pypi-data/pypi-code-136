# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slackbot_helper',
 'slackbot_helper.bp',
 'slackbot_helper.dmo',
 'slackbot_helper.dto',
 'slackbot_helper.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'slack-bolt>=1.14.3,<2.0.0', 'slackclient>=2.9.4,<3.0.0']

setup_kwargs = {
    'name': 'slackbot-helper',
    'version': '0.1.8',
    'description': 'Helper Functions for Slackbots',
    'long_description': '# Slackbot Helper (slackbot-helper)\n\nContains Utility Functions to help deal with Slack Events and I/O\n\n## Usage\nAssume this incoming event:\n```python\nd_incoming = {\n    "blocks": [\n        {\n            "block_id": "vz+U",\n            "elements": [\n                {\n                    "elements": [\n                        {\n                            "type": "user",\n                            "user_id": "U045HCSMG8K"\n                        },\n                        {\n                            "text": " dead ahead!",\n                            "type": "text"\n                        }\n                    ],\n                    "type": "rich_text_section"\n                }\n            ],\n            "type": "rich_text"\n        }\n    ],\n    "channel": "C046DB9TLEL",\n    "team": "T045AR44M70",\n    "text": "<@U045HCSMG8K> dead ahead!",\n    "ts": 1665195085.499959,\n    "type": "app_mention",\n    "user": "U04674UNRBJ"\n}\n```\n\nImport the `normalize_event` function:\n```python\nfrom slackbot_helper import normalize_event\n\nd_normalized = normalize_event(\n    d_event=d_incoming,\n    bot_ids=[\'U045HCSMG8K\']\n)\n```\n\nThe `bot_ids` parameter is a list of all known **bot_ids** in your application.\n\nThe output of this function is:\n```json\n{\n    "membership": "85e8d1eb_46c2_11ed_97a0_4c1d96716627",\n    "analysis": {\n        "commands": [],\n        "meta_mode": "human2bot",\n        "meta_type": "H2B_SINGLE",\n        "text_1": "@U045HCSMG8K dead ahead!",\n        "text_2": "dead ahead!",\n        "user_all": ["U045HCSMG8K"],\n        "user_source": "U04674UNRBJ",\n        "user_target": "U045HCSMG8K"\n    },\n    "event": {\n        "blocks": [\n            {\n                "block_id": "vz+U",\n                "elements": [\n                    {\n                        "elements": [\n                            {\n                                "type": "user",\n                                "user_id": "U045HCSMG8K"\n                            },\n                            {\n                                "text": " dead ahead!",\n                                "type": "text"\n                            }\n                        ],\n                        "type": "rich_text_section"\n                    }\n                ],\n                "type": "rich_text"\n            }\n        ],\n        "channel": "C046DB9TLEL",\n        "team": "T045AR44M70",\n        "text": "<@U045HCSMG8K> dead ahead!",\n        "ts": 1665195085.499959,\n        "type": "app_mention",\n        "user": "U04674UNRBJ"\n    },\n}\n```\n\nThe `analysis` structure within the output contains the following fields of interest:\n1. `commands`: Any Commands extracted from the text\n2. `meta_mode`: The Mode of communication (`human2bot`, `human2human`, `bot2human`, `bot2bot`)\n3. `meta_type`: The Type of communication (`H2B_SINGLE` means Human is addressing a Single bot)\n4. `text_1`: The original text\n5. `text_2`: The normalized text\n6. `user_all`: All the user IDs addressed in the text\n7. `source_user`: The Source User (responsible for sending the event)\n8. `target_user`: The Target User (primary user responsible for receiving the event)\n',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/slackbot-helper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
