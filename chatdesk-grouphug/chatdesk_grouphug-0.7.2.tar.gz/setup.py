# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grouphug', 'grouphug.heads']

package_data = \
{'': ['*']}

install_requires = \
['Unidecode>=1.3.4,<2.0.0',
 'datasets>=2.0.0,<3.0.0',
 'demoji>=1.1.0,<2.0.0',
 'numpy>=1.21,<2.0',
 'regex>=2022.3.15,<2023.0.0',
 'sentencepiece>=0.1.96,<0.2.0',
 'torch>=1.10.0,<2.0.0',
 'transformers>=4.19.0,<5.0.0']

setup_kwargs = {
    'name': 'chatdesk-grouphug',
    'version': '0.7.2',
    'description': 'GroupHug is a library with extensions to 🤗 transformers for multitask language modelling.',
    'long_description': '\n# grouphug\n\nGroupHug is a library with extensions to 🤗 transformers for multitask language modelling.\nIn addition, it contains utilities that ease data preparation, training, and inference.\n\n## Overview\n\nThe package is optimized for training a single language model to make quick and robust predictions for a wide variety of related tasks at once,\n as well as to investigate the regularizing effect of training a language modelling task at the same time.\n\nYou can train on multiple datasets, with each dataset containing an arbitrary subset of your tasks. Supported tasks include: \n\n* A single language modelling task (Masked language modelling, Masked token detection, Causal language modelling).\n  * The default collator included handles most preprocessing for these heads automatically.\n* Any number of classification tasks, including single- and multi-label classification and regression\n  * A utility function that automatically creates a classification head from your data. \n  * Additional options such as hidden layer size, additional input variables, and class weights.\n* You can also define your own model heads.\n\n## Quick Start\n\nThe project is based on Python 3.8+ and PyTorch 1.10+. To install it, simply use:\n\n`pip install grouphug`\n\n### Documentation\n\nDocumentation can be generated from docstrings using `make html` in the `docs` directory, but this is not yet on a hosted site. \n\n### Example usage\n\n```python\nimport pandas as pd\nfrom datasets import load_dataset\nfrom transformers import AutoTokenizer\n\nfrom grouphug import AutoMultiTaskModel, ClassificationHeadConfig, DatasetFormatter, LMHeadConfig, MultiTaskTrainer\n\n# load some data. \'label\' gets renamed in huggingface, so is better avoided as a feature name.\ntask_one = load_dataset("tweet_eval",\'emoji\').rename_column("label", "tweet_label")\nboth_tasks = pd.DataFrame({"text": ["yay :)", "booo!"], "sentiment": ["pos", "neg"], "tweet_label": [0,14]})\n\n# create a tokenizer\nbase_model = "prajjwal1/bert-tiny"\ntokenizer = AutoTokenizer.from_pretrained(base_model)\n\n# preprocess your data: tokenization, preparing class variables\nformatter = DatasetFormatter().tokenize().encode("sentiment")\n# data converted to a DatasetCollection: essentially a dict of DatasetDict\ndata = formatter.apply({"one": task_one, "both": both_tasks}, tokenizer=tokenizer, test_size=0.05)\n\n# define which model heads you would like\nhead_configs = [\n    LMHeadConfig(weight=0.1),  # default is BERT-style masked language modelling\n    ClassificationHeadConfig.from_data(data, "sentiment"),  # detects dimensions and type\n    ClassificationHeadConfig.from_data(data, "tweet_label"),  # detects dimensions and type\n]\n# create the model, optionally saving the tokenizer and formatter along with it\nmodel = AutoMultiTaskModel.from_pretrained(base_model, head_configs, formatter=formatter, tokenizer=tokenizer)\n# create the trainer\ntrainer = MultiTaskTrainer(\n    model=model,\n    tokenizer=tokenizer,\n    train_data=data[:, "train"],\n    eval_data=data[["one"], "test"],\n    eval_heads={"one": ["tweet_label"]},  # limit evaluation to one classification task\n)\ntrainer.train()\n```\n\n### Tutorials\n\nSee [examples](./examples) for a few notebooks that demonstrate the key features.\n\n## Supported Models\n\nThe package has support for the following base models:\n\n* Bert, DistilBert, Roberta/DistilRoberta, XLM-Roberta \n* Deberta/DebertaV2\n* Electra\n* OPT\n\nExtending it to support other models is possible by simply inheriting from `_BaseMultiTaskModel`, although language modelling head weights may not always load. \n\n## Limitations\n\n* The package only supports PyTorch, and will not work with other frameworks. There are no plans to change this.\n* Grouphug was developed and tested with 🤗 transformers 4.19.x. We will aim to test and keep compatibility with the latest version, but it is still recommended to lock the latest working versions. \n* It has only been tested on training and inference on a single GPU, and some wrappers in the training code may not be completely happy when moving to multi-GPU or TPU environments. Testing on such environments and patches for any bugs found are appreciated.\n* The default used for masked token detection is using random tokens rather than a generator, which appears to be an overly simple task.  We plan to look into an intermediate solution between random tokens and a full generator, and contributions are appreciated.\n\nSee the [contributing page](CONTRIBUTING.md) if you are interested in contributing.\n\n## License\n\ngrouphug was developed by [Chatdesk](http://www.chatdesk.com) and is licensed under the Apache 2 [license](LICENSE).\n\n\n\n\n\n\n',
    'author': 'Sander Land',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chatdesk/grouphug',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
