# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['umlaut', 'umlaut.examples']

package_data = \
{'': ['*']}

install_requires = \
['mlflow==1.28.0', 'psycopg2==2.9.3']

setup_kwargs = {
    'name': 'umlaut',
    'version': '0.1.0',
    'description': 'Umlaut simplifies deploying data science models',
    'long_description': '# uMLaut\n\nThe uMLaut library simplifies data science model deployment and querying. It provides a single access point for all your models and an interface to interact with them. uMLaut models can be as extensive as deep learning models or as simple as a reusable code block.\n\nuMLaut offers\n- simple commands to track and query models\n- history of all model query inputs and results\n- model lifecycle management\n- access to multiple versions of the same model\n- a user interface with `MLflow`\n- model audit tracking history (roadmap)\n- auto-deployed models that can be queried through an API (roadmap)\n\n## MLflow Setup\n[MLflow](https://bit.ly/3eHJsx3) is a powerful machine learning library created by Databricks for data science teams. It offers an extensive API for tracking and querying models, but the learning curve can be a deterrent for small teams without dedicated data scientists. uMLaut strips away much of the complexity of MLflow while maintaining the immense value of tracking and querying your models in a single location. \n\nMLflow has two requirements:\n1) A model artifact storage location\n- This can be a local directory or a cloud storage URI. More info in the MLflow [docs](https://mlflow.org/docs/latest/tracking.html#artifact-stores).\n2) A model registry\n- The model registry is where model changes and query data are stored. More info in the MLflow [docs](https://mlflow.org/docs/latest/tracking.html#backend-stores).\n\nAn `mlflow server` must be running in order to work with uMLaut. The command to start an MLflow server with local artifact storage and a Postgres model registry is as follows:\n\n`mlflow server --backend-store-uri postgresql+psycopg2://admin:password@localhost:5432/database --default-artifact-root "mlruns/"`\n\nOnce the server is running you can navigate to the MLflow UI and begin interacting with models.\n\n____\n## Core Functionality\nuMLaut offers a simple Python class to assist with saving and querying business logic in MLflow.\n\n- `track_model`: Converts a data science model or block of business logic into an MLflow compatible `model`\n- `query_model`: Queries a previously trained `model` and saves audit metadata\n- `track_dataset (roadmap)`: Saves reporting datasets along with the initial query and underlying data that built it (roadmap)\n- `audit_model (roadmap)`: Retrieve the results of a model run for a historic date\n- `audit_dataset (roadmap)`: Retrieve a dataset as it was on a historic date\n\n### Deploying models with Umlaut\nCustom data science models or business logic can be deployed simply by running `umlaut.track_model()`. Ensure the model code block is in a Python `Class` and follow the example below.\n\n```\nclass ExampleModel():\n    """\n    Example business logic that can be wrapped into a model.\n    The class _must_ contain a \'predict\' method.\n    """\n    def business_logic(self, revenue: int) -> bool:\n        if revenue > 5:\n            return True\n        else:\n            return False\n\n    def predict(self, model_input: dict) -> bool:\n        return self.business_logic(revenue=model_input.get("revenue"))\n\n\nif __name__ == "__main__":\n    """Saves the model to MLflow in an experiment run"""\n    from core import Umlaut\n\n    umlaut = Umlaut()\n    umlaut.track_model(\n        model=ExampleModel(),\n        model_name="Quarterly Revenue",\n        run_name="Update",\n    )\n```\n\nThis will push the latest changes of `ExampleModel()` to MLflow as a new model version. Navigate to the MLflow server where you can find details for the example "Quarterly Revenue" model.\n\n\n### Querying models with Umlaut\nOnce a model is deployed in MLflow with `umlaut.track_model()`, it can be queried by calling `umlaut.query_model()`.\n\n```\nfrom core import Umlaut\n\numlaut = Umlaut()\nresult = umlaut.query_model(\n    model_name="Quarterly Revenue",\n    input_config={"revenue": 3},\n    stage="Staging",\n)\nprint(f"Revenue will{\'\' if result else \' not\'} exceed target")\n```\n\nIf we query the simple `Quarterly Revenue` example model with `revenue = 3`, the model will return `False` as the revenue does not exceed the target of 5. The call to the model will be tracked in MLflow with model inputs and results.\n',
    'author': 'Andrew Dunkel',
    'author_email': 'andrew.dunkel1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/andrewdunkel/uMLaut',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.12,<4.0',
}


setup(**setup_kwargs)
