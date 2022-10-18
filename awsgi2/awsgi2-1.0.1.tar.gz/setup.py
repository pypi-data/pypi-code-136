# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['awsgi2']

package_data = \
{'': ['*']}

install_requires = \
['libadvian>=1.3,<2.0']

setup_kwargs = {
    'name': 'awsgi2',
    'version': '1.0.1',
    'description': 'A WSGI gateway for the AWS API Gateway/Lambda proxy integration',
    'long_description': '======\nawsgi2\n======\n\n\nAWSGI allows you to use WSGI-compatible middleware and frameworks like Flask and Django with the `AWS API Gateway/Lambda proxy integration <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html>`_.\n\nThis is an improved fork of `original aws-wsgi <https://github.com/slank/awsgi>`_.\n\nInstallation\n------------\n\n``awsgi2`` is available from PyPI as ``awsgi2``::\n\n    pip install awsgi2\n\nExamples\n--------\n\nFlask\n^^^^^\n\n.. code-block:: python\n\n    import awsgi2\n    from flask import (\n        Flask,\n        jsonify,\n    )\n\n    app = Flask(__name__)\n\n\n    @app.route(\'/\')\n    def index():\n        return jsonify(status=200, message=\'OK\')\n\n\n    def lambda_handler(event, context):\n        return awsgi2.response(app, event, context, base64_content_types={"image/png"})\n\nDjango\n^^^^^^\n\n.. code-block:: python\n\n    import os\n    import awsgi2\n\n    from django.core.wsgi import get_wsgi_application\n\n    # my_app_directory/settings.py is a vanilla Django settings file, created by "django-admin startproject".\n    os.environ.setdefault(\'DJANGO_SETTINGS_MODULE\', \'my_app_directory.settings\')\n    # In the settings.py file, you may find it useful to include this setting to remove\n    # Django\'s need for SQLite, which is currently (2020-11-17) outdated in the Lambda runtime image\n    # DATABASES = { \'default\': { \'ENGINE\': \'django.db.backends.dummy\', } }\n\n    application = get_wsgi_application()\n\n    def lambda_handler(event, context):\n        return awsgi2.response(application, event, context, base64_content_types={"image/png"})\n\n\nDocker\n------\n\nFor more controlled deployments and to get rid of "works on my computer" -syndrome, we always\nmake sure our software works under docker.\n\nIt\'s also a quick way to get started with a standard development environment.\n\nSSH agent forwarding\n^^^^^^^^^^^^^^^^^^^^\n\nWe need buildkit_::\n\n    export DOCKER_BUILDKIT=1\n\n.. _buildkit: https://docs.docker.com/develop/develop-images/build_enhancements/\n\nAnd also the exact way for forwarding agent to running instance is different on OSX::\n\n    export DOCKER_SSHAGENT="-v /run/host-services/ssh-auth.sock:/run/host-services/ssh-auth.sock -e SSH_AUTH_SOCK=/run/host-services/ssh-auth.sock"\n\nand Linux::\n\n    export DOCKER_SSHAGENT="-v $SSH_AUTH_SOCK:$SSH_AUTH_SOCK -e SSH_AUTH_SOCK"\n\nCreating a development container\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\nBuild image, create container and start it::\n\n    docker build --ssh default --target devel_shell -t awsgi2:devel_shell .\n    docker create --name awsgi2_devel -v `pwd`":/app" -it `echo $DOCKER_SSHAGENT` awsgi2:devel_shell\n    docker start -i awsgi2_devel\n\npre-commit considerations\n^^^^^^^^^^^^^^^^^^^^^^^^^\n\nIf working in Docker instead of native env you need to run the pre-commit checks in docker too::\n\n    docker exec -i awsgi2_devel /bin/bash -c "pre-commit install"\n    docker exec -i awsgi2_devel /bin/bash -c "pre-commit run --all-files"\n\nYou need to have the container running, see above. Or alternatively use the docker run syntax but using\nthe running container is faster::\n\n    docker run --rm -it -v `pwd`":/app" awsgi2:devel_shell -c "pre-commit run --all-files"\n\nTest suite\n^^^^^^^^^^\n\nYou can use the devel shell to run py.test when doing development, for CI use\nthe "tox" target in the Dockerfile::\n\n    docker build --ssh default --target tox -t awsgi2:tox .\n    docker run --rm -it -v `pwd`":/app" `echo $DOCKER_SSHAGENT` awsgi2:tox\n\nDevelopment\n-----------\n\nTLDR:\n\n- Create and activate a Python 3.8 virtualenv (assuming virtualenvwrapper)::\n\n    mkvirtualenv -p `which python3.8` my_virtualenv\n\n- change to a branch::\n\n    git checkout -b my_branch\n\n- install Poetry: https://python-poetry.org/docs/#installation\n- Install project deps and pre-commit hooks::\n\n    poetry install\n    pre-commit install\n    pre-commit run --all-files\n\n- Ready to go.\n\nRemember to activate your virtualenv whenever working on the repo, this is needed\nbecause pylint and mypy pre-commit hooks use the "system" python for now (because reasons).\n',
    'author': 'Eero af Heurlin',
    'author_email': 'eero.afheurlin@advian.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/advian-oss/python-awsgi2/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
