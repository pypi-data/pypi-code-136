# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drive']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.64.0,<3.0.0',
 'httplib2>=0.20.4,<0.21.0',
 'oauth2client>=4.1.3,<5.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'python-magic>=0.4.27,<0.5.0']

setup_kwargs = {
    'name': 'drive',
    'version': '0.4.0',
    'description': 'Google Drive client',
    'long_description': '# Drive\n\nGoogle Drive client.\n\n## Install\n\n    python -m pip install drive\n\nWith Poetry:\n\n    poetry add drive\n\n## Usage\n\nThe API exposes a client as `drive.client.Client` that manipulates instances of\n`drive.files.File`. A `File` represent a Google Drive file. Note that both\nregular files and directories are represented as `File`s, and a file can have\nmultiple parent directories. You can check if a `File` is a directory using the\n`is_directory` attribute.\n\nNote: "Folder" is just a synonym for "Directory".\n\n### Authentication\n\nBy default, the client reads your service account key JSON file at the location\ngiven by the environment variable `GOOGLE_APPLICATION_CREDENTIALS`. You can\noverride this behavior by passing it directly:\n\n    client = Client("/path/to/your/service-account-key.json")\n\n\nSee Google’s documentation on [how to create a service account key][k].\n\n[k]: https://cloud.google.com/iam/docs/creating-managing-service-account-keys\n\n### Client\n\nHigh-level `Client` methods:\n\n* `get_file(file_id)` (`File`)\n* `get_file_by_name(name)` (`File`)\n* `files_shared_with_me()` (`File` list)\n* `get_shared_directory(name)` (`File`)\n* `root()` (`File`)\n* `upload_file(parent, path[, name])`: Upload a file\n* `upload_excel_workbook(parent, name, workbook)`: Upload an `openpyxl`\n  workbook in a Google spreadsheet under `parent` with the name `name`.\n\nThe client also exposes low-level methods that work on file ids.\n\n### File\n\n* `id` (`str`, attribute)\n* `name` (`str`, attribute)\n* `is_directory` (`bool`, attribute)\n* `human_type` (`str`, attribute): Human-readable file type\n* `exists()` (`bool`)\n* `unlink()` (`bool`): Remove the file. If it\'s a directory, all its children\n  are removed as well\n* `rename(new_name)`: Rename the file\n* `move_in(new_parent[, new_name])`: Move a file under another directory. It\n  can also rename the file at the same time.\n* `list()`: List a directory’s content\n* `create_folder(name)`: Create a folder under the current one\n* `get_or_create_folder(name)`: Retrieve a child folder or create it if it\n  doesn’t exist\n* `get_child(name)`: Return a file under the current directory.\n* `parents()`: Return a file\'s parents\n* `parent()`: Return the first parent of a file\n* `download_file(path[, mime_type])`: Download the file at a given location\n* `download_workbook()`: Download the file as an `openpyxl` workbook\n* `json()`: Parse the file as JSON\n* `jsons()`: Parse the file as JSONS (one JSON per line) and returns a generator\n\nMethods that operate on directories (e.g. `list()`) generally have no effect if\nthe `File` instance is a regular file.\n\n### Examples\n\n```python\nfrom drive.client import Client\n\n# Uses credentials from the path in the environment variable\n# GOOGLE_APPLICATION_CREDENTIALS.\ncl = Client()\n\n# Get the root directory\nd = cl.root()\nprint(d.is_directory) # True\nprint(d.name) # e.g. "My Drive"\n\n# Get a directory\'s content\nfor f in d.list():\n    print(f.name)\n\n# Get a shared directory\nd = cl.get_shared_directory("My Shared Dir")\n```\n\n#### Spreadsheets\n\n```python\nfrom drive.client import Client\nfrom openpyxl import Workbook\n\ncl = Client()\n\n# Download\nf = cl.get_file_by_name("my_sheet")\nworkbook = f.download_workbook()  # openpyxl workbook\n# save your download:\nworkbook.save("myfile.xlsx")\n\n# Upload\nworkbook = Workbook()\nd = cl.get_shared_directory("My Shared Directory")\ncl.upload_excel_workbook(d, "my_other_sheet", workbook)\n```\n\n#### Drawings\n\n```python\nfrom drive.client import Client\n\ncl = Client()\n# download a Drawing in a png image\ncl.download_file("11AASomeFileId", "localfile.png", "image/png")\n```\n\n## License\n\nCopyright © 2016-2022 Baptiste Fontaine\n\nDistributed under the MIT License.\n',
    'author': 'Baptiste Fontaine',
    'author_email': 'b@ptistefontaine.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
