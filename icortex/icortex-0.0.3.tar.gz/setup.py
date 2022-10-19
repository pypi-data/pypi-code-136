# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['icortex', 'icortex.services']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.13.0,<3.0.0',
 'entrypoints>=0.4,<0.5',
 'ipykernel>=6.16.0,<7.0.0',
 'ipython>=8.5.0,<9.0.0',
 'ipywidgets>=8.0.2,<9.0.0',
 'jupyter-client>=7.4.2,<8.0.0',
 'jupyter-console>=6.4.4,<7.0.0',
 'jupyter-core>=4.11.1,<5.0.0',
 'jupyterlab-widgets>=3.0.3,<4.0.0',
 'onnx[huggingface]>=1.12.0,<2.0.0',
 'onnxruntime[huggingface]>=1.12.1,<2.0.0',
 'openai[openai]>=0.23.1,<0.24.0',
 'optimum[huggingface]>=1.4.0,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'torch[huggingface]>=1.12.1,<2.0.0',
 'transformers[huggingface]>=4.23.1,<5.0.0']

entry_points = \
{'console_scripts': ['icortex = icortex.cli:main']}

setup_kwargs = {
    'name': 'icortex',
    'version': '0.0.3',
    'description': 'Jupyter kernel that allows you generate Python code from natural language prompts',
    'long_description': "# ICortex Kernel\n\n![Github Actions Status](https://github.com/textcortex/icortex/workflows/Build/badge.svg)\n[![License](https://img.shields.io/github/license/textcortex/icortex.svg?color=blue)](https://github.com/textcortex/icortex/blob/main/LICENSE)\n[![](https://dcbadge.vercel.app/api/server/QtfGgKneHX?style=flat)](https://discord.textcortex.com/)\n\nICortex is a [Jupyter kernel](https://jupyter-client.readthedocs.io/en/latest/kernels.html) that lets you program with plain English, by letting you generate Python code from natural language prompts:\n\nhttps://user-images.githubusercontent.com/2453968/193281898-8f2b4311-2a3a-4bbf-a7d4-b31fcd4f5e08.mp4\n\nIt is ...\n\n- a drop-in replacement for the IPython kernel. Prompts start with a forward slash `/`—otherwise the line is treated as regular Python code.\n- a [Natural Language Programming](https://en.wikipedia.org/wiki/Natural-language_programming) interface—prompts written in plain English automatically generate Python code which can then be executed in the global namespace.\n- interactive—install missing packages directly, decide whether to execute the generated code or not, and so on, directly in the Jupyter Notebook cell.\n- open source and fully extensible—if you think we are missing a model or an API, you can request it by creating an issue, or implement it yourself by subclassing `ServiceBase` under [`icortex/services`](icortex/services).\n\nICortex is currently in alpha, so expect breaking changes. We are giving free credits to our first users—[join our Discord](https://discord.textcortex.com/) to help us shape this product.\n\n## Installation\n\nTo install the ICortex Kernel, run the following in the main project directory:\n\n```sh\npip install icortex\n```\n\nThis will install the Python package and the `icortex` command line interface. You will need to run `icortex` once to install the kernel spec to Jupyter.\n\n## Using ICortex\n\nBefore you can use ICortex in Jupyter, you need to configure it for your current project.\n\nIf you are using the terminal:\n\n```bash\nicortex init\n```\n\nAlternatively, you can initialize directly in a Jupyter Notebook ([instructions on how to start JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)):\n\n```\n//init\n```\n\nThe shell will then instruct you step by step and create a configuration file `icortex.toml` in the current directory.\n\n### Choosing a code generation service\n\nICortex supports different code generation services such as the TextCortex API, OpenAI Codex API, local HuggingFace transformers, and so on.\n\nTo use the TextCortex code generation API,\n\n1. [sign up on the website](https://app.textcortex.com/user/signup),\n2. [generate an API key on the dashboard](https://app.textcortex.com/user/dashboard/settings/api-key),\n3. and proceed to configure `icortex` for your current project:\n\n[![asciicast](https://asciinema.org/a/sTU1EaGFfi3jdSV8Ih7vulsfT.svg)](https://asciinema.org/a/sTU1EaGFfi3jdSV8Ih7vulsfT)\n\nIf you use up the starter credits and would like to continue testing out ICortex, [hit us up on our Discord on #icortex channel](https://discord.textcortex.com) and we will charge your account with more free credits.\n\nYou can also try out different services e.g. OpenAI's Codex API, if you have access. You can also run code generation models from HuggingFace locally, which we have optimized to run on the CPU—though these produce lower quality outputs due to being smaller.\n\n## Usage\n\n### Executing prompts\n\nTo execute a prompt with ICortex, use the `/` character (forward slash, also used to denote division) as a prefix. Copy and paste the following prompt into a cell and try to run it:\n\n```\n/print Hello World. Then print the Fibonacci numbers till 100\n```\n\nDepending on the response, you should see an output similar to the following:\n\n```\nprint('Hello World.', end=' ')\na, b = 0, 1\nwhile b < 100:\n    print(b, end=' ')\n    a, b = b, a+b\n\nHello World.\n1 1 2 3 5 8 13 21 34 55 89\n```\n\nYou can also specify variables or options with command line flags, e.g. to auto-install packages, auto-execute the returned code and so on. To see the complete list of variables for your chosen service, run:\n\n```\n/help\n```\n\n### Using ICortex CLI\n\nICortex comes with a full-fledged CLI similar to git or Docker CLI, which you can use to configure how you generate code in your project. To see all the commands you can invoke, run\n\n```sh\nicortex help\n```\n\nFor example the command `icortex service` lets you configure the code generation service you would like to use. To see how to use each command, call them with `help`\n\n```\nicortex service help\n```\n\n### Accessing ICortex CLI inside Jupyter\n\nYou can still access the `icortex` CLI in a Jupyter Notebook or shell by using the prefix `//`. For example running the following in the terminal switches to a local HuggingFace model:\n\n```\nicortex service set huggingface\n```\n\nTo do the same in a Jupyter Notebook, you can run\n\n```\n//service set huggingface\n```\n\nin a cell, which initializes and switches to the new service directly in your Jupyter session.\n\n## Getting help\n\nFeel free to ask questions in our [Discord](https://discord.textcortex.com/).\n\n## Uninstalling\n\nTo uninstall, run\n\n```bash\npip uninstall icortex\n```\n\nThis removes the package, however, it may still leave the kernel spec in Jupyter's kernel directories, causing it to continue showing up in JupyterLab. If that is the case, run\n\n```\njupyter kernelspec uninstall icortex -y\n```\n",
    'author': 'TextCortex Team',
    'author_email': 'onur@textcortex.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://icortex.ai/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
