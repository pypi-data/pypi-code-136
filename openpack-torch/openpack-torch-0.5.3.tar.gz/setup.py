# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openpack_torch',
 'openpack_torch.configs',
 'openpack_torch.data',
 'openpack_torch.models',
 'openpack_torch.models.imu',
 'openpack_torch.models.keypoint',
 'openpack_torch.utils']

package_data = \
{'': ['*']}

install_requires = \
['hydra-core>=1.2.0,<2.0.0',
 'numpy<1.22.0',
 'omegaconf>=2.2.1,<3.0.0',
 'openpack-toolkit>=0.6.3,<0.7.0',
 'pandas>=1.2.4,<2.0.0',
 'pytorch-lightning>=1.6.3,<2.0.0',
 'sklearn>=0.0',
 'torch>=1.9.0,<2.0.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'openpack-torch',
    'version': '0.5.3',
    'description': 'PyTorch extention to work around with OpenPack dataset',
    'long_description': '# openpack-torch\n\n[![Test](https://github.com/open-pack/openpack-torch/actions/workflows/test.yaml/badge.svg)](https://github.com/open-pack/openpack-torch/actions/workflows/test.yaml)\n[![GitHub Pages](https://github.com/open-pack/openpack-torch/actions/workflows/deploy-docs.yaml/badge.svg)](https://github.com/open-pack/openpack-torch/actions/workflows/deploy-docs.yaml)\n\nPyTorch utilities to work around with [OpenPack Dataset](https://open-pack.github.io/).\n\n## Setup\n\nYou can install via pip with the following command.\n\n```bash\n# Pip\npip install openpack-torch\n\n# Poetry\npoetry add  openpack-torch\n```\n\n## Docs\n\n- [Dataset Page](https://open-pack.github.io/)\n- [API Docs](https://open-pack.github.io/openpack-torch/openpack_torch)\n- [PyPI - openpack-torch](https://pypi.org/project/openpack-torch/)\n\n## Examples\n\n### Operation Recognition (Semantic Segmentation)\n\n#### IMU\n\n- Acceleration\n  - [U-Net](./examples/unet/)\n  - [DeepConvLSTM](./examples/deep-conv-lstm/)\n\n#### Vision\n\n- Keypoints\n  - [ST-GCN](./examples/st-gcn)\n\n#### Scores of Baseline Moodel (Preliminary Experiments)\n\n##### Split: Pilot Challenge\n\n| Model                    | F1 (Test Set) | F1 (Submission Set) | Date       | Code |\n|--------------------------|---------------|---------------------|------------|------|\n| UNet                     | 0.3451        | 0.3747              | 2022-06-28 | [main.py](./examples/unet/main.py) |\n| DeepConvLSTM             | 0.7081        | 0.7695              | 2022-06-28 | [main.py](./examples/deep-conv-lstm/main.py) |\n| ST-GCN                   | 0.7024        | 0.6106              | 2022-07-07 | [main.py](./examples/st-gcn/main.py) |\n\nNOTE: F1 = F1-measure (macro average)\n\n##### Split: OpenPack Challenge 2022\n\nThis split is defined for OpenPack Challenge 2022.\n\n| Model                    | F1 (Test Set) | F1 (Submission Set) | Date       | Code |\n|--------------------------|---------------|---------------------|------------|------|\n| UNet                     | TBA           | TBA                 | -          | -    |\n| DeepConvLSTM             | TBA           | TBA                 | -          | -    |\n| ST-GCN                   | TBA           | TBA                 | -          | -    |\n\n## OpenPack Challenge 2022 @ PerCom2023 WS Bird\n\nWe are hosting an activity recognition competition, using the OpenPack dataset at a [PerCom 2023 Workshop](https://bio-navigation.jp/bird2023/)!\nThe task is very simple: Recognize 10 work operations from the OpenPack dataset.\nPlease join this exciting opportunity. For more information about the competition, click [here](https://open-pack.github.io/challenge2022).\n\n### Tutorials\n\n- [Train a baseline model and make submission file.](./examples/unet/notebooks/U-Net_Train-Model-and-Make-Submission-File.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-pack/openpack-torch/blob/main/examples/unet/notebooks/U-Net_Train-Model-and-Make-Submission-File.ipynb)\n- Change input modalities. (coming soon ...)\n\n![OpenPack Challenge Logo](./assets/img/OpenPackCHALLENG-black.png)\n\n## LICENCE\n\nThis software (openpack-torch) is distributed under [MIT Licence](./LICENSE).\nFor the license of "OpenPack Dataset", please check [this site (https://open-pack.github.io/)](https://open-pack.github.io/).\n',
    'author': 'Yoshimura Naoya',
    'author_email': 'yoshimura.naoya@ist.osaka-u.ac.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://open-pack.github.io/home',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.11,<3.10',
}


setup(**setup_kwargs)
