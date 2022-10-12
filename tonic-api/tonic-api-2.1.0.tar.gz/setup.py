# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tonic_api', 'tonic_api.classes', 'tonic_api.services']

package_data = \
{'': ['*']}

install_requires = \
['more-itertools>=8.6.0,<9.0.0',
 'pandas>=1.0.0,<2.0.0',
 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'tonic-api',
    'version': '2.1.0',
    'description': 'Wrappers around the Tonic.ai API',
    'long_description': '# Overview\nThis library contains useful wrappers around the Tonic.ai API.\n\n## Usage\n\nInstantiate the API wrapper using the following code:\n\n```\nfrom tonic_api.api import TonicApi\n\n# Do not include trailing backslash in TONIC_URL\napi = TonicApi(TONIC_URL, API_KEY)\n```\n\nOnce instantiated, the following endpoints are available for consumption. Note that available endpoints and response types are limited. Available fields may be severely limited compared to the current Tonic API.\n\n```\nTonicApi:\n    get_workspace(workspace_id) => Workspace\n\nWorkspace:\n    id => string\n    name => string\n    models => Model[]\n\n    train(model_id) => new job ID\n    get_trained_model_by_training_job_id(job_id) => TrainedModel (or None if training is not done)\n    get_training_status_by_training_job_id(job_id) => TrainingJobStatus\n    get_most_recent_trained_model_by_model_id => TrainedModel\n\n    describe() => debugger helper for printing fields\n\nModel:\n    id => string\n    name => string\n    query => string\n    parameters => {}\n    encodings => {}\n\n    describe() => debugger helper for printing fields\n\nTrainedModel:\n    id => string\n    job_id => string\n    model => Model\n\n    sample(num_rows) => pandas DataFrame (defaults to 1 row if num_rows not provided)\n    sample_source(num_rows) => pandas DataFrame (defaults to 1 row if num_rows not provided). Note: NOT randomized. Upper limit is limited to row count in source.\n\n    get_numeric_columns() => string[]\n    get_categorical_columns() => string[]\n\n    describe() => debugger helper for printing fields\n\nTrainingJobStatus:\n    state => string\n    error => string[] or None\n    tasks => {}\n\n    current_epoch_progress() => dict or None\n\n    describe() => debugger helper for printing fields\n```\n',
    'author': 'Eric Timmerman',
    'author_email': 'eric@tonic.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.tonic.ai/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
