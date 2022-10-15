# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ream', 'ream.actors']

package_data = \
{'': ['*']}

install_requires = \
['filelock>=3.8.0,<4.0.0',
 'graph-wrapper>=1.5.0,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'orjson>=3.8.0,<4.0.0',
 'python-slugify>=6.1.2,<7.0.0',
 't2-yada>=1.0.4,<2.0.0',
 'timer4>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'ream2',
    'version': '1.0.0',
    'description': 'An actor architecture for research software',
    'long_description': '# ream ![PyPI](https://img.shields.io/pypi/v/ream2) ![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)\n\nA simple actor architecture for your research project.\n\n## Introduction\n\nLet\'s say you are developing a method, an algorithm, or a pipeline to solve a problem. In many cases, it can be viewed as a computational graph. So why not structuring your code as a computational graph, where each node is a component in your method or a step in your pipeline? It made your code more modular, easy to release, to cache, and to evaluate.\n\nTo see how we can apply this architecture, let\'s take a look at a record linkage project (linking entities in a table). A record linkage system typically has the following steps:\n\n1. Generate candidate entities in a table\n2. Rank the candidate entities and select the best matches.\n\nSo naturally, we will have two actors for two steps: `CandidateGeneration` and `CandidateRanking`:\n\n```python\nimport pandas as pd\nfrom typing import Literal\nfrom ream.prelude import BaseActor\nfrom dataclasses import dataclass\n\n@dataclass\nclass CanGenParams:\n    # type of query that will be sent to ElasticSearch\n    query_type: Literal["exact-match", "fuzzy-match"]\n\nclass CandidateGeneration(BaseActor[pd.DataFrame, CanGenParams]):\n    VERSION = 100\n\n    def run(self, table: pd.DataFrame):\n        # generate candidate entities of the given table\n        ...\n\n@dataclass\nclass CanRankParams:\n    # ranking method to use\n    rank_method: Literal["pairwise", "columnwise"]\n\nclass CandidateRanking(BaseActor[pd.DataFrame, CanRankParams]):\n    VERSION = 100\n\n    def __init__(self, params: CanRankParams, cangen_actor: CandidateGeneration):\n        super().__init__(params, [cangen_actor])\n\n    def run(self, table: pd.DataFrame):\n        # rank candidate entities of the given table\n        ...\n```\n\nThe two actors made your code be more modular and closer to releasable quality. To define the linking pipeline, use `ActorGraph`\n\n````python\nfrom ream.prelude import ActorGraph, ActorNode, ActorEdge\n\ng = ActorGraph()\ncangen = g.add_node(ActorNode.new(CandidateGeneration))\ncanrank = g.add_node(ActorNode.new(CandidateRanking))\ng.add_edge(BaseEdge(id=-1, source=cangen, target=canrank))\n```\n\nThis seems boring and does not offer much, but then you can pick whatever actor and its function you want to call without manually initializing and parsing command line arguments. For example, we want to trigger the `evaluate` method on each actor. The parameters of the actors will be obtained automatically from the command line arguments, thanks to the [`yada`](https://github.com/binh-vu/yada) parser.\n\n```python\nif __name__ == "__main__":\n    g.run(actor_class="CandidateGeneration", actor_method="evaluate")\n```\n\nThe `evaluate` method for each actor can be very useful. On the candidate generation actor, it can tell us the upperbound accuracy of our method so we know whether we need to improve the candidate generation or candidate ranking. If an dataset actor is introduced to the computational graph as demonstrated below, its evaluate method can tell us statistics about the dataset.\n\n```python\nfrom ream.prelude import NoParams, BaseActor, DatasetQuery\n\nclass DatasetActor(BaseActor[str, NoParams]):\n    VERSION = 100\n\n    def run(self, query: str):\n        # use a query so we can dynamically select a subset of the dataset for quickly test\n        # for example: mnist[:10] -- select first 10 examples\n        dsquery = DatasetQuery.from_string(query)\n\n        # load the real dataset\n        examples = ...\n        return dsquery.select(examples)\n\n    def evaluate(self, query: str):\n        dsdict = self.run(query)\n        for split, examples in dsdict.items():\n            print(f"Dataset: {dsdict.name} - split {split} has {len(examples)} examples")\n```\n\nLet\'s talk about caching. Each actor when they run, they will be uniquely identify by their name, version, and parameters (including the dependent actor parameters), and this is referred as actor state which you can retrieve from `BaseActor.get_actor_state` function. From this, we can create a unique folder associated with that state that you can used to store your cache data (the folder can be retrieved from the function `BaseActor.get_working_fs`). Whenever the actor\'s dependency is updated, you will always get a new folder so no worry about managing the cache yourself! To set it up, in the file that define the actor graph, init the ream workspace as follow:\n\n```python\nfrom ream.prelude import ReamWorkspace, ActorGraph\n\nReamWorkspace.init("<folder>/<to>/<store>/<cache>")\ng = ActorGraph()\n...\n```\n\n## Installation\n\n```python\npip install ream2  # not ream\n````\n\n## Examples\n\nWill be added later.\n',
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
