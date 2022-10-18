# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tawazi']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'networkx>=2.6.3,<3.0.0', 'pydantic>=1.10,<2.0']

setup_kwargs = {
    'name': 'tawazi',
    'version': '0.2.0',
    'description': 'This library helps you execute a set of functions in a Directed Acyclic Graph (DAG) dependency structure in parallel in a production environment. It aims at providing This in a production environment',
    'long_description': '# tawazi\n[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)\n[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)\n[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)\n[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)\n[![CodeFactor](https://www.codefactor.io/repository/github/mindee/tawazi/badge)](https://www.codefactor.io/repository/github/mindee/tawazi)\n\n![Tawazi GIF](documentation/tawazi_GIF.gif)\n\n## Introduction\n\n<!-- TODO: put a link explaining what a DAG is-->\n\nThe tawazi library enables **parallel** execution of functions in a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) dependency structure.\nThis library satisfies the following:\n* Stable, robust, well tested\n* lightweight\n* Thread Safety\n* Low to no dependencies\n* Legacy Python versions support (in the future)\n* pypy support (in the future)\n\nIn the context of tawazi, the computation sequence to be run in parallel is referred to as DAG and the functions that must run in parallel are called `ExecNode`s.\n\nThis library supports:\n* Limitation of the number of "Threads"\n* Priority Choice of each `ExecNode`\n* Per `ExecNode` choice of parallelization (i.e. An `ExecNode` is allowed to run in parallel with other `ExecNode`s or not)\n\n**Note**: The library is still at an [advanced state of development](#future-developments). Your contributions are highly welcomed.\n\n\n## Usage\n```python\n\n# type: ignore\nfrom time import sleep, time\nfrom tawazi import op, to_dag\n\n@op\ndef a():\n    print("Function \'a\' is running", flush=True)\n    sleep(1)\n    return "A"\n\n@op\ndef b():\n    print("Function \'b\' is running", flush=True)\n    sleep(1)\n    return "B"\n\n@op\ndef c(a, b):\n    print("Function \'c\' is running", flush=True)\n    print(f"Function \'c\' received {a} from \'a\' & {b} from \'b\'", flush=True)\n    return f"{a} + {b} = C"\n\n@to_dag(max_concurrency=2)\ndef deps_describer():\n  result_a = a()\n  result_b = b()\n  result_c = c(result_a, result_b)\n\nif __name__ == "__main__":\n\n  t0 = time()\n  # executing the dag takes a single line of code\n  deps_describer().execute()\n  execution_time = time() - t0\n  assert execution_time < 1.5\n  print(f"Graph execution took {execution_time:.2f} seconds")\n\n```\n\n## Advanced Usage\n\n```python\n\n# type: ignore\nfrom time import sleep, time\nfrom tawazi import op, to_dag\n\n@op\ndef a():\n    print("Function \'a\' is running", flush=True)\n    sleep(1)\n    return "A"\n\n# optionally configure each op using the decorator:\n# is_sequential = True to prevent op from running in parallel with other ops\n# priority to choose the op in the next execution phase\n# argument_name to choose the name of the argument that will be used\n@op(is_sequential=True, priority=10, argument_name="arg_b")\ndef b():\n    print("Function \'b\' is running", flush=True)\n    sleep(1)\n    return "B"\n\n@op\ndef c(a, arg_b):\n    print("Function \'c\' is running", flush=True)\n    print(f"Function \'c\' received {a} from \'a\' & {arg_b} from \'b\'", flush=True)\n    return f"{a} + {arg_b} = C"\n\n# optionally customize the DAG\n@to_dag(max_concurrency=2, behavior="strict")\ndef deps_describer():\n  result_a = a()\n  result_b = b()\n  result_c = c(result_a, result_b)\n\nif __name__ == "__main__":\n\n  t0 = time()\n  # the dag instance is reusable.\n  # This is recommended if you want to do the same computation multiple times\n  dag = deps_describer()\n  results_1 = dag.execute()\n  execution_time = time() - t0\n  print(f"Graph execution took {execution_time:.2f} seconds")\n\n  # debugging the code using `dag.safe_execute()` is easier\n  # because the execution doesn\'t go through the Thread pool\n  results_2 = dag.safe_execute()\n\n  # you can look throught the results of each operation like this:\n  for my_op in [a, b, c]:\n    assert results_1[my_op.id].result == results_2[my_op.id].result\n\n```\n\n\n## Name explanation\nThe libraries name is inspired from the arabic word تَوَازٍ which means parallel.\n\n## Building the doc\nThe general documentation has no dedicated space at the moment and is being hosted offline (on your machine).\nExpect future developments on this side as well. To build it, simply run `mkdocs build` and `mkdocs serve` at the root of the repository.\n\n## Future developments\n*This library is still in development. Breaking changes are expected.\n',
    'author': 'Bashir Abdelwahed',
    'author_email': 'bashir@mindee.co>, Matthias Cremieux <matthias@mindee.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
