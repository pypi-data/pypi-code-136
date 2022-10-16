# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.', 'psycopg2': './psycopg2'}

packages = \
['psycopg2',
 'puff',
 'puff.contrib',
 'puff.contrib.django',
 'puff.contrib.django.postgres']

package_data = \
{'': ['*']}

install_requires = \
['greenlet>=1.1,<2.0']

setup_kwargs = {
    'name': 'puff-py',
    'version': '0.1.1',
    'description': 'Python support for Puff',
    'long_description': '# Python for ☁ Puff ☁!\n\n`puff-py` provides support to run Python on the puff runtime.\n\nSee the official [puff repository](https://github.com/hansonkd/puff) for more details.\n\nThere is also an integrated example with Django found in this repo\'s `/examples` folder [which gives specific guidance on how to use Django](https://github.com/hansonkd/puff-py/tree/main/examples/hello_world_puff)\n\nTo use the example\n\n```bash\ncd ./examples/hello_world_puff/hello_world_py_app\npoetry install\npoetry run cargo run runserver\n```\n\nYou may have to adjust your `PUFF_POSTGRES_URL` and `PUFF_REDIS_URL` to your local Postgres and redis instances to get it to run.\n\n# Using Django with Puff\n\nSet up your project:\n\n```bash\ncargo new my_puff_proj --bin\ncd my_puff_proj\ncargo add puff-rs\npoetry new my_puff_proj_py\ncd my_puff_proj_py\npoetry install puff-py\npoetry install django\npoetry run django-admin startproject hello_world_django_app .\n```\n\nAdd Django to your Puff Program\n\n```rust\nuse puff_rs::program::commands::{PytestCommand, WSGIServerCommand, DjangoManagementCommand};\nuse puff_rs::graphql::handlers::{handle_graphql, handle_subscriptions, playground};\nuse puff_rs::prelude::*;\n\n\nfn main() -> ExitCode {\n    let rc = RuntimeConfig::default()\n        .add_env("DJANGO_SETTINGS_MODULE", "hello_world_django_app.settings")\n        .set_postgres(true)\n        .set_redis(true)\n        .set_pubsub(true)\n        .set_gql_schema_class("hello_world_py_app.Schema");\n\n    let router = Router::new()\n            .get("/", playground("/graphql", "/subscriptions"))\n            .post("/graphql", handle_graphql())\n            .get("/subscriptions", handle_subscriptions());\n\n    Program::new("puff_django_app_example")\n        .about("This is my first graphql app")\n        .runtime_config(rc)\n        .command(DjangoManagementCommand::new())\n        .command(WSGIServerCommand::new_with_router("hello_world_django_app.wsgi.application", router))\n        .command(PytestCommand::new("."))\n        .run()\n}\n```\n\nChange your settings to use Puff Database and Redis Cache\n\n```python\nDATABASES = {\n    \'default\': {\n        \'ENGINE\': \'puff.contrib.django.postgres\',\n        \'NAME\': \'global\',\n    }\n}\n\nCACHES = {\n    \'default\': {\n        \'BACKEND\': \'puff.contrib.django.redis.PuffRedisCache\',\n        \'LOCATION\': \'redis://global\',\n    }\n}\n```\n\nChange `wsgi.py` to serve static files;\n\n```python\n...\n\nfrom django.core.wsgi import get_wsgi_application\nfrom django.contrib.staticfiles.handlers import StaticFilesHandler\n\napplication = StaticFilesHandler(get_wsgi_application())\n```\n\nUse Poetry and Cargo run instead of `./manage.py`\n\n```bash\npoetry run cargo run runserver\npoetry run cargo run django migrate\n```',
    'author': 'Kyle Hanson',
    'author_email': 'me@khanson.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hansonkd/puff',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
