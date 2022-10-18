# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['databricks_filestore_uploader', 'databricks_filestore_uploader.toolchain']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'databricks-filestore-uploader',
    'version': '0.1.0',
    'description': 'A quick filetree uploader for the databricks filestore, local to cloud.',
    'long_description': '# **Databricks FileStore Uploader**\n*A convenience tool for uploading local directories to the DBFS FileStore*\n\n<br />\n\n## **Upload Local Files**\nThis tool uploads specified source directories to specified paths in the *<abbr title="Databricks File System">DBFS</abbr> FileStore*.\n\nCreate a file adjacent to `main.py` called `input.yml`, and copy the following:\n```yml\nhost : <workspace-url>\ntoken: <user-access-token>\n\n# THIS TOOL CREATES OR OVERWRITES THE TARGET FOLDER!\n# Folder paths don\'t start with \'./\'\n# Folder paths don\'t end with \'/\'\npayloads:\n  some-local-folder : some-filestore-folder\n  some-other-local-folder : some-other/filestore-folder\n  # ...\n```\n\nReplace `<user-access-token>` with your token in databricks, and replace the example text under `payloads:` one or more "*source : destination*" pairs. \\\nThese local source directory paths **are relative to `main.py`**.\n\nYou can then upload all files contained in the local source folders to their specified destinations with:\n```\n./main.py\n```\nThough make sure you have [PyYAML](https://pypi.org/project/PyYAML/) installed.\n\n<br />\n\n## **Verify Uploads**\nIn a databricks notebook, you can verify uploads with:\n```py\ndisplay(dbutils.fs.ls("/FileStore/some-filestore-folder"))\n```\n\n<br />\n\n> Please Note❗ \\\n> This tool CREATES or OVERWRITES it\'s target dbfs:/FileStore path. Only target folders that are meant to be overwritten, or don\'t exist.',
    'author': 'anthonybench',
    'author_email': 'anthonybenchyep@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anthonybench/databricks-filestore-uploader',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
