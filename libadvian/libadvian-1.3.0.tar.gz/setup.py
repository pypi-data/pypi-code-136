# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['libadvian', 'libadvian.logging']

package_data = \
{'': ['*']}

extras_require = \
{'http': ['frozendict>=2.3,<3.0'],
 'http:python_version >= "3.6" and python_version < "3.7"': ['requests>=2.17,<3.0'],
 'http:python_version >= "3.7" and python_version < "3.8"': ['requests>=2.28,<3.0']}

setup_kwargs = {
    'name': 'libadvian',
    'version': '1.3.0',
    'description': 'Small helpers that do not warrant their own library',
    'long_description': '=========\nlibadvian\n=========\n\nSmall helpers that do not warrant their own library.\n\nNotable helpers\n---------------\n\n  - init_logging (libadvian.logging): Initializes default logger to our standard log format\n  - b64_to_uuid and uuid_to_b64 (libadvian.binpackers): URL-safe base64 UUID decode/encode\n  - ensure_[utf8|str] (libadvian.binpackers): For making sure you are dealing with bytes or strings.\n\nThere is more, everything is type hinted and documented, just look around.\n\nHTTP Logging notes\n------------------\n\nNote: requires you install the extra feature "http" to use\n\nIf LOG_HTTP_TARGET_URI is set in ENV, init_logging will add BufferedHTTPMultiRecordHandler handler\nfor shipping logs to Vector/Logtash (or similar that can take POSTs with text body), for username and password use\nLOG_HTTP_USERNAME and LOG_HTTP_PASSWORD variables.\n\nAny extra properties set by logger.level("message", extra={"key": "value"}) will be resolved and added to\nlabels_json -header in the POST. If LOG_GLOBAL_LABELS_JSON is set in ENV that will be decoded and filter\nadded to init_logging -pipeline that will add those labels as extras to all logrecords.\n\nYou can of course initialize those handlers manually and use them as you wish. For quick and very dirty\nway of adding headers to the HTTP requests muck with libadvian.logging.httpmulti.HTTP_LOGGING_CONFIG\nbefore initializing logging::\n\n    libadvian.logging.httpmulti.HTTP_LOGGING_CONFIG["handlers"]["http"].update({"session_options": { "headers": {\n        "Myheader": "myval"\n    }}})\n\nMaking a deep copy and using logging.dictConfig() on the copy would be much cleaner though.\n\nDocker\n------\n\nFor more controlled deployments and to get rid of "works on my computer" -syndrome, we always\nmake sure our software works under docker.\n\nIt\'s also a quick way to get started with a standard development environment.\n\nSSH agent forwarding\n^^^^^^^^^^^^^^^^^^^^\n\nWe need buildkit_::\n\n    export DOCKER_BUILDKIT=1\n\n.. _buildkit: https://docs.docker.com/develop/develop-images/build_enhancements/\n\nAnd also the exact way for forwarding agent to running instance is different on OSX::\n\n    export DOCKER_SSHAGENT="-v /run/host-services/ssh-auth.sock:/run/host-services/ssh-auth.sock -e SSH_AUTH_SOCK=/run/host-services/ssh-auth.sock"\n\nand Linux::\n\n    export DOCKER_SSHAGENT="-v $SSH_AUTH_SOCK:$SSH_AUTH_SOCK -e SSH_AUTH_SOCK"\n\nCreating a development container\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\nBuild image, create container and start it::\n\n    docker build --ssh default --target devel_shell -t libadvian:devel_shell .\n    docker create --name libadvian_devel -v `pwd`":/app" -it `echo $DOCKER_SSHAGENT` libadvian:devel_shell\n    docker start -i libadvian_devel\n\npre-commit considerations\n^^^^^^^^^^^^^^^^^^^^^^^^^\n\nIf working in Docker instead of native env you need to run the pre-commit checks in docker too::\n\n    docker exec -i libadvian_devel /bin/bash -c "pre-commit install"\n    docker exec -i libadvian_devel /bin/bash -c "pre-commit run --all-files"\n\nYou need to have the container running, see above. Or alternatively use the docker run syntax but using\nthe running container is faster::\n\n    docker run --rm -it -v `pwd`":/app" libadvian:devel_shell -c "pre-commit run --all-files"\n\nTest suite\n^^^^^^^^^^\n\nYou can use the devel shell to run py.test when doing development, for CI use\nthe "tox" target in the Dockerfile::\n\n    docker build --ssh default --target tox -t libadvian:tox .\n    docker run --rm -it -v `pwd`":/app" libadvian:tox\n\nDevelopment\n-----------\n\nTLDR:\n\n- Create and activate a Python 3.7 virtualenv (assuming virtualenvwrapper)::\n\n    mkvirtualenv -p `which python3.7` my_virtualenv\n\n- change to a branch::\n\n    git checkout -b my_branch\n\n- install Poetry: https://python-poetry.org/docs/#installation\n- Install project deps and pre-commit hooks::\n\n    poetry install\n    pre-commit install\n    pre-commit run --all-files\n\n- Ready to go.\n\nRemember to activate your virtualenv whenever working on the repo, this is needed\nbecause pylint and mypy pre-commit hooks use the "system" python for now (because reasons).\n',
    'author': 'Eero af Heurlin',
    'author_email': 'eero.afheurlin@advian.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/advian-oss/python-libadvian/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
