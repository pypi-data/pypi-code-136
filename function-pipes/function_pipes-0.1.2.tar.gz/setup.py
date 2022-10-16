# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['function_pipes',
 'function_pipes.with_paramspec',
 'function_pipes.without_paramspec']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'function-pipes',
    'version': '0.1.2',
    'description': 'Typed python equivalent for R pipes.',
    'long_description': '# function-pipes\n\n[![PyPI](https://img.shields.io/pypi/v/function-pipes.svg)](https://pypi.org/project/function-pipes/)\n[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/inkleby/function-pipes/blob/main/LICENSE.md)\n[![Copy and Paste](https://img.shields.io/badge/Copy%20%2B%20Paste%3F-yes!-blue)](#install)\n\nFast, type-hinted python equivalent for R pipes.\n\nThis decorator only relies on the standard library, so can just be copied into a project as a single file.\n\n# Why is this needed?\n\nVarious languages have versions of a \'pipe\' syntax, where a value can be passed through a succession of different functions before returning the final value. \n\nThis means you can avoid syntax like the below, where the sequence is hard to read (especially if extra arguments are introduced).\n\n```python\na = c(b(a(value)))\n```\n\nIn Python, there is not a good built-in way of doing this, and other attempts at a pipe do not play nice with type hinting. \n\nThis library has a very simple API, and does the fiddly bits behind the scenes to keep the pipe fast. \n\n## The pipe\n\nThere is a `pipe`, function which expects a value and then a list of callables.\n\n```python\nfrom function_pipes import pipe\n\nvalue = pipe(5, lambda x: x + 2, str)\nvalue == "7"\n\n```\n\n## No special form for extra arguments, small special case for functions that don\'t return a value\n\nThere is no bespoke syntax for passing in extra arguments or moving where the pipe\'s current value is placed - just use a lambda. This is a well understood approach, that is compatible with type hinting. In the above, `value` will be recognised as a string, but the x is understood as an int. \n\nThere is a small bit of bespoke syntax for when you want to pass something through a function, but that function doesn\'t return the result to the next function. Here the `pipe_bridge` function will wrap another function, pass the function into it, and continue onwards. The following will print `7`, before passing the value on. \n\n```python\nfrom function_pipes import pipe, pipe_bridge\n\nvalue = pipe(5, lambda x: x + 2, pipe_bridge(print), str)\nvalue == "7"\n\n```\n\n## Merging functions to use later\n\nThere is also a `pipeline`, which given a set of functions will return a function which a value can be passed into. Where possible based on other hints, this will hint the input and output variable types.\n\n```python\nfrom function_pipes import pipeline\n\nfunc = pipeline(lambda x: x + 2, str)\nfunc(5) == "7"\n\n```\n\n## Optimising use of pipes\n\nThere\'s work behind the scenes to minimise the overhead of using the pipe, but it is still adding a function call. If you want the readability of the pipe *and* the speed of the native ugly approach you can use the `@fast_pipes` decorator. This rewrites the function it is called on to expand out the pipe and any lambdas into the fastest native equivalent. \n\ne.g. These two functions should have equivalent AST trees:\n\n```python\n\n@fast_pipes\ndef function_that_has_a_pipe(v: int) -> str:\n    value = pipe(v, a, lambda x: b(x, foo="other_input"), c)\n    return pipe\n```\n\n```python\ndef function_that_has_a_pipe(v: int) -> str:\n    value = c(b(a(v),foo="other_input"))\n    return pipe\n```\n\nThis version of the function is solving three versions of the same puzzle at the same time:\n\n* The type hinting is unpacking the structure when it is being written.\n* The pipe function solves the problem in standard python.\n* The fast_pipes decorator is rewriting the AST tree to get the same outcome faster.\n\nBut to the user, it all looks the same - pipes!\n\nThere is a limit of 20 functions that can be passed to a pipe or pipeline. If you *really* want to do more, you could chain multiple pipelines together.\n\n## Install\n\nYou can install from pip: `python -m pip install function-pipes`\n\nOr you can copy the module directly into your projects.\n\n* For python 3.10+: [with_paramspec/function_pipes.py](src/function_pipes/with_paramspec/function_pipes.py)\n* For python 3.8, 3.9: [without_paramspec/function_pipes.py](src/function_pipes/without_paramspec/function_pipes.py)\n\n## Development\n\nThis project comes with a Dockerfile and devcontainer that should get a good environment set up. \n\nThe actual code is generated from `src/function_pipes/pipes.jinja-py` using jinja to generate the code and the seperate versions with and without use of paramspec.\n\nUse `make` to regenerate the files. The number of allowed arguments is specified in `Makefile`.\n\nThere is a test suite that does checks for equivalence between this syntax and the raw syntax, as well as checking that fast_pipes and other optimisations are faster. \n\nThis can be run with `script/test`.',
    'author': 'Alex Parsons',
    'author_email': 'alex@alexparsons.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ajparsons/function-pipes',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
