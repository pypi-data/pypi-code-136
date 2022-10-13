# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bluetarget']

package_data = \
{'': ['*']}

install_requires = \
['click==8.1.3']

setup_kwargs = {
    'name': 'bluetarget',
    'version': '0.1.6',
    'description': 'Deploy, monitor and explain your machine learning models',
    'long_description': '# BlueTarget\n\n**Deploy, monitor and explain machine learning models.**\n\n![Logo](https://deploy.bluetarget.ai/statics/bt.jpg)\n\nBlueTarget is a MLops platform which allows ML engineer and Data Science deploy, monitor and explain their machine learning models. We\'re able to deploy your model using different kind of strategies like A/B testing, Canary or Rolling update.\n\nGet started with the [BlueTarget](https://docs.deploy.bluetarget.ai).\n\n## What can I do with BlueTarget?\n\nIf you\'ve ever tried to get a model out of a Jupyter notebook, BlueTargert is for you.\n\nBlueTarget allow your to deploy your ML model taking away the whole complexity of the cloud. However If you prefer to have the control of the infrastructure, BlueTarget can work with your preferred cloud:\n\nHere are some of the things BlueTarget does:\n\n- Turns your Python model into a microservice with a production-ready API endpoint, no need for Flask or Django.\n- Track your model\'s version and metadata\n- Understad the drift of your model\n- Track your inference\n- Deployment strategies like A/B testing, canary and rolling update\n\n## Installation\n\nBlueTarget requires Python >=3.7\n\nTo install from [PyPi](https://pypi.org/project/bluetarget/), run:\n\n```\npip install bluetarget\n```\n\nBlueTarget is actively developed, and we recommend using the latest version. To update your BlueTarget installation, run:\n\n```\npip install --upgrade bluetarget\n```\n\n## How to use BlueTarget\n\n### Quickstart: making a BlueTarget\n\n#### train.py\n\n```python\n!pip install --upgrade scikit-learn bluetarget pickle-mixin\n\nfrom sklearn import svm\nfrom sklearn import datasets\n\nimport pickle\n\n# Load training data set\niris = datasets.load_iris()\nX, y = iris.data, iris.target\n\n# Train the model\nclf = svm.SVC(gamma=\'scale\')\nclf.fit(X, y)\n\npickle.dump(clf, open(\'model.pkl\', \'wb\'))\n\n```\n\n#### service.py\n\n```python\nimport os\nfrom typing import Dict, List\n\nclass Model:\n    def __init__(self) -> None:\n        self._model = None\n\n    def load(self):\n        import pickle\n\n        with open(f"{os.path.dirname(__file__)}/model.pkl", \'rb\') as pickle_file:\n            self._model = pickle.load(pickle_file)\n\n    def predict(self, request: Dict) -> Dict[str, List]:\n        response = {}\n        inputs = request["inputs"]\n        result = self._model.predict(inputs).tolist()\n        response["predictions"] = result\n\n        return response\n```\n\n#### requirements.txt\n\n```\nscikit-learn==1.0.2\npickle-mixin==1.0.2\n```\n\n#### deploy.py\n\n```python\nfrom bluetarget import BlueTarget\n\nbt = BlueTarget(api_key="YOUR_API_KEY")\n\nbt.deploy(\n    model_name="YourFirstModel",\n    model_class="Model",\n    model_files=["model.py", "model.pkl"],\n    requirements_file="requirements.txt"\n)\n\ninputs = [\n    [6.9, 3.1, 5.1, 2.3],\n    [5.8, 2.7, 5.1, 1.9],\n    [6.8, 3.2, 5.9, 2.3],\n    [6.7, 3.3, 5.7, 2.5],\n    [6.7, 3.,  5.2, 2.3],\n    [6.3, 2.5, 5.,  1.9],\n    [6.5, 3.,  5.2, 2.],\n    [6.2, 3.4, 5.4, 2.3],\n    [5.9, 3.,  5.1, 1.8]\n]\n\nbt.predict(inputs)\n\n# {\n#     "predictions": [\n#         2,\n#         1,\n#         2,\n#         3,\n#         0,\n#         2,\n#         3,\n#         2,\n#         1\n#     ]\n# }\n\n```\n',
    'author': 'Sergio Kaz',
    'author_email': 'sergio@bluetarget.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
