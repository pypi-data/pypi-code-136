# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['txt2ebook',
 'txt2ebook.formats',
 'txt2ebook.formats.templates',
 'txt2ebook.formats.templates.epub',
 'txt2ebook.helpers',
 'txt2ebook.languages',
 'txt2ebook.models']

package_data = \
{'': ['*']}

install_requires = \
['CJKwrap>=2.2,<3.0',
 'EbookLib>=0.17.1,<0.18.0',
 'bs4>=0.0.1,<0.0.2',
 'cchardet>=2.1.7,<3.0.0',
 'langdetect>=1.0.9,<2.0.0',
 'regex>=2021.11.10,<2022.0.0']

entry_points = \
{'console_scripts': ['tte = txt2ebook.txt2ebook:main',
                     'txt2ebook = txt2ebook.txt2ebook:main']}

setup_kwargs = {
    'name': 'txt2ebook',
    'version': '0.1.14',
    'description': 'CLI tool to convert txt file to ebook format',
    'long_description': "# txt2ebook\n\nConsole tool to convert txt file to different ebook format.\n\n## Installation\n\nStable version From PyPI:\n\n```console\npython3 -m pip install txt2ebook\n```\n\nLatest development version from GitHub:\n\n```console\npython3 -m pip install -e git+https://github.com/kianmeng/txt2ebook.git\n```\n\n## Usage\n\nShowing help message of command-line options:\n\n```console\ntxt2ebook --help\n```\n\n```console\nusage: tte [-f {epub,txt}] [-t TITLE] [-l LANGUAGE] [-a AUTHOR]\n           [-c IMAGE_FILENAME] [-w WIDTH] [-rd REGEX] [-rvc REGEX] [-rv REGEX]\n           [-rc REGEX] [-rt REGEX] [-ra REGEX] [-rl REGEX] [-rr REGEX REGEX]\n           [-et TEMPLATE] [-vp] [-tp] [-nb] [-d] [-h] [-v]\n           TXT_FILENAME [EBOOK_FILENAME]\n\ntxt2ebook/tte is a cli tool to convert txt file to ebook format.\n\n  website: https://github.com/kianmeng/txt2ebook\n  issues: https://github.com/kianmeng/txt2ebook/issues\n\npositional arguments:\n  TXT_FILENAME         set the source text filename\n  EBOOK_FILENAME       set the converted ebook filename (default: 'TXT_FILENAME.{epub,txt}')\n\noptional arguments:\n  -f {epub,txt}        set the export format ebook (default: 'epub')\n  -t TITLE             set the title of the ebook (default: 'None')\n  -l LANGUAGE          set the language of the ebook (default: 'None')\n  -a AUTHOR            set the author of the ebook (default: '[]')\n  -c IMAGE_FILENAME    set the cover of the ebook\n  -w WIDTH             set the width for line wrapping\n  -rd REGEX            set the regex to delete word or phrase (default: '[]')\n  -rvc REGEX           set the regex to parse volume and chapter header (default: by LANGUAGE)\n  -rv REGEX            set the regex to parse volume header (default: by LANGUAGE)\n  -rc REGEX            set the regex to parse chapter header (default: by LANGUAGE)\n  -rt REGEX            set the regex to parse title of the book (default: by LANGUAGE)\n  -ra REGEX            set the regex to parse author of the book (default: by LANGUAGE)\n  -rl REGEX            set the regex to delete whole line (default: '[]')\n  -rr REGEX REGEX      set the regex to search and replace (default: '[]')\n  -et TEMPLATE         set the CSS template for epub ebook (default: 'clean')\n  -vp, --volume-page   set to generate each volume as separate page\n  -tp, --test-parsing  set to test parsing for volume/chapter header\n  -nb, --no-backup     set to disable backup source TXT_FILENAME\n  -d, --debug          show debugging log and stacktrace\n  -h, --help           show this help message and exit\n  -v, --version        show program's version number and exit\n```\n\nConvert a txt file into epub:\n\n```console\ntxt2book ebook.txt\n```\n\n## Copyright and License\n\nCopyright (c) 2021,2022 Kian-Meng Ang\n\nThis program is free software: you can redistribute it and/or modify it under\nthe terms of the GNU Affero General Public License as published by the Free\nSoftware Foundation, either version 3 of the License, or (at your option) any\nlater version.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY\nWARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A\nPARTICULAR PURPOSE. See the GNU Affero General Public License for more details.\n\nYou should have received a copy of the GNU Affero General Public License along\nwith this program. If not, see <https://www.gnu.org/licenses/>.\n",
    'author': 'Kian-Meng Ang',
    'author_email': 'kianmeng@cpan.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kianmeng/txt2ebook',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
