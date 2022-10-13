# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chess_ai',
 'chess_ai.classical_agent',
 'chess_ai.evaluation',
 'chess_ai.playground',
 'chess_ai.rlagent']

package_data = \
{'': ['*'], 'chess_ai.playground': ['resources/*']}

install_requires = \
['chess-python-pip>=0.1.7,<0.2.0', 'pyglet>=1.5.27,<2.0.0']

setup_kwargs = {
    'name': 'chess-ai-pip',
    'version': '0.1.2',
    'description': '',
    'long_description': '# ChessAI\n\nAttempt to create a decent adversary to play chess against. The game implementation used for the\nagents in this project is another personal project\n[chess_python](https://github.com/pacanada/chess-python)\n\nRun the (very basic) GUI with:\n\n```cmd\npip install chess-ai-pip\npython -m chess_ai.playground.chess_gui\n```\n\n<img src="docs/screenshot_2.png" width="380" height="400">\n<img src="docs/screenshot_1.png" width="380" height="400">\n\n## Plan\n\n**Classical engine**:\n\n- [x] Create "decent" agent with alpha beta pruning and minimax\n- [x] Implement Move ordering\n- [x] Implement transpositions (caching)\n- [ ] Implement Iterative deepening search\n\nThis classical engine is limited by the performance of the chess game implementation (heavily)\n\n**Deep lerning agent**:\n\n- [ ] 1. Game implementation with legal moves known and value network based on plays of DL agents\n- [ ] 2. Learned model, policy and value network\n\n**Evaluation of agent strenght**:\n\nCome up with a simple strength evaluator strategy that can be used to measure progress for the DL\nagent and baseline for classical engine agent.\n\n1. Choose an arbitrary number of positions\n2. Run them through an engine (stockfish) and rank all posible moves (from best to worst)\n3. Compare chosen move from agent to the list of moves from the engine\n4. Assign score based on how good is the agent choice, if agent choice is more than one (same\n   evaluation for different positions) take the best\n5. Sum the score\n\n**UI**\n\nImportant for testing TODO:\n\n- [x] Basic UI\n- [ ] Play also as black inverting board\n- [ ] Allow args when launching the GUI (depth, agent type, fen)\n',
    'author': 'pacanada',
    'author_email': 'pereirapcanada@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
