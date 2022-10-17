# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['segal', 'segal.datasets', 'segal.strategies']

package_data = \
{'': ['*']}

install_requires = \
['albumentations>=1.3.0,<2.0.0',
 'matplotlib>=3.6.0,<4.0.0',
 'scipy>=1.8.0,<2.0.0',
 'segmentation-models-pytorch==0.3.0']

setup_kwargs = {
    'name': 'segal',
    'version': '0.1.2',
    'description': 'SegAL is an active learning freamwork for semantice segmentation.',
    'long_description': '# SegAL\n\n<p align="center">\n  <a href="https://github.com/BrambleXu/segal/actions?query=workflow%3ACI">\n    <img src="https://img.shields.io/github/workflow/status/BrambleXu/segal/CI/main?label=CI&logo=github&style=flat-square" alt="CI Status" >\n  </a>\n  <a href="https://python-poetry.org/">\n    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png" alt="Poetry">\n  </a>\n  <a href="https://github.com/ambv/black">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">\n  </a>\n  <a href="https://github.com/pre-commit/pre-commit">\n    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">\n  </a>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/segal/">\n    <img src="https://img.shields.io/pypi/v/segal.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">\n  </a>\n  <img src="https://img.shields.io/pypi/pyversions/segal.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">\n  <img src="https://img.shields.io/pypi/l/segal.svg?style=flat-square" alt="License">\n</p>\n\nSegAL is an active learning freamwork for semantice segmentation.\n\n## Installation\n\nSegAL is available on PyPI:\n\n`pip install segal`\n\nSegAL officially supports Python 3.8.\n\n## Active Learning Cycle\n\nTo understand what SegAL can do, we first introduce the pool-based active learning cycle.\n\n![al_cycle](./docs/images/al_cycle.png)\n\n- Step 0: Prepare seed data (a small number of labeled data used for training)\n- Step 1: Train the model with seed data\n  - Step 2: Predict unlabeled data with the trained model\n  - Step 3: Query informative samples based on predictions\n  - Step 4: Annotator (Oracle) annotate the selected samples\n  - Step 5: Input the new labeled samples to labeled dataset\n  - Step 6: Retrain model\n- Repeat step2~step6 until the f1 score of the model beyond the threshold or annotation budget is no left\n\nSegAL can simulate the whole active learning cycle.\n\n## Usage\n\nThe user can execute the below command to run the active learning cycle.\n\n```\npython examples/run_al_cycle.py --dataset CamVid  --data_path ./data/CamVid/ --model_name Unet --encoder resnet34 --encoder_weights imagenet --num_classes 12 --strategy LeastConfidence --seed_ratio 0.02 --query_ratio 0.02 --n_epoch 1\n```\n\n- `dataset`: which dataset to use\n- `data_path`: the path where the data store\n- `model_name`: name of segmentation model. More model names can be found in [architectures](https://github.com/qubvel/segmentation_models.pytorch#architectures-)\n- `encoder`: name of encoder used in model. More encoder names can be found in [encoders](https://github.com/qubvel/segmentation_models.pytorch#encoders-)\n- `encoder_weights`: pretrained weights. See [encoder table](https://github.com/qubvel/segmentation_models.pytorch#encoders-) with available weights for each encoder\n- `num_classes`: number of classes\n- `strategy`: name of sampling strategy. Available strategies: `RandomSampling`, `LeastConfidence`, `MarginSampling`, `EntropySampling`. You can find the papers for these strategy in [here](https://github.com/cure-lab/deep-active-learning/tree/main#deep-active-learning-strategies)\n- `seed_ratio`: percentage of seed data. The  used for initial training. \n- `query_ratio`: percentage of queried data in each round\n- `n_epoch`: number of epoch in each round\n\nMore explanation can be found in [usage](./docs/usage.md)\n',
    'author': 'Xu Liang',
    'author_email': 'liangxu006@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tech-sketch/SegAL',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
