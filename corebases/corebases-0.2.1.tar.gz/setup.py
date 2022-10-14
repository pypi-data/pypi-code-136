# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['corebases', 'corebases.backends']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy', 'asyncpg']

setup_kwargs = {
    'name': 'corebases',
    'version': '0.2.1',
    'description': 'Full power of *asyncpg* with user friendly api of *sqlalchemy.core*',
    'long_description': '# Corebases\n\n> Full power of *asyncpg* with user friendly api of *sqlalchemy.core*\n\n\nCorebases - is *async* adapter for [Sqlalchemy.Core](https://docs.sqlalchemy.org/en/14/core/).\nInterface and code based on [encode/databases](https://github.com/encode/databases), but has bit [difference](#difference-between-encodedatabases). Now supported only **asycnpg** driver (but It\'s possible to extend)\n\nCurrent status - **Experimental**\n\n## Reason for create fork\n - https://github.com/encode/databases/issues/403#issue-1016133277\n\n## Install\n```bash\n> pip install corebases\n```\n\n## Usage\n\n```python\n# Create a database instance, and connect to it.\nfrom corebases import database\ndatabase = database(\'postgres://user:pass@localhost:5432\')\nawait database.connect()\n\n# Insert some data.\nquery = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"\nvalue =  {"name": "Daisy", "score": 92}\n\nwith database.transaction() as db:\n    await db.execute(query=query, value=value)\n\n# Run a database query.\nquery = "SELECT * FROM HighScores"\nrows = await database.fetch_all(query=query)\nprint(\'High Scores:\', rows)\n\nawait database.disconnect()\n\n\n```\n\n## Difference between encode/databases\nPrincipal is a bit of difference in interface on transactions:\n\n*encode/database*:\n\n```python\nwith database.transaction():\n    await database.execute(query=query, value=value)\n\n```\n\n*corebases*:\n\n```python\nwith database.transaction() as db:\n    await db.execute(query=query, value=value)\n\n```\n\nAlso, *corebases* doesn\'t support methods:\n- feach_val\n- execute_many\n\nBut we can add in the future.\n',
    'author': 'Evgeny Zuev',
    'author_email': 'zueves@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/zueve/corebases',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
