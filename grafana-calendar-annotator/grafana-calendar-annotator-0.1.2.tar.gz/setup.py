# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grafana_calendar_annotator']

package_data = \
{'': ['*']}

install_requires = \
['ics>=0.7.2,<0.8.0',
 'python-decouple>=3.6,<4.0',
 'requests>=2.28.1,<3.0.0',
 'rich-click>=1.5.2,<2.0.0']

entry_points = \
{'console_scripts': ['grafana-calendar-annotator = '
                     'grafana_calendar_annotator.cli:cli']}

setup_kwargs = {
    'name': 'grafana-calendar-annotator',
    'version': '0.1.2',
    'description': 'Generate Grafana Annotations from calendar events',
    'long_description': "# Grafana Calendar Annotator\n\n[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6552/badge)](https://bestpractices.coreinfrastructure.org/projects/6552)\n\nGenerate [annotations](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/annotate-visualizations/) in Grafana from events pulled from an ICS calendar.\n\n## Hacktoberfest\n\nThis project welcomes [Hacktoberfest](https://hacktoberfest.com/) contributions! Any contributions to increase the [OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/en/projects/6552) percentage or that [close an issue](https://github.com/cam-barts/grafana-calendar-annotator/issues) will be given priority.\n\n## Getting Started\n\n### CLI\n\n```bash\n$ grafana-calendar-annotator --help\n\n Usage: grafana-calendar-annotator [OPTIONS]\n\n╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ *  --grafana-url                 -g      TEXT         Url of the Grafana instance to populate annotations into    │\n│                                                       [required]                                                  │\n│ *  --grafana-api-key             -k      TEXT         API key to authenticate to the Grafana instance [required]  │\n│ *  --calendar-url                -c      TEXT         URL of the ICS Calendar to use to populate events from      │\n│                                                       [required]                                                  │\n│ *  --flatten/--no-flatten        -f/-nf               Flattening events will create a single time annotation      │\n│                                                       instead of a span                                           │\n│                                                       [default: no-flatten]                                       │\n│                                                       [required]                                                  │\n│ *  --flatten-direction           -fd     [start|end]  Create the annotation at the start or the end of the event  │\n│                                                       if the event is flattened                                   │\n│                                                       [default: (start)]                                          │\n│                                                       [required]                                                  │\n│ *  --tags                        -t      TEXT         List of tags to add to created annotations                  │\n│                                                       [default: (generated,)]                                     │\n│                                                       [required]                                                  │\n│ *  --regenerate/--no-regenerate  -r/-nr               Regenerating will delete all annotations that have the same │\n│                                                       set of tags before creating new annotations                 │\n│                                                       [default: regenerate]                                       │\n│                                                       [required]                                                  │\n│    --delete-only                 -d                   Only delete annotations with tags, do not create new        │\n│                                                       annotations                                                 │\n│    --help                                             Show this message and exit.                                 │\n╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n```\n\nThe following flags can be set with environment variables:\n\n| Flag                | Variable Name     |\n| ------------------- | ----------------- |\n| --grafana-url       | GRAFANA_URL       |\n| --grafana-api-key   | GRAFANA_TOKEN     |\n| --flatten           | FLATTEN           |\n| --flatten-direction | FLATTEN_DIRECTION |\n\n```bash\ngrafana-calendar-annotator --grafana-url https://my-grafana.com --grafana-api-key abcd1234 --flatten --flatten-direction end --calendar-url https://my-calendar.com/personal.ics\n\n# is the same as this\n\nGRAFANA_URL=https://my-grafana.com GRAFANA_TOKEN=abcd1234 FLATTEN=true FLATTEN_DIRECTION=end grafana-calendar-annotator --calendar-url https://my-calendar.com/personal.ics\n```\n\n\n### Installing\n\n#### Pip\n\nFor the library and the cli\n\n```shell\npip install grafana_calendar_annotator\n```\n\n#### Pipx\n\nPipx is useful for [installing and running applications in isolated environments](https://pypa.github.io/pipx/). I've always found it useful to ensure python applications are can be executed from anywhere in your system.\n\n```shell\npipx install grafana_calendar_annotator\n```\n\n## Running the tests\n\n<!--TODO-->\n\n## Deployment\n\n<!--TODO-->\n\n## Built With\n\n  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used for the Code of Conduct\n  - [Poetry](https://python-poetry.org/) - Used for build and packaging\n  - [Contributing.md Generator](https://generator.contributing.md/)\n  - [Billie Thompson's README Template](https://github.com/PurpleBooth/a-good-readme-template)\n\n## Contributing\n\nPlease read [CONTRIBUTING.md](https://github.com/cam-barts/grafana-calendar-annotator/blob/main/CONTRIBUTING.md) for details on our code\nof conduct, and the process for submitting pull requests to us.\n\n## Versioning\n\nWe use [Semantic Versioning](http://semver.org/) for versioning. For the versions\navailable, see the [tags on this\nrepository](https://github.com/cam-barts/grafana-calendar-annotator/tags).\n\n## Contributors\n\n[Contributors](https://github.com/cam-barts/grafana-calendar-annotator/contributors)\nwho participated in this project.\n\n## License\n\nThis project is licensed under the [MIT](https://github.com/cam-barts/grafana-calendar-annotator/blob/main/LICENSE.txt).",
    'author': 'Cam',
    'author_email': 'camerond.barts@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cam-barts/grafana-calendar-annotator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
