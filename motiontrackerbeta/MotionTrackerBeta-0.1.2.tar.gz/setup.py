# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['MotionTrackerBeta',
 'MotionTrackerBeta.classes',
 'MotionTrackerBeta.functions',
 'MotionTrackerBeta.widgets']

package_data = \
{'': ['*'], 'MotionTrackerBeta': ['images/*', 'style/*']}

install_requires = \
['PyQt5>=5.15.2,<6.0.0',
 'cvxopt>=1.3.0,<2.0.0',
 'cvxpy>=1.2.0,<2.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.22.3,<2.0.0',
 'opencv-contrib-python-headless>=4.5.5.64,<5.0.0.0',
 'pandas>=1.4.2,<2.0.0',
 'pynumdiff>=0.1.2,<0.2.0',
 'scipy>=1.9.2,<2.0.0']

entry_points = \
{'console_scripts': ['MotionTrackerBeta = MotionTrackerBeta.main:MotionTracker',
                     'motiontracker = MotionTrackerBeta.main:MotionTracker',
                     'motiontrackerbeta = '
                     'MotionTrackerBeta.main:MotionTracker']}

setup_kwargs = {
    'name': 'motiontrackerbeta',
    'version': '0.1.2',
    'description': 'a GUI based, open-source motion tracking application',
    'long_description': '<p align="center">\n  <img src="https://user-images.githubusercontent.com/65981382/166214135-47ecd327-cba8-47c0-a034-9f6f14b777ce.png" alt="Motion Tracker Beta"/>\n</p>\n\n# Motion Tracker Beta\nAn easy-to-use, standalone and open-source motion tracking application for researchers and engineers, written in Python.\n\n## Features\n- Intutitive graphical user interface\n- Capable of handling the most common video formats\n- Capable of tracking various properties of multiple objects simultaneously\n- Diverse set of built in tracking algorithms, based on the `OpenCV` libary\n- Rich selection of numerical differentiation algorithms powered by the `PyNumDiff` libary\n- Built in plotting an exporting features\n\n\nFor the complete list of features please check the [documentation](https://github.com/flochkristof/motiontracker/blob/main/docs/GUIDE.pdf).\n\n## Dependencies\nThe Graphical user interface was created with the [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) framework. For the handling of video files and to do the actual tracking the [OpenCV](https://opencv.org/) library was used with its built in tracking algorithms. Numerical differentiations are carried out using the [PyNumDiff](https://github.com/florisvb/PyNumDiff). Plots and figures are generated by [matplotlib](https://matplotlib.org/). For the complete list of required packages check [pyproject.toml](https://github.com/flochkristof/motiontracker/blob/main/pyproject.toml) [requirements.txt](https://github.com/flochkristof/motiontracker/blob/main/requirements.txt)\n\n## Installation\n### Download & install via PyPI\n```\n$ pip install MotionTrackerBeta\n```\n- Run the application\n```\n$ MotionTrackerBeta\n```\n### Download & install the wheel file\n- Download the `.whl` file from the latest release\n- Execute\n```\n$ pip install <path-to-wheel-file.whl>\n```\n- Run the application\n```\n$ MotionTrackerBeta\n```\n> Note: If you would like to use Chebysev filters in the post processing of the tracked data, run `$ pip install pychebfun`!\n\n### Download binaries (Windows)\n- Download the binaries from the latest release\n- Extract it to your specified location\n- Open application with `Motion Tracker Beta.exe`\n### Download the installer (Windows)\n- Download the installer from the latest release\n- Run the installer and follow the instructions\n- After successfull installation the software is accessible under the name `Motion Tracker Beta`\n###\n# Usage\nFor a detailed guide about the software check out the [documentation](docs/DOCUMENTATION.pdf).\n# License\nMotion Tracker Beta is released under the `GNU General Public License v3.0`.\n# Author\nThe software was developed by Kristof Floch at the Department of Applied Mechanics, Faculty of Mechanical Engineering, Budapest University of Technology and Economics.\n### Contact\n- E-mail: kristof.floch@gmail.com',
    'author': 'Kristof Floch',
    'author_email': 'kristof.floch@gmail.com',
    'maintainer': 'Kristof Floch',
    'maintainer_email': 'kristof.floch@gmail.com',
    'url': 'https://github.com/flochkristof/motiontracker',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
