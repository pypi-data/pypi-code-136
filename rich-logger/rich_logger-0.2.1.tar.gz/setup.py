# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich_logger']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.0.0', 'rich>=10.11.0']

entry_points = \
{'spacy_loggers': ['rich-logger = rich_logger.spacy:rich_logger']}

setup_kwargs = {
    'name': 'rich-logger',
    'version': '0.2.1',
    'description': 'Table logger using Rich',
    'long_description': '![tests](https://github.com/percevalw/rich-logger/actions/workflows/tests.yml/badge.svg)\n[![pypi](https://badge.fury.io/py/rich-logger.svg)](https://pypi.org/project/rich-logger)\n\n# rich-logger\nTable logger using Rich, aimed at Pytorch Lightning logging\n\n## Features\n\n- display your training logs with pretty [rich](https://github.com/willmcgugan/rich) tables\n- describe your fields with `goal` ("higher_is_better" or "lower_is_better"), `format` and `name`\n- a field descriptor can be matched with any regex\n- a field name can be computed as a regex substitution\n- works in Jupyter notebooks as well as in a command line\n- integrates easily with [Pytorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning)\n\n## Demo\n```python\nfrom rich_logger import RichTablePrinter\nimport time\nimport random\nfrom tqdm import trange\n\nlogger_fields = {\n    "step": {},\n    "(.*)_precision": {\n        "goal": "higher_is_better",\n        "format": "{:.4f}",\n        "name": r"\\1_p",\n    },\n    "(.*)_recall": {\n        "goal": "higher_is_better",\n        "format": "{:.4f}",\n        "name": r"\\1_r",\n    },\n    "duration": {"format": "{:.1f}", "name": "dur(s)"},\n}\n\n\ndef optimization():\n    printer = RichTablePrinter(key="step", fields=logger_fields)\n    printer.hijack_tqdm()\n\n    t = time.time()\n    for i in trange(10):\n        time.sleep(random.random() / 3)\n        printer.log(\n            {\n                "step": i,\n                "task_precision": i / 10.0 if i < 5 else 0.5 - (i - 5) / 10.0,\n            }\n        )\n        time.sleep(random.random() / 3)\n        printer.log(\n            {\n                "step": i,\n                "task_recall": 0.0 if i < 3 else (i - 3) / 10.0,\n                "duration": time.time() - t,\n            }\n        )\n        printer.log({"test": i})\n        t = time.time()\n        for j in trange(5):\n            time.sleep(random.random() / 10)\n\n    printer.finalize()\n\n\noptimization()\n```\n![Demo](demo.gif)\n\n## Use it with PytorchLightning\n```python\nfrom rich_logger import RichTableLogger\n\ntrainer = pl.Trainer(..., logger=[RichTableLogger(key="epoch", fields=logger_fields)])\n```\n',
    'author': 'Perceval Wajsbürt',
    'author_email': 'perceval.wajsburt@sorbonne-universite.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
