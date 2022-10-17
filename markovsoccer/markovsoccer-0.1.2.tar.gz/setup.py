# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markovsoccer']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.0,<4.0.0',
 'matplotsoccer>=0.0.8,<0.0.9',
 'pandas>=1.5.0,<2.0.0',
 'seaborn>=0.12.0,<0.13.0',
 'setuptools>=65.4.1,<66.0.0',
 'sklearn>=0.0,<0.1',
 'socceraction==1.2.3',
 'statsbombpy>=1.5.0,<2.0.0',
 'tables>=3.7.0,<4.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'markovsoccer',
    'version': '0.1.2',
    'description': 'Implementation of the construction of Markov models representing the offensive style of play of soccer teams, and analysis based on these models.',
    'long_description': "# Markovsoccer\nMarkovsoccer is a Python package to construct and inspect team models representing the offensive behaviour of soccer\nteams. In particular, it provides a function to build a team model based on event stream data of that team. This model\nrepresents their ball possession sequences. The team model is able to capture the sequential nature of the game and has\nthe ability to generalize over the historical actions that a team has performed in the past. This package implements the\ncalculation of several numerical features to analyze the playing style of teams based on these models. These features\nare related to a team's preference for certain locations, their preference for certain sequences, their directness of\nplay, and their ability to create shooting opportunities. \n\n## Core Features\n- **Construct Team Models**: implementation of a function to construct team models based on the \n  (vendor-independent) \n  SPADL event stream data format.\n- **Analyze Playing Style**: implementation of several numerical features to analyze the offensive playing style of \n  soccer teams based on these team models.\n\n## Installation\nThe recommended way to install this package is using pip. The latest version officially supports Python versions 3.8 - \n3.10.\n\n```\npip install markovsoccer\n```\n\nThe [public-notebooks](./public-notebooks) folder contains several demos to get started.\n\n## Benefits of the Team Model\nThe use of the intermediate team models to analyze the playing style of teams has two advantages:\n- It captures the sequential aspect of the game.\n- It has the ability to generalize over the historical actions that a team has performed in the past.\n\n**Overview of the Team Model:** The figure below provides an overview of the states and transitions of the team \nmodel. Each transition is associated with a team-dependent probability. This probability is equal to the historical \nfrequency of the corresponding action by that team.\n\n![](docfiles/model.png)\n\n**Generalization:** The generalization ability stems from the assumption that if a team has a high likelihood of moving \nthe ball from position A to B, and also a high likelihood of moving the ball prom B to C, then this team is assumed to\nalso have a high likelihood of consecutively moving the ball from A to B to C. This assumption allows the model to\nderive new ways how a team can score a goal, arrive at a shot, or move the ball to a particular location. This is\ndone by interleaving historical ball possession sequences. By doing so, it is hypothesized that analysis of the playing\nstyle based on the model is more reliable. As an example, playing style analysis based on raw event stream data only has\na small number of shots and goals which can be analyzed, leading to skewed results. However, analysis based on the model\ncan take into account (tens of) thousands of ways to arrive at a shot or score a goal, each which their own probability.\nThis leads to a more all-encompassing view and less skewed results.\n\nThe figure below visualizes the generalization ability. Imagine a first sequence representing a goal as in the left\nimage. Then image a second sequence ending in a ball loss as in the middle image. The model will then be able to derive\na new way how a team can score a goal by interleaving these two sequences. The resulting sequence is shown in the right \nimage.\n\n![](docfiles/generalization.png)\n\n**Probabilistic Model Checking:** The team model is a discrete-time Markov chain and can be used for probabilistic \nmodel checking. In particular, this package provides functionality to write each team model to disk as a PRISM file \nfor use in the [PRISM](https://www.prismmodelchecker.org/) model checker. Examples can be found in the \n[public-notebooks](./public-notebooks) folder.\n\n## Research\n\nIf you use this package in your research, please consider citing the following paper:\n\n- Clijmans, Jeroen, Maaike Van Roy, and Jesse Davis. **Looking Beyond the Past: Analyzing the Intrinsic Playing Style \n  of Soccer Teams**. European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in \n  Databases ECML PKDD 2022, 2022. [ [pdf](https://2022.ecmlpkdd.org/wp-content/uploads/2022/09/sub_1025.pdf) |\n  [bibtex](./docfiles/citation.bib) ]",
    'author': 'Jeroen Clijmans',
    'author_email': 'jeroen.clijmans@student.kuleuven.be',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JeroenClijmans/markovsoccer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
