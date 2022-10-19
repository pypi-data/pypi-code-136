# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['target_jsonl_webhdfs']
install_requires = \
['adjust-precision-for-schema==0.3.3',
 'hdfs==2.7.0',
 'jsonschema==2.6.0',
 'singer-python==5.8.0']

entry_points = \
{'console_scripts': ['target-jsonl-webhdfs = target_jsonl_webhdfs:main']}

setup_kwargs = {
    'name': 'target-jsonl-webhdfs',
    'version': '0.1.4.4',
    'description': 'Singer.io target for writing JSON Line files via webhdfs',
    'long_description': '# target-jsonl-webhdfs\n\nA [Singer](https://singer.io) target that writes data to HDFS cluster in the JSONL ([JSON Lines](http://jsonlines.org/)) format.\nThis is fork of the [Target-jsonl](https://github.com/andyhuynh3/target-jsonl) repo.\n\n## How to use it\n\n`target-jsonl` works together with any other [Singer Tap] to move data from sources like [Braintree], [Freshdesk] and [Hubspot] to JSONL formatted files.\n\n### Install\n\nWe will use [`tap-exchangeratesapi`][Exchangeratesapi] to pull currency exchange rate data from a public data set as an example.\n\nFirst, make sure Python 3 is installed on your system or follow these installation instructions for [Mac] or [Ubuntu].\n\nIt is recommended to install each Tap and Target in a separate Python virtual environment to avoid conflicting dependencies between any Taps and Targets.\n\n```bash\n # Install tap-exchangeratesapi in its own virtualenv\npython3 -m venv ~/.virtualenvs/tap-exchangeratesapi\nsource ~/.virtualenvs/tap-exchangeratesapi/bin/activate\npip install tap-exchangeratesapi\ndeactivate\n\n# Install target-jsonl in its own virtualenv\npython3 -m venv ~/.virtualenvs/target-jsonl\nsource ~/.virtualenvs/target-jsonl/bin/activate\npip install target-jsonl\ndeactivate\n```\n\n### Run\n\nWe can now run `tap-exchangeratesapi` and pipe the output to `target-jsonl`.\n\n```bash\n~/.virtualenvs/tap-exchangeratesapi/bin/tap-exchangeratesapi | ~/.virtualenvs/target-jsonl/bin/target-jsonl\n```\n\nThe data by default will be written to a file called `exchange_rate-{timestamp}.jsonl` in your working directory.\n\n```bash\n› cat exchange_rate-{timestamp}.jsonl\n{"CAD": 1.3954067515, "HKD": 7.7503228187, "ISK": 147.1130787678, "PHP": 50.5100534957, "DKK": 6.8779745434, "HUF": 327.9376498801, "CZK": 25.018446781, "GBP": 0.8059214167, "RON": 4.4673491976, "SEK": 9.9002029146, "IDR": 15321.0016602103, "INR": 75.6516325401, "BRL": 5.4711307877, "RUB": 73.6220254566, "HRK": 6.9765725881, "JPY": 106.548607268, "THB": 32.420217672, "CHF": 0.9750046117, "EUR": 0.9223390518, "MYR": 4.3475373547, "BGN": 1.8039107176, "TRY": 6.988286294, "CNY": 7.0764619074, "NOK": 10.3973436635, "NZD": 1.6446227633, "ZAR": 18.4316546763, "USD": 1.0, "MXN": 24.1217487548, "SGD": 1.4152370411, "AUD": 1.5361556908, "ILS": 3.5102379635, "KRW": 1218.9540675152, "PLN": 4.1912931194, "date": "2020-04-29T00:00:00Z"}\n```\n\n### Optional Configuration\n\n`target-jsonl` takes an optional configuration file that can be used to set formatting parameters like the delimiter - see [config.sample.json](config.sample.json) for examples. To run `target-jsonl` with the configuration file, use this command:\n\n```bash\n~/.virtualenvs/tap-exchangeratesapi/bin/tap-exchangeratesapi | ~/.virtualenvs/target-jsonl/bin/target-jsonl -c my-config.json\n```\n\nHere is a brief description of the optional config keys\n\n`destination_path` - Specifies where to write the resulting `.jsonl` file to. By default, the file gets written in your working directory.\n\n`custom_name` - Specifies a custom name for the filename, instead of the stream name (i.e. `{custom_name}-{timestamp}.jsonl`, asumming `do_timestamp_file` is `true`). By default, the stream name will be used.\n\n`do_timestamp_file` - Specifies if the file should get timestamped. By default, the resulting file will have a timestamp in the file name (i.e. `exchange_rate-{timestamp}.jsonl` as described above in the `Run` section). If this option gets set to `false`, the resulting file will not have a timestamp associated with it (i.e. `exchange_rate.jsonl` in our example).\n\n`webhdfs` - Boolean variable to enable webhdfs writing.\n\n`webhdfs_url` - Specifies url for connection to the webhdfs service (i.e. `http://hostname:port`).\n\n`webhdfs_user` - Specifies user that will be use for connect to the webhdfs service.\n\n---\n\nCopyright &copy; 2022 Andy Huynh, Stanislav Lysikov\n\n[Singer Tap]: https://singer.io\n[Braintree]: https://github.com/singer-io/tap-braintree\n[Freshdesk]: https://github.com/singer-io/tap-freshdesk\n[Hubspot]: https://github.com/singer-io/tap-hubspot\n[Exchangeratesapi]: https://github.com/singer-io/tap-exchangeratesapi\n[Mac]: http://docs.python-guide.org/en/latest/starting/install3/osx/\n[Ubuntu]: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04\n',
    'author': 'Andy Huynh',
    'author_email': 'andy.huynh312@gmail.com',
    'maintainer': 'Stanislav Lysikov',
    'maintainer_email': 'stave.tx@gmail.com',
    'url': 'https://github.com/barloc/target-jsonl-webhdfs',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
