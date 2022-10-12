# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webster',
 'webster.conf',
 'webster.core',
 'webster.net',
 'webster.net.request',
 'webster.pipelines',
 'webster.utils']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.9.1,<5.0.0',
 'pycurl>=7.45.1,<8.0.0',
 'pymongo>=4.2.0,<5.0.0',
 'w3lib>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'webster-crawler',
    'version': '0.1.0',
    'description': 'Website crawler-ish thing?',
    'long_description': '# Webster\n\nWebster is an experimental python web scraping framework for my own learning.\n\nWebster can be used to scrape or download webpages by giving a list of urls to visit and\noptionally a list of urls to stay within.\n\nWebster could be used as a broad crawler also, but it is not optimized for that as of now.\n\n## Version\nWebster has been tested using Python 3.10+\n\n## Project documentation\n1. [Quick start guide](docs/project_docs/quickstart.md)\n2. [Architectural model](docs/project_docs/architecture.md)\n3. [Functional specification](docs/project_docs/functional_spec.md)\n4. [Test documentation](docs/project_docs/testing.md)\n\n\n## Installation\nInstall Webster using one off the following methods\n\nFrom requirements.txt\n```bash\npip install -r requirements.txt\n```\n\n\n### Dependencies\nWebster is using multiple external Python packages some of which are:\n+ [lxml](https://lxml.de/index.html) used for processing html documents.\n+ [w3lib](https://w3lib.readthedocs.io/en/latest/) used for URL handling and prosessing.\n+ [pycURL](http://pycurl.io/) used for networking and making requests to a http server.\n+ [pymongo](https://pymongo.readthedocs.io/en/stable/) tools for working with mongoDB using python\n\nUse [pipreqs](https://pypi.org/project/pipreqs/) to make new requirements.txt\nif new dependencies are added in PR force over requirements.txt\nand make sure to include the new one in PR.\n\n```bash\npipreqs --force\n```\n\nUpdate dependencies if necessary\n\n```bash\npip install -U -r requirements.txt\n```\n\n## Testing\nWebster uses [unittest](https://docs.python.org/3/library/unittest.html) for testing.\n\nTo run all the tests use the following command:\n\n```bash\npython -m unittest discover -v\n```\n\nExample: We want to test Parser module\nTo run single module test use the following command:\n\n```bash\npython -m unittest test.test_parser -v\n```\n\n\n### Coverage\nTo run test coverage use the [coverage](https://coverage.readthedocs.io/en/6.5.0/) module\n\n```bash\npython -m coverage run -m unittest\n```\n\nTo show coverage report in terminal\n\n```bash\npython -m coverage report\n```\n\nOutput should look something like this.\n\n```console\nName                              Stmts   Miss  Cover\n-----------------------------------------------------\ntest/__init__.py                      0      0   100%\ntest/test_data/__init__.py           10      0   100%\ntest/test_downloader.py              43      1    98%\ntest/test_parser.py                  54      1    98%\ntest/test_request.py                 49      2    96%\ntest/test_robotstxt.py               23      1    96%\ntest/test_url_tools.py               22      1    95%\ntest/test_validators.py              53      1    98%\nwebster/__init__.py                   0      0   100%\nwebster/conf/__init__.py              0      0   100%\nwebster/conf/settings.py              9      0   100%\nwebster/core/__init__.py              0      0   100%\nwebster/core/downloader.py           36      8    78%\nwebster/core/parser.py               40      1    98%\nwebster/net/__init__.py               0      0   100%\nwebster/net/request/__init__.py      47      2    96%\nwebster/pipelines/__init__.py         0      0   100%\nwebster/robotstxt.py                 15      2    87%\nwebster/utils/__init__.py             0      0   100%\nwebster/utils/url_tools.py           15      0   100%\nwebster/utils/validators.py          16      7    56%\n-----------------------------------------------------\nTOTAL                               432     27    94%\n```\n\nFor a nicer report and more detailed use the html report\n\n```bash\npython -m coverage html\n\nopen htmlcov/index.html   \n```\n\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\nBSD 3-Clause License\n\nCopyright (c) 2022, Henri Remonen.\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:\n\n1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.\n\n2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.\n\n3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.',
    'author': 'Henri Remonen',
    'author_email': 'henri@remonen.fi',
    'maintainer': 'Henri Remonen',
    'maintainer_email': 'henri@remonen.fi',
    'url': 'https://github.com/HRemonen/Webster',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
