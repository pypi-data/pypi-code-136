# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['empaia_app_test_suite',
 'empaia_app_test_suite.models',
 'empaia_app_test_suite.models.annotation',
 'empaia_app_test_suite.models.tests',
 'empaia_app_test_suite.py_ead_validation',
 'empaia_app_test_suite.py_ead_validation.py_ead_validation',
 'empaia_app_test_suite.py_ead_validation.py_ead_validation.indepth',
 'empaia_app_test_suite.py_ead_validation.tests']

package_data = \
{'': ['*'],
 'empaia_app_test_suite.models': ['.gitlab/issue_templates/*',
                                  '.gitlab/merge_request_templates/*'],
 'empaia_app_test_suite.py_ead_validation': ['.gitlab/issue_templates/*',
                                             '.gitlab/merge_request_templates/*'],
 'empaia_app_test_suite.py_ead_validation.py_ead_validation': ['definitions/*',
                                                               'definitions/.gitlab/issue_templates/*',
                                                               'definitions/.gitlab/merge_request_templates/*',
                                                               'definitions/ead/*',
                                                               'definitions/namespaces/*',
                                                               'definitions/tags/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'docker>=6.0.0,<7.0.0',
 'jsonschema>=4.4.0,<5.0.0',
 'prettytable>=3.2.0,<4.0.0',
 'pydantic[dotenv]>=1.9.0,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'toml>=0.10.2,<0.11.0',
 'typer>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['eats = empaia_app_test_suite.cli:app',
                     'empaia-app-test-suite = empaia_app_test_suite.cli:app']}

