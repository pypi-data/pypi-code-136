# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['abstract_codebase']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'abstract-codebase',
    'version': '0.1.0',
    'description': 'Abstract codebase with utilities to register generic modules.',
    'long_description': '# abstract-codebase\n\n![PyPI](https://img.shields.io/pypi/v/abstract-codebase)\n![PyPI](https://img.shields.io/pypi/pyversions/abstract-codebase)\n![PyPI](https://img.shields.io/github/license/aidd-msca/abstract-codebase)\n\nAn abstract codebase with utilities for registering generic modules with an optional configuration setup and accreditation system.\n\n## Installation\n\nThe codebase can be installed from PyPI using `pip`, or your package manager of choice, with\n\n```bash\n$ pip install abstract-codebase\n```\n\n## Dependencies\n\nNo dependencies to use the minimal Registry functionality. The configuration setup depends on yaml and hydra.\n\n## Usage\n\n### RegistryFactory \nThe codebase provides a way to register generic modules into a codebase. \nFirst a specific Registry is created, e.g. for deep learning models. \n\n``` Python\nfrom abstract_codebase.registration import RegistryFactory\n\nclass ModelRegistry(RegistryFactory):\n    pass\n```\n\nNext, any models can be added to the ModelRegistry as such.\n\n``` Python\nimport torch.nn as nn\n\n@ModelRegistry.register(call_name="simple_model")\nclass SimpleModel(nn.Module):\n\n    def __init__(self, layer_sizes) -> None:\n        super(SimpleModel, self).__init__()\n        dropout_rate = 0.25\n        self.layers = nn.ModuleList()\n        for layer in range(len(layer_sizes)-2):\n            self.layers.append(\n                nn.Sequential(\n                    nn.Linear(hidden_layers[layer], hidden_layers[layer+1]),\n                    nn.ReLU(),\n                    nn.Dropout(p=dropout_rate)\n                )\n            )\n        self.layers.append(\n            nn.Sequential(\n                nn.Linear(hidden_layers[-2], hidden_layers[-1])\n            )\n        )\n\n    def forward(self, x):\n        for layer in self.layers:\n            x = layer(x)\n        return x\n\n```\n\n### Configurations\nEach registered module can be accompanied with a dataclass of settings with default values. \n\n``` Python\n\n@ModelRegistry.register(call_name="simple_model")  \n@dataclass(unsafe_hash=True)\nclass SimpleModelArguments():\n\n    dropout_rate = 0.25\n```\n\nAs such, the model can rather be defined as.\n\n``` Python\n\n@ModelRegistry.register(call_name="simple_mlp")\nclass SimpleModel(nn.Module):\n\n    def __init__(self, layer_sizes, args: SimpleModelArguments) -> None:\n        super(SimpleMLP, self).__init__()\n        dropout_rate = args.dropout_rate\n        ...\n\n```\n\nFurther, the Config class can be used to read and update configurations across all modules, through yaml files or the command line interface.\n### Accreditation\nAt registration of a module, additional information can be supplied such as author, credit type and more. \nThis information can be used to collect a summary of the accreditation required for all modules used in a given script. \n\n``` Python\n@ModelRegistry.register(\n    call_name="simple_model",\n    author="Author name",\n    credit_type=CreditType.REFERENCE,\n    additional_information="Reference published work in (link)."\n)\nclass SimpleModel(nn.Module):\n    ...\n```\n\nTODO exemplify an accreditation summery.\n``` Python\nModelRegistry.get_accreditation()\n```\n\n## Code of Conduct\n\nEveryone interacting in the codebase, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).\n\n ',
    'author': 'Peter Hartog',
    'author_email': 'peter.hartog@hotmail.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aidd-msca/abstract-codebase',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
