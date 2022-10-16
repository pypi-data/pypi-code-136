# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jinja_docker_compose']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'docker-compose>=1.29.2,<2.0.0']

entry_points = \
{'console_scripts': ['jinja-docker-compose = jinja_docker_compose.main:main']}

setup_kwargs = {
    'name': 'jinja-docker-compose',
    'version': '1.0.1',
    'description': 'Enables jinja like preposessing of docker-compose files.',
    'long_description': '# `jinja-docker-compose`\n[`jinja-docker-compose`](https://github.com/MorganLindqvist/jinja-compose) is a simple python script that wraps [`docker-compose`](https://docs.docker.com/compose/) to provide Jinja2 based templating ability to `docker-compose`. It is based on [\'jinja-commpose\'](https://github.com/sinzlab/jinja-compose).\n\n## Dependencies\n`jinja-docker-compose` requires following dependencies to be installed on the system:\n* python3\n* python3-pip\n* Docker engine\n\n## Installing\nTo install the script, simply run:\n\n```bash\n$ pip install jinja-docker-compose\n```\nThe script is installed in ~/.local/bin. If not in the PATH add the following to your initiation script, like .bashrc\n```\nPATH=~/.local/bin:$PATH\n```\n\n## Using `jinja-docker-compose`\nThe `jinja-docker-compose` preprocess the `docker-compose` file to act upon for instance `for loops` and `conditional statements`. The variables used in the preprocessing resides in a dictionnay file in JSON format.\n\n`jinja-docker-compose`can either just do the pre-processing or as well run `docker-compose` on the processed file.\n\nExample of dictionary file:\n```json\n{\n  "LOGGING": "false",\n  "N_GPU": "2"\n}\n```\n\n`docker-compose` file to preprocess:\n```\nversion: "3"\nservices:\n  {% for i in range(N_GPU) %}\n  ubuntu{{i}}:\n    image: ubuntu:latest\n  {% endfor %}\n  ubuntulog:\n    image: ubuntu:latest\n    {% if LOGGING == \'true\' %}\n    logging:\n      driver: syslog\n      options:\n        syslog-address: "tcp://graylog.example.com:516"\n    {% endif %}\n```\nAfter processing the file looks like this:\n```\nversion: "3"\nservices:\n  ubuntu1:\n    image: ubuntu:latest\n  ubuntu2:\n    image: ubuntu:latest\n  ubuntulog:\n    image: ubuntu:latest\n```\nThe default names of the files are:\nFile|Default name\n:--|--\nInput file to preprocess|jinja-docker-compose.yml\nDictionary file| jinja-docker-compose.dic\nOutput file | docker-compose.yml\n\nThe options are:\nOption|Description\n:--|--\n-f|Input file name\n-D|Dictionary file name\n-o|Output file name\n-s|Uses the SafeLoader when loading the YAML, this removes the possible exploit that the default FullLoader enables.\n-G|Only genereates the output file, do not run `docker-compose`\n\nAll options that are valid options to `docker-compose` can also be given to `jinja-docker-compose`and then passed on to `docker-compose`\n\nDepending on how your system is configured, you may need to run the script with `sudo` (i.e. if you usually need `sudo` to run `docker`, you will need `sudo`).',
    'author': 'Morgan',
    'author_email': 'Morgan@quzed.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
