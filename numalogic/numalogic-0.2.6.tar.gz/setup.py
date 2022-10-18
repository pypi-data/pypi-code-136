# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numalogic',
 'numalogic.models',
 'numalogic.models.autoencoder',
 'numalogic.models.autoencoder.variants',
 'numalogic.models.forecast',
 'numalogic.models.forecast.variants',
 'numalogic.preprocess',
 'numalogic.registry',
 'numalogic.synthetic',
 'numalogic.tests',
 'numalogic.tests.models',
 'numalogic.tests.models.autoencoder',
 'numalogic.tests.models.autoencoder.variants',
 'numalogic.tests.models.forecast',
 'numalogic.tests.preprocess',
 'numalogic.tests.registry',
 'numalogic.tests.synthetic',
 'numalogic.tests.tools',
 'numalogic.tools']

package_data = \
{'': ['*'], 'numalogic.tests': ['resources/data/*']}

install_requires = \
['numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pytz>=2022.1,<2023.0',
 'scikit-learn>=1.0,<2.0',
 'torch>=1.12.0,<2.0.0',
 'torchinfo>=1.6.0,<2.0.0']

extras_require = \
{'mlflow': ['mlflow>=1.27.0,<2.0.0']}

setup_kwargs = {
    'name': 'numalogic',
    'version': '0.2.6',
    'description': 'Collection of operational Machine Learning models and tools.',
    'long_description': '# numalogic\n\n[![Build](https://github.com/numaproj/numalogic/actions/workflows/ci.yml/badge.svg)](https://github.com/numaproj/numalogic/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/numaproj/numalogic/branch/main/graph/badge.svg?token=020HF97A32)](https://codecov.io/gh/numaproj/numalogic)\n[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)\n[![slack](https://img.shields.io/badge/slack-numaproj-brightgreen.svg?logo=slack)](https://join.slack.com/t/numaproj/shared_invite/zt-19svuv47m-YKHhsQ~~KK9mBv1E7pNzfg)\n[![Release Version](https://img.shields.io/github/v/release/numaproj/numalogic?label=numalogic)](https://github.com/numaproj/numalogic/releases/latest)\n\n\n## Background\nNumalogic is a collection of ML models and algorithms for operation data analytics and AIOps. \nAt Intuit, we use Numalogic at scale for continuous real-time data enrichment including \nanomaly scoring. We assign an anomaly score (ML inference) to any time-series \ndatum/event/message we receive on our streaming platform (say, Kafka). 95% of our \ndata sets are time-series, and we have a complex flowchart to execute ML inference on \nour high throughput sources. We run multiple models on the same datum, say a model that is \nsensitive towards +ve sentiments, another more tuned towards -ve sentiments, and another \noptimized for neutral sentiments. We also have a couple of ML models trained for the same \ndata source to provide more accurate scores based on the data density in our model store. \nAn ensemble of models is required because some composite keys in the data tend to be less \ndense than others, e.g., forgot-password interaction is less frequent than a status check \ninteraction. At runtime, for each datum that arrives, models are picked based on a conditional \nforwarding filter set on the data density. ML engineers need to worry about only their \ninference container; they do not have to worry about data movement and quality assurance.\n\n## Numalogic realtime training \nFor an always-on ML platform, the key requirement is the ability to train or retrain models \nautomatically based on the incoming messages. The composite key built at per message runtime \nlooks for a matching model, and if the model turns out to be stale or missing, an automatic \nretriggering is applied. The conditional forwarding feature of the platform improves the \ndevelopment velocity of the ML developer when they have to make a decision whether to forward \nthe result further or drop it after a trigger request.\n\n\n## Installation\n\nnumalogic can be installed using pip.\n```shell\npip install numalogic\n```\n\nIf using mlflow for model registry, install using:\n```shell\npip install numalogic[mlflow]\n```\n\n### Build locally\n\n1. Install [Poetry](https://python-poetry.org/docs/):\n    ```\n    curl -sSL https://install.python-poetry.org | python3 -\n    ```\n2. To activate virtual env:\n    ```\n    poetry shell\n    ```\n3. To install dependencies:\n    ```\n    poetry install\n    ```\n   If extra dependencies are needed:\n    ```\n    poetry install --all-extras\n    ```\n4. To run unit tests:\n    ```\n    make test\n    ```\n5. To format code style using black:\n    ```\n    make lint\n    ```\n\n## Usage\nThe following example shows a series of operations that can be performed using the package.\n### Generate synthetic data\nLet\'s start with generating some synthetic time series data using numalogic\'s synthetic module.\n```python\nfrom numalogic.synthetic import SyntheticTSGenerator\n\nts_generator = SyntheticTSGenerator(\n    seq_len=8000,\n    num_series=3,\n    freq="T",\n    primary_period=720,\n    secondary_period=6000,\n    seasonal_ts_prob=0.8,\n    baseline_range=(200.0, 350.0),\n    slope_range=(-0.001, 0.01),\n    amplitude_range=(10, 75),\n    cosine_ratio_range=(0.5, 0.9),\n    noise_range=(5, 15),\n)\nts_df = ts_generator.gen_tseries()  # shape: (8000, 3) with column names [s1, s2, s3]\n\n# Split into test and train\ntrain_df, test_df = ts_generator.train_test_split(ts_df, test_size=1000)\n```\n![Train and Test sets](images/train_test.png)\n\n### Generate synthetic anomalies\nNow we will add "contextual" anomalies in the test set, using numalogic\'s AnomalyGenerator.\nContextual is one of the different types of anomalies that can be imputed. Others include "point", "collective"\nand "causal".\n```python\nfrom numalogic.synthetic import AnomalyGenerator\n\ninjected_cols = ["s1", "s2"]  # columns to inject anomalies\nanomaly_generator = AnomalyGenerator(\n    train_df, anomaly_type="contextual", anomaly_ratio=0.3\n)\noutlier_test_df = anomaly_generator.inject_anomalies(\n    test_df, cols=injected_cols, impact=1.5\n)\n```\n![Outliers](images/outliers.png)\n\n### Model training \nLet\'s use one of the available models to train on generated data.\nHere we are going to use a sparse convolutional Autoencoder.\nWe can start by scaling the data.\n```python\nfrom sklearn.preprocessing import MinMaxScaler\nfrom numalogic.models.autoencoder.variants import Conv1dAE\nfrom numalogic.models.autoencoder.pipeline import SparseAEPipeline\n\n# Scale the train and test sets.\nscaler = MinMaxScaler()\nX_train = scaler.fit_transform(train_df.to_numpy())\n\n# Define the model and train\nseq_len = 36\n# SparseAEPipeline is a sparse autoencoder trainer that follows sklearn\'s API pattern\nmodel = SparseAEPipeline(\n    model=Conv1dAE(in_channels=3, enc_channels=8), seq_len=seq_len, num_epochs=30\n)\nmodel.fit(X_train)\n```\n\n### Model saving\nNow that the model is trained, let\'s save it. Numalogic has built in support \nfor Mlflow\'s tracking and logging system.\n\nLet\'s first start the [mlflow server on localhost](https://www.mlflow.org/docs/latest/tracking.html#scenario-1-mlflow-on-localhost),\nwhich has already been installed optionally via `poetry` dependency:\n```shell\nmlflow server \\\n        --default-artifact-root {directory}/mlruns --serve-artifacts \\\n        --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 5000\n```\n```python\nfrom numalogic.registry import MLflowRegistrar\n\n# static and dynamic keys are used to look up a model\nstatic_keys = ["synthetic", "3ts"]\ndynamic_keys = ["minmaxscaler", "sparseconv1d"]\n\nregistry = MLflowRegistrar(tracking_uri="http://0.0.0.0:5000", artifact_type="pytorch")\nregistry.save(\n   skeys=static_keys, \n   dkeys=dynamic_keys, \n   primary_artifact=model, \n   secondary_artifacts={"preproc": scaler}\n)\n```\n\n### Model loading\nLet\'s now load the model for inference on test data\n```python\nregistry = MLflowRegistrar(tracking_uri="http://0.0.0.0:8080")\nartifact_dict = registry.load(\n    skeys=static_keys, dkeys=dynamic_keys\n)\nscaler = artifact_dict["secondary_artifacts"]["preproc"]\nmodel = artifact_dict["primary_artifact"]\n```\n\n### Model inference\nFinally, let\'s use the loaded artifacts to predict on the anomalous test data.\nThis can be a streaming or a batched data.\n```python\nX_test = scaler.transform(outlier_test_df.to_numpy())\n\n# predict method returns the reconstruction produced by the AE\ntest_recon = model.predict(X_test)\n\n# score method returns the anomaly score, calculated using thresholds.\n# A number less than 1 indicates an inlier, and greater than 1 indicates an outlier.\ntest_anomaly_score = model.score(X_test)\n```\n![Reconstruction](images/recon.png)\n![Anomaly Score](images/anomaly_score.png)\n\n## Contributing\nWe would love contributions in the numalogic project in one of the following (but not limited to) areas:\n\n- Adding new time series anomaly detection models\n- Making it easier to add user\'s custom models\n- Support for additional model registry frameworks\n\nFor contribution guildelines please refer [here](https://github.com/numaproj/numaproj/blob/main/CONTRIBUTING.md).',
    'author': 'Numalogic Developers',
    'author_email': 'None',
    'maintainer': 'Avik Basu',
    'maintainer_email': 'avikbasu93@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
