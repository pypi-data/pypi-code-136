# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlcvzoo_util',
 'mlcvzoo_util.cvat_annotation_handler',
 'mlcvzoo_util.logger',
 'mlcvzoo_util.model_evaluator',
 'mlcvzoo_util.model_timer',
 'mlcvzoo_util.model_trainer',
 'mlcvzoo_util.pre_annotation_tool',
 'mlcvzoo_util.video_image_creator']

package_data = \
{'': ['*']}

install_requires = \
['imageio>=2.9,<3.0',
 'mlcvzoo_base>=4.2,<5.0',
 'mlflow>=1.22,<2.0',
 'nptyping>=2.0,<3.0',
 'numpy>=1.19.2,!=1.19.5',
 'opencv-contrib-python>=4.5,<5.0,!=4.5.5.64',
 'opencv-python>=4.5,<5.0,!=4.5.5.64',
 'related-mltoolbox>=1.0,<2.0',
 'tqdm>=4.61,<5.0',
 'yaml-config-builder>=7.0,<8.0']

extras_require = \
{':python_version < "3.11"': ['backports.strenum>=1.1,<2.0']}

entry_points = \
{'console_scripts': ['mlcvzoo-cvat-handler = '
                     'mlcvzoo_util.cvat_annotation_handler.cvat_annotation_handler:main',
                     'mlcvzoo-modelevaluator = '
                     'mlcvzoo_util.model_evaluator.model_evaluator:main',
                     'mlcvzoo-modeltimer = '
                     'mlcvzoo_util.model_timer.model_timer:main',
                     'mlcvzoo-modeltrainer = '
                     'mlcvzoo_util.model_trainer.model_trainer:main',
                     'mlcvzoo-preannotator = '
                     'mlcvzoo_util.pre_annotation_tool.pre_annotation_tool:main',
                     'mlcvzoo-video-image-creator = '
                     'mlcvzoo_util.video_image_creator.video_image_creator:main']}

setup_kwargs = {
    'name': 'mlcvzoo-util',
    'version': '0.1.0',
    'description': 'MLCVZoo Util Package',
    'long_description': '# MLCVZoo Util\n\nThe MLCVZoo is an SDK for simplifying the usage of various (machine learning driven)\ncomputer vision algorithms. The package **mlcvzoo_util** provides additional utility functions for downstream developments and tools for convenience and CLI usage.\n\nFurther information about the MLCVZoo can be found [here](../README.md).\n\n## Install\n`\npip install mlcvzoo-util\n`\n\n## Technology stack\n\n- Python\n',
    'author': 'Maximilian Otten',
    'author_email': 'maximilian.otten@iml.fraunhofer.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.openlogisticsfoundation.org/silicon-economy/base/ml-toolbox/mlcvzoo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
