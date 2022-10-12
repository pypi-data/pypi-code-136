# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imgmanip',
 'imgmanip.dialogs',
 'imgmanip.functions',
 'imgmanip.functions.tasks',
 'imgmanip.models',
 'imgmanip.widgets',
 'imgmanip.widgets.main',
 'imgmanip.widgets.task_frames']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'PySide6>=6.3.2,<7.0.0',
 'PyYAML>=6.0,<7.0',
 'natsort>=8.2.0,<9.0.0',
 'numpy>=1.23.3,<2.0.0',
 'opencv-python>=4.6.0.66,<5.0.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'pyqtdarktheme>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['imgmanip = imgmanip.main:main']}

setup_kwargs = {
    'name': 'imgmanip',
    'version': '0.0.5',
    'description': 'Image manipulation tool written in python in which you can select a large number of photos and perform a lot of different operations on them.',
    'long_description': "Image manipulation tool in which you can select a large number of photos and\nperform a lot of different operations on them.\n---\n\n## Installation\n\n### Install from PyPI\n\n```shell\npip install imgmanip\n```\n\n#### If you want the program to be displayed in the system applications menu. (Linux only)\n\n```shell\nsudo ln -s $(whereis imgmanip) /usr/bin/imgmanip\ncurl https://raw.githubusercontent.com/hawier-dev/imgmanip/develop/imgmanip.desktop > ./imgmanip.desktop\nsudo mv ./imgmanip.desktop /usr/share/applications/imgmanip.desktop\n```\n\nThe current list of operations\n\n- **Resize** - resizes the images to the given resolution or by a specified percentage.\n- **Compress** - compresses the image. The lower the 'quality',\n  the smaller the file size.\n- **Invert** - inverts the colors of the image.\n- **Flip** - flips the image in horizontal or vertical axis.\n- **Color detection** - marks where the given color appears in the image.\n  Additionally, it can save the **mask** in .png format.\n- **Convert** - converts the image to the other format.\n- **Convert color mode** - This task converts the image color mode to the selected one.",
    'author': 'Mikołaj Badyl',
    'author_email': 'contact@hawier.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