setup_kwargs = {
    'name': 'empaia-app-test-suite',
    'version': '2.0.23',
    'description': 'The EMPAIA App Test Suite (EATS)',
    'long_description': '# EMPAIA App Test Suite (EATS)\n\n## Requirements\n\n* The EMPAIA App Test Suite requires Python 3.8.\n* Supported Operating Systems are Linux, Windows and MacOS\n  * for **Windows** the EATS requires the usage of WSL 2 (Windows Subsystem for Linux) with Docker for Windows\n\n## Installation\n\nThere are different possibilities to install the EMPAIA App Test Suite depending on your intended use:\n\n* Installation as App Developer\n  * Latest stable release\n  * Latest test release\n* Build and installation as EATS Developer\n\n### Installation as App Developer - Latest stable release\n\nInstallation via `pip` from Python Package Index (PyPI).\n\n```bash\n# create virtual environment (recommended)\npython3 -m venv .venv\nsource .venv/bin/activate\n\n# install with pip\npip install empaia-app-test-suite\n```\n\n### Installation as App Developer - Latest test release\n\nInstallation via `pip` from Python Package Index Test Repository (Test.PyPI).\n\n```bash\n# create virtual environment (recommended)\npython3 -m venv .venv\nsource .venv/bin/activate\n\n# install with pip from test.pypi.org\npip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ empaia-app-test-suite\n```\n\n### Build and installation as EATS Developer\n\nClone the EATS source code repository.\n\nThis module uses submodules, i.e. references to other git repositories. Add `--recurse-submodule` to your clone command to also get all submodules, e.g.\n\n```bash\ngit clone --recurse-submodule https://gitlab.com/empaia/integration/empaia-app-test-suite.git\ncd empaia-app-test-suite\n### also after changing branch\ngit submodule update --init --recursive\n```\n\nBuild the EATS CLI app and install all needed dependencies:\n\n```bash\n# create virtual environment (recommended)\npython3 -m venv .venv\nsource .venv/bin/activate\n\n# build / install EATS and dependencies\npoetry install\n```\n\n## Run EATS\n\nRun the EATS CLI app with\n\n```bash\neats\n```\n\nTo force pull and build services and submodules:\n\n```bash\neats services up ./wsi-mount-points.json --build --pull\n```\n\n## Usage\n\n**For detailed instructions take a look at the [App Developer Documentation](https://developer.empaia.org/app_developer_docs/#/)**\n\nDefine absolute paths to directories containing WSIs in a `./wsi-mount-points.json` file as follows:\n\n```json\n{\n    "/absolute/local/path/to/wsis/dir1": "/absolute/container/mount/dir1/",\n    "/absolute/local/path/to/wsis/dir2": "/absolute/container/mount/dir2/"\n}\n```\n\nStart all backend services in Docker containers using the `eats services up` command. WSI directories are mounted into the WSI Service container. Only WSIs contained in one of the specified directories can be used as a job input.\n\n```bash\neats services up ./wsi-mount-points.json\n```\n\nYou can perform health checks of running backend services.\n\n```bash\neats services health\n```\n\nRegister your app with its `<docker-image-name>` (can be fully qualified docker registry url, e.g. `registry.gitlab.com/empaia/integration/sample-apps/org-empaia-vendor_name-tutorial_app_01:v1`). Also provide the path to your `ead.json`. If your app required configuration parameters, use the `--config-file` flag to specify the path to you `configuration.json`.\n\n```bash\neats apps register <path-to-ead.json> <docker-image-name> > app.env\n\n# or with configuration\n\neats apps register <path-to-ead.json> <docker-image-name> --config-file <path-to-configuration.json> > app.env\n\n# export the app id for later use\n\nexport $(xargs <app.env)\necho $APP_ID\n```\n\nUse the APP_ID together with your JSON files for your data inputs in a `job-inputs` directory to register ar new job.\n\n```bash\neats jobs register $APP_ID <path-to-job-inputs> --v1 > job.env\n```\n\nThe generated `job.env` file contains the `EMPAIA_JOB_ID`, `EMPAIA_TOKEN`, and `EMPAIA_APP_API` environment variables, that are handed to your app during the `eats jobs run` step.\n\n```bash\neats jobs run ./job.env\n```\n\nThe job ID can be retrieved from the `job.env` file to be used in other commands.\n\n```bash\nexport $(xargs <job.env)\necho $EMPAIA_JOB_ID\n```\n\nRegularly check the jobs status until it is `COMPLETED`.\n\n```bash\neats jobs status ${EMPAIA_JOB_ID}\n```\n\nThe job ID is used as the container name. It can be used to retrieved docker logs.\n\n```bash\ndocker logs ${EMPAIA_JOB_ID}\n```\n\nOpen `localhost:8888/wbc` in a Browser to review job results using the Workbench Client 1.0.\n\nIn addition, the job results can be exported to JSON files in a `job-outputs` directory.\n\n```bash\neats jobs export ${EMPAIA_JOB_ID} ./job-outputs\n```\n\nIf a job is taking too long or is stuck, the job can be aborted.\n\n```bash\neats jobs abort ${EMPAIA_JOB_ID}\n```\n\nTo inspect backend service logs the `docker logs` command can used directly. The names of all service containers can be retrieved using the `eats services list` command.\n\n```bash\neats services list  # print list of service names\ndocker logs ${SERVICE_NAME}\n```\n\nIt is possible to register and run multiple jobs without restart backend services. The services can be stopped, if they are not needed anymore. All created data is available when the services are started again.\n\n```bash\neats services down\n```\n\nTo erase all created data use `eats services down -v` to remove all created docker volumes or `docker volume rm` directly.\n\n```bash\neats services down -v\n\n# or\n\ndocker volume rm $(eats services volumes)\n```\n\n## Executing Your App without Job Execution Service\n\nThe command `eats jobs run $EMPAIA_JOB_ID <job.env-file>` sends a request to the Job Execution Service, which start your containerized app. Debugging your app this way can be tedious and time consuming. To speed up the debugging process, you can also start your app natively:\n\n1. Start services as usual.\n\n```bash\neats services up ./wsi-mount-points.json\n```\n\n2. Register app as usual, receiving the `APP_ID`\n\n```bash\neats apps register <path-to-ead.json> <docker-image-name> --config-file <path-to-configuration.json> > app.env\nexport $(xargs <app.env)\necho $APP_ID\n```\n\n3. Register job and export to `job.env`, e.g.\n\n```bash\neats jobs register $APP_ID <eats-inputs-folder> --v1 > job.env\nexport $(xargs <job.env)\necho $EMPAIA_JOB_ID\n```\n\n4. Overwrite the `EMPAIA_APP_API` value with `localhost:<NGINX-PORT>/app-api` (the exposed port of the NGINX proxy server is `8888` by default):\n\n```bash\nexport EMPAIA_APP_API=http://localhost:8888/app-api\n```\n\n5. Set job to status `RUNNING` (without actually running it):\n\n```bash\neats jobs set-running $EMPAIA_JOB_ID\n```\n\n6. Run your app, e.g.:\n\n```bash\npython3 <path-to-app.py>\n```\n\n7. Make changes to your app.py and **GO TO 3.**\n\n## For EATS Developers\n\n### Code Checks\n\nCheck your code before committing.\n\n* always format code with `black` and `isort`\n* check code quality using `pycodestyle` and `pylint`\n  * `black` formatting should resolve most issues for `pycodestyle`\n\n```bash\nisort .\nblack empaia_app_test_suite tests check_version.py\npycodestyle empaia_app_test_suite tests check_version.py\npylint empaia_app_test_suite tests check_version.py\n```\n\n### Tests\n\nCreate `./wsi-mount-points.json`:\n\n```JSON\n{\n  "/path/to/testdata/Aperio/": "/data",\n  "/path/to/testdata/Fluorescence OME-Tif/": "/data2"\n}\n```\n\n```bash\neats services up ./wsi-mount-points.json --build --pull\n\n# run cli command tests\npytest tests/commands --maxfail=1 -s -v\n\n# run sample apps tests\npytest tests/sample_apps_tests --maxfail=1 -s -v\n```\n\nIf a test from `tests/sample_apps` fails, use `docker logs <servicename>` for debugging.\n\n### Test GPU support\n\n```bash\neats services up ./wsi-mount-points.json --build --pull --gpu-driver nvidia\n\n# run cli command test\npytest tests/gpu_support_test\n```\n\nIf docker is locally installed with support for CUDA and a supported GPU is available on the host system the test must succeed. If the test fails please check if docker is correctly installed.\n',
    'author': 'EMPAIA',
    'author_email': 'dev-support@empaia.org',
    'maintainer': 'EMPAIA',
    'maintainer_email': 'dev-support@empaia.org',
    'url': 'https://developer.empaia.org/app_developer_docs/#/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
