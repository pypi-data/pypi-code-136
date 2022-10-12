# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fasterrisk']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.3,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'scikit-learn>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'fasterrisk',
    'version': '0.1.1',
    'description': 'Create sparse and accurate risk scoring systems!',
    'long_description': '# fasterrisk <!-- omit in toc -->\n\nThis repository contains source code to our NeurIPS 2022 paper:\n\n**FasterRisk: Fast and Accurate Interpretable Risk Scores**\n\n# Table of Content <!-- omit in toc -->\n- [Introduction](#introduction)\n- [Installation](#installation)\n- [Usage](#usage)\n- [License](#license)\n- [Contributing](#contributing)\n\n\n# Introduction\nOver the last century, risk scores have been the most popular form of predictive model used in healthcare and criminal justice. Risk scores are sparse linear models with integer coefficients; often these models can be memorized or placed on an index card. Below is a risk score example created on the 3rd fold of the [adult dataset](https://github.com/ustunb/risk-slim/tree/master/examples/data) by FasterRisk, predicting salary> 50K.\n\n|                            |             |       |\n| :---                       |    ---:     |  :--- |\n|1.  No High School Diploma  |   -4 points |   ... |\n|2.     High School Diploma  |   -2 points | + ... |\n|3.            Age 22 to 29  |   -2 points | + ... |\n|4.       Any Capital Gains  |    3 points | + ... |\n|5.                 Married  |    4 points | + ... |\n|                            |       SCORE | =     |\n\n|      |        |        |        |        |        |        |        |\n|:---  | :----: | :----: | :----: | :----: | :----: | :----: | :----: | \n|SCORE |  -8.0  |  -6.0  |  -5.0  |  -4.0  |  -3.0  |  -2.0  |  -1.0  |\n|RISK  |   0.1% |   0.4% |   0.7% |   1.2% |   2.3% |   4.2% |   7.6% |\n|SCORE |   0.0  |   1.0  |   2.0  |   3.0  |   4.0  |   5.0  |   7.0  |        \n|RISK  |  13.3% |  22.3% |  34.9% |  50.0% |  65.1% |  77.7% |  92.4% |\n\nTypically, risk scores have been created either without data or by rounding logistic regression coefficients, but these methods do not reliably produce high-quality risk scores. Recent work used mathematical programming, which is computationally slow.\n\nWe introduce an approach for efficiently producing a collection of high-quality risk scores learned from data. Specifically, our approach produces a pool of almost-optimal sparse continuous solutions, each with a different support set, using a beam-search algorithm. Each of these continuous solutions is transformed into a separate risk score through a "star ray" search, where a range of multipliers are considered before rounding the coefficients sequentially to maintain low logistic loss. Our algorithm returns all of these high-quality risk scores for the user to consider. This method completes within minutes and can be valuable in a broad variety of applications.\n\n# Installation\n\n```bash\nconda create -n FasterRisk python=3.9 # create a virtual environment\nconda activate FasterRisk # activate the virtual environment\npython -m pip install fasterrisk # pip install the fasterrisk package\n```\n\n\n# Usage\nPlease see the [example.ipynb](./docs/example.ipynb) jupyter notebook for a detailed tutorial on how to use FasterRisk in a python environment.\n\nThere are two major two classes for the users to interact with:\n- **RiskScoreOptimizer**\n```python\nsparsity = 5 # produce a risk score model with 5 nonzero coefficients \n\n# import data\nX_train, y_train = ...\n\n# initialize a risk score optimizer\nm = RiskScoreOptimizer(X = X_train, y = y_train, k = sparsity)\n\n# perform optimization\nm.optimize()\n\n# get all top m solutions from the final diverse pool\narr_multiplier, arr_intercept, arr_coefficients = m.get_models() # get m solutions from the diverse pool; Specifically, arr_multiplier.shape=(m, ), arr_intercept.shape=(m, ), arr_coefficients.shape=(m, p)\n\n# get the first solution from the final diverse pool by passing an optional model_index; models are ranked in order of increasing logistic loss\nmultiplier, intercept, coefficients = m.get_models(model_index = 0) # get the first solution (smallest logistic loss) from the diverse pool; Specifically, multiplier.shape=(1, ), intercept.shape=(1, ), coefficients.shape=(p, )\n\n```\n\n- **RiskScoreClassifier**\n```python\n# import data\nX_featureNames = ... # X_featureNames is a list of strings, each of which is the feature name\n\n# create a classifier\nclf = RiskScoreClassifier(multiplier = multiplier, intercept = intercept, coefficients = coefficients, featureNames = featureNames)\n\n# get the predicted label\ny_pred = clf.predict(X = X_train)\n\n# get the probability of predicting y[i] with label +1\ny_pred_prob = clf.predict_prob(X = X_train)\n\n# compute the logistic loss\nlogisticLoss_train = clf.compute_logisticLoss(X = X_train, y = y_train)\n\n# get accuracy and area under the ROC curve (AUC)\nacc_train, auc_train = clf.get_acc_and_auc(X = X_train, y = y_train) \n\n# print the risk score model card\nm.print_model_card() \n```\n\n# License\n\n`fasterrisk` was created by Jiachang Liu. It is licensed under the terms of the BSD 3-Clause license.\n\n# Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n# Credits <!-- omit in toc -->\n\n`fasterrisk` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Jiachang Liu',
    'author_email': 'jiachang.liu@duke.edu',
    'maintainer': 'Jiachang Liu',
    'maintainer_email': 'jiachang.liu@duke.edu',
    'url': 'https://pypi.org/project/fasterrisk/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
