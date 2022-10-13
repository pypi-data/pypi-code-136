# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chess_python']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'chess-python-pip',
    'version': '0.1.8',
    'description': 'Python implementation of the game of chess.',
    'long_description': '# Introduction\n\nPython **implementation of the chess game** in less than 1000 lines of code.\n\nFor engines/agents to play against check my other project\n[chess-ai](https://github.com/pacanada/chess-ai)\n\nThere is also a work in progress for the cli based game (`python -m chess_python.game`).\n\n# Usage\n\n```\npip install chess-python-pip\n```\n\n```python\n#examples/example_01.py\nfrom chess_python.chess import Chess\nchess = Chess(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0") # Default\nprint(chess)\nprint(chess.legal_moves())\nchess.move("e2e4")\nprint(chess)\n```\n\noutputs:\n\n```\nPlayer to move: White\nMove count: 0\n8 || r | n | b | q | k | b | n | r |\n-----------------------------------\n7 || p | p | p | p | p | p | p | p |\n-----------------------------------\n6 ||   |   |   |   |   |   |   |   |\n-----------------------------------\n5 ||   |   |   |   |   |   |   |   |\n-----------------------------------\n4 ||   |   |   |   |   |   |   |   |\n-----------------------------------\n3 ||   |   |   |   |   |   |   |   |\n-----------------------------------\n2 || P | P | P | P | P | P | P | P |\n-----------------------------------\n1 || R | N | B | Q | K | B | N | R |\n-----------------------------------\n-----------------------------------\n  || a | b | c | d | e | f | g | h\n\n[\'b1a3\', \'b1c3\', \'g1f3\', \'g1h3\', \'a2a3\', \'a2a4\', \'b2b3\', \'b2b4\', \'c2c3\', \'c2c4\', \'d2d3\', \'d2d4\', \'e2e3\', \'e2e4\', \'f2f3\', \'f2f4\', \'g2g3\', \'g2g4\', \'h2h3\', \'h2h4\']\nPlayer to move: Black\nMove count: 1\n8 || r | n | b | q | k | b | n | r |\n-----------------------------------\n7 || p | p | p | p | p | p | p | p |\n-----------------------------------\n6 ||   |   |   |   |   |   |   |   |\n-----------------------------------\n5 ||   |   |   |   |   |   |   |   |\n-----------------------------------\n4 ||   |   |   |   | P |   |   |   |\n-----------------------------------\n3 ||   |   |   |   |   |   |   |   |\n-----------------------------------\n2 || P | P | P | P |   | P | P | P |\n-----------------------------------\n1 || R | N | B | Q | K | B | N | R |\n-----------------------------------\n-----------------------------------\n  || a | b | c | d | e | f | g | h\n```\n\n# DEV section:\n\n## Performance tracking\n\nUsing `python3 -m cProfile -o prof.txt tree.py -h` for profiling and `snakeviz prof.txt` to\nvisualize.\n\nPerft(3) initial position `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1` (8902\npositions, reference time 0.05 s with\n[`python-chess`](https://python-chess.readthedocs.io/en/latest/):\n\n- 1.25 s (first)\n- 0.79 s (moving `get_positions_attacking_pieces` to optimizer initialization and update, not when\n  checking if move is legal)\n- 0.70 s removing `np.array` from list of moves (does not make a lot of sense)\n- 0.55 s removing more np.arrays\n- 0.51 s removing np.unravel\n- 0.47 s using only lists in `get_allowed_moves_by_piece`\n- 0.39 s with revamped `get_index_trajectory`\n- 0.35 with custom `deepcopy`\n- 0.18 s with using list for board instead of numpy!!\n- 0.15 s further tweaks\n\n## TODO:\n\n- [x] Include tests for perft in different positions\n- [x] Include utils if there is a mismatch in positions tree with reference implementation\n- [ ] Improve performance:\n  - [x] Keep track of index where there are pieces in optimizer level\n  - [ ] Move and unmake move (implenting unmake also requires using a copy of the board, which\n        performance wise does not improve anything)\n- [ ] Improve overall code quality (clarity, choose right data structure for the job):\n  - Public vs private functions\n  - cyclomatic complexity in `is_legal_move`\n- [x] Automate release with github action to pip\n- [ ] Explore pypy\n- [x] Explore deepcopy for tree generation, it takes a lot of time (only copying board improves\n      performance)\n- [ ] Simplify castling\n',
    'author': 'pacanada',
    'author_email': 'pereirapcanada@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
