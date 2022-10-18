# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rai',
 'rai._cli',
 'rai.contours',
 'rai.data',
 'rai.dicom',
 'rai.display',
 'rai.inference',
 'rai.mask',
 'rai.metrics',
 'rai.model',
 'rai.typing',
 'rai.vendor']

package_data = \
{'': ['*'], 'rai.mask': ['test_figures/*']}

install_requires = \
['PyWavelets<1.4.0',
 'click',
 'ipywidgets>=7.6',
 'jupyter-dash',
 'numba',
 'numpy',
 'pandas',
 'plotly>=4',
 'pydicom',
 'raicontours==0.3.0-dev1',
 'scikit-image',
 'scipy',
 'shapely',
 'statsmodels',
 'tqdm']

extras_require = \
{':platform_system != "Windows"': ['tensorflow'],
 ':platform_system == "Windows"': ['tensorflow-intel',
                                   'tensorflow-directml-plugin']}

entry_points = \
{'console_scripts': ['rai = rai.__main__:cli']}

setup_kwargs = {
    'name': 'rai',
    'version': '0.2.0.dev1',
    'description': 'AI assisted treatments accessible to all',
    'long_description': '# `rai`, RadiotherapyAI\'s non-clinical open source autocontouring library\n\nThis Open Source Unregulated Software is provided in the hope that it might be\nuseful but WITHOUT ANY WARRANTY. It is **not** intended for clinical use, and\nis instead intended for research use only.\n\nIf you are looking for the Regulated Medical Device, `RAIContours`, that is\nbased upon the source code within this repository, when it has completed its\nregulatory approval, it will be available for download directly from\n<https://radiotherapy.ai/>. Prior to regulatory approval, you may be able to\nutilise `RAIContours` under a clinical trial notification or equivalent. If you\nare interested in undergoing a clinical trial with `RAIContours` please reach\nout to <clinical-trials@radiotherapy.ai>.\n\n## Goal\n\nCreate an AI Software as a Medical Device that saves lives built entirely from\nopen source software. Being a part of making it easier for researchers to\ntranslate from "bench-top to bedside", helping anyone to build regulated tools\nthat go on to save more lives than any one of us alone could ever hope to\nachieve.\n\n## Installation\n\nThis open source research library is able to be installed by running:\n\n```\npip install rai\n```\n\n## The regulatory documentation\n\nAll of the regulatory documentation is available under a creative commons\nlicense and is built upon\n[the amazing templates](https://openregulatory.com/templates/)\nprovided by [OpenRegulatory](https://openregulatory.com/).\n\nThe source code for the regulatory documentation is available within the\n[docs directory](./docs). The online rendering of the documentation is viewable\nat <https://docs.radiotherapy.ai>\n\nThe regulatory task is currently a work in progress. Right now I am just\nlearning the regulatory ropes while putting all of my warts up here for all to\nsee. There will be mistakes. If you find them please let me know. Also, if you\nwant to help out, please get in touch. My email address is\nsimon.biggs@radiotherapy.ai.\n',
    'author': 'Simon Biggs',
    'author_email': 'simon.biggs@radiotherapy.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://radiotherapy.ai',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
