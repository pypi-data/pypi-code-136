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
    'version': '0.0.3',
    'description': 'Umlaut simplifies deploying data science models',
    'long_description': '# uMLaut\n\nThe uMLaut library simplifies model deployment and querying. It provides a single\naccess point for all of your organizations models and an interface to interact with them. Umlaut `models` can be as extensive as deep learning models or as simple as a reusable code block.\n\nuMLaut offers...\n- simple model lifecycle management\n- easy model maintenance\n- access to multiple versions of the same model\n- business logic sharing\n- a user interface with `MLflow`\n- audit tracking history (roadmap)\n- auto-deployed models that can be queried through an API (roadmap)\n\n____\n## Umlaut Class\nA Python class to assist with saving and querying business logic.\n\n- `track_model`: Converts a data science model or block of business logic into an uMLaut compatible `model`\n- `query_model`: Queries a previously trained `model` and saves audit metadata\n- `track_dataset (roadmap)`: Saves reporting datasets along with the initial query and underlying data that built it (roadmap)\n- `audit_model (roadmap)`: Retrieve the results of a model run for a historic date\n- `audit_dataset (roadmap)`: Retrieve a dataset as it was on a historic date\n\n### Deploying models with Umlaut\nCustom data science models or business logic can be deployed simply by running `umlaut.track_model()`. Ensure the model code block is in a Python `Class` and follow the example below.\n\n```\nclass ExampleModel():\n    """\n    Example business logic that can be wrapped into a model.\n    The class _must_ contain a \'predict\' method.\n    """\n    def business_logic(self, revenue: int) -> bool:\n        if revenue > 5:\n            return True\n        else:\n            return False\n\n    def predict(self, model_input: dict) -> bool:\n        return self.business_logic(revenue=model_input.get("revenue"))\n\n\nif __name__ == "__main__":\n    """Saves the model to MLflow in an experiment run"""\n    from core import Umlaut\n\n    umlaut = Umlaut()\n    umlaut.track_model(\n        model=ExampleModel(),\n        model_name="Quarterly Revenue",\n        run_name="Update",\n    )\n```\n\nThis will push the latest changes of `ExampleModel()` to MLflow as a new model version. Navigate to the MLflow Tracking Server to find the latest push and associate it to the MLflow model.\n\n\n### Querying models with Umlaut\nOnce a model is deployed in MLflow with `umlaut.track_model()`, it can be queried by calling `umlaut.query_model()`.\n\n```\nfrom core import Umlaut\n\numlaut = Umlaut()\nresult = umlaut.query_model(\n    model_name="Quarterly Revenue",\n    input_config={"revenue": 3},\n    stage="Staging",\n)\nprint(f"Revenue will{\'\' if result else \' not\'} exceed target")\n```\n\nIf we query the simple `Quarterly Revenue` example model with `revenue = 3`, the model will return `False` as the revenue does not exceed the target of 5.\n',
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
