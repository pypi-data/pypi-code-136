# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdto']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0']

setup_kwargs = {
    'name': 'sdto',
    'version': '0.1.4',
    'description': 'Subdomain takeover finder',
    'long_description': '[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Downloads](https://pepy.tech/badge/sdto)](https://pepy.tech/project/sdto)\n\n# sdto - subdomain takeover finder\n\nSubdomain takeover scanner  \nCurrent count of fingerprints: **80**\n\n[What is subdomain takeover?](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)\n\n\n## Supported Services\n\n```\nacquia\nactivecampaign\naftership\nagilecrm\naha\nairee\nanima\nannouncekit\naws/s3\nbigcartelbitbucket\nbrightcove\ncampaignmonitor\ncanny\ncargo\ncargocollective\ncloudfront\ndesk\nfastly\nfeedpress\nflexbe\nflywheel\nfrontify\ngemfury\ngetresponse\nghost\ngitbook\ngithub\nhatenablog\nhelpjuice\nhelprace\nhelpscout\nheroku\nhubspot\nintercom\njazzhr\njetbrains\nkajabi\nkinsta\nlaunchrock\nmashery\nnetlify\nngrok\npagewiz\npantheon\npingdom\nproposify\nreadme\nreadthedocs\ns3bucket\nshopify\nshortio\nsimplebooklet\nsmartjob\nsmartling\nsmugmug\nsmugmug\nsprintful\nstatuspage\nstrikingly\nsurge\nsurveygizmo\nsurveysparrow\ntave\nteamwork\nthinkific\ntictail\ntilda\ntumbler\nuberflip\nunbounce\nuptimerobot\nuservoice\nvend\nwebflow\nwishpond\nwix\nwordpress\nworksites.net\nwufoo\nzendesk\n```\n## Installation:\n\n\nto use as python library\n```shell\npip install sdto\n```\n\nto use as a CLI tool\n\n```shell\npip install sdto[cli]\n```\n\n\n**or:**\n```shell\ngit clone https://github.com/scanfactory/sdto.git\ncd sdto\npoetry install\n```\n## Usage as a CLI tool\n\nExamples:\n\n```shell\npython3 -m sdto -t www.domain.com\npython3 -m sdto -t www.domain.com -f path/to/custom-fingerprints-file.json\npython3 -m sdto -t https://www.domain.com/\npython3 -m sdto -t http://www.domain.com/\npython3 -m sdto -t www.domain.com --no-ssl\npython3 -m sdto -t www.domain.com -v --timeout 30\npython3 -m sdto -t www.domain.com -H "user-agent" "your-custom-user-agent" -H "another-header" "header-value"\npython3 -m sdto -t www.domain.com -F json\npython3 -m sdto -t www.domain.com -o output.txt\npython3 -m sdto -t www.domain.com -F json -o output.json\npython3 -m sdto -t www.domain.com -F txt -o output.txt\npython3 -m sdto -t www.domain.com -p http://127.0.0.1:8080 \npython3 -m sdto -l subdomains-list.txt\n```\n\n### Docker support\n\nBuild the image:\n\n```\ndocker build -t sdto .\n```\n\nRun the container:\n\n```\ndocker run -it --rm sdto -t www.domain.com -v\n```\n\n\n### Using custom fingerprints\n\nYou can specify custom fingerprints file via `-f path/to/file.json` parameter.\nThe expected json file format:\n```json\n{\n  "AWS/S3": {"pattern": "The specified bucket does not exist"},\n  "BitBucket": {"pattern": "Repository not found"},\n  "Fastly": {"pattern": "Fastly pattern\\\\: unknown domain\\\\:", "process_200": true}\n}\n```\nNote that `pattern` value is expected to be a python regexp.\n\n## Usage as a python library\n\nExample:\n\n```python\nimport re\n\nfrom aiohttp import ClientSession\nfrom sdto import check_target, RegexFingerprint\n\n\nasync def main():\n    async with ClientSession() as cs:\n        fingerprint = await check_target(\n            cs=cs,\n            target="sub.domain.com",\n            ssl=True,\n            proxy=None,\n            fingerprints=[\n                RegexFingerprint(\n                    "Github", \n                    re.compile(r"There isn\\\'t a Github Pages site here\\."),\n                    process_200=False,\n                )\n            ]\n        )\n        if not fingerprint:\n            print("No match")\n        else:\n            print(fingerprint.name)\n\n```\n',
    'author': 'godpleaseno',
    'author_email': 'zfrty@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/scanfactory/sdto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
