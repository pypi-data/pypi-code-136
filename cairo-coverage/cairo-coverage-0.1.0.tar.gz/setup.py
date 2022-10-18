# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cairo_coverage']

package_data = \
{'': ['*']}

install_requires = \
['asynctest>=0.13.0,<0.14.0', 'cairo-lang==0.10.1', 'pytest>=7.1.3,<8.0.0']

setup_kwargs = {
    'name': 'cairo-coverage',
    'version': '0.1.0',
    'description': 'Cairo coverage module',
    'long_description': "# Cairo coverage\n\nThis package allows you to have a small coverage report for your cairo files. For now it's a bit hacky but with cairo 0.10.1 it'll be easier.\n\n## How to make it work\n\nTo install it run:\n\n```sh\npip install .\n```\n\nThat's the hacky part and i'll explain later why it's needed. You'll need to go into your python packages folder to modify the `cairo_runner.py` file. To find it easily run `which starknet` it should display something like `BASE_PATH/bin/starknet`. The part that we need is `BASE_PATH`. You'll need to use your preferred editor and follow the steps. I chose to use nano but feel free to use vim or vs code.\n\n1. `nano BASE_PATH/python3.X/site-packages/starkware/cairo/lang/vm/cairo_runner.py`\n2. go to the function `initialize_vm` on line 254\nIt should look like this:\n\n```py\ndef initialize_vm(\n        self, hint_locals, static_locals: Optional[Dict[str, Any]] = None, vm_class=VirtualMachine\n    ):\n        context = RunContext(\n            pc=self.initial_pc,\n            ap=self.initial_ap,\n            fp=self.initial_fp,\n            memory=self.memory,\n            prime=self.program.prime,\n        )\n```\n\nWe're now going to modify the default argument for the `vm_class` so it looks like this:\n\n```py\ndef initialize_vm(\n        self, hint_locals, static_locals: Optional[Dict[str, Any]] = None, vm_class=None\n    ):\n        if vm_class is None:\n            vm_class = VirtualMachine\n        context = RunContext(\n            pc=self.initial_pc,\n            ap=self.initial_ap,\n            fp=self.initial_fp,\n            memory=self.memory,\n            prime=self.program.prime,\n        )\n```\n\nTo understand why all this is necessary we'll take a look on how the coverage works and how python works.\n\nTo run the examples:\n\n```sh\npoetry run python3 -m pytest examples/ -s -W ignore::DeprecationWarning\n```\n\n## How cairo coverage works\n\nThe first step to create cairo coverage was to find a way on how to know which instruction has been ran and to save them. The way cairo works is that every time you run some cairo code it creates a VM to execute the code (which is pretty obvious I know) but it implies that every transaction will need a new VM (also obvious). But this is a problem for us because we want to know all the `pc` (program counter) that have been touched by our tests and we can't just ask the VM at the end of the tests because it's wiped at each new transaction. So we would need to find a way to save what pc has been touched for what file and to map back the pc to a cairo line. In order to do that we'll override the default VM and create our own that has all the functionalities we want. Now to override the default VM we can monkey patch it basically `cairo_runner.VirtualMachine = CustomVm`. This would replace the cairo_runner VirtualMachine by our own but since it's a default value here\n\n```py\ndef initialize_vm(\n        self, hint_locals, static_locals: Optional[Dict[str, Any]] = None, vm_class=VirtualMachine\n    ):\n```\n\nVirtualMachine can't be modified once the script has started because this value is set at python's compile time (yes python is compiled). So in order to prevent this we modify the default value to `None` so the `VirtualMachine` class can be patched at runtime.\n\nSo now we know how to override the VM now let's understand what the VM is actually doing.\nThe first important thing is to save all the pc touched by the tests across all the files we would need a variable that's shared between all the class instances (spoiler we need to find a hacky way to do it easily). Fortunately for us we can do that\n\n```py\n@staticmethod\ndef covered(val: defaultdict(list) = defaultdict(list)) -> defaultdict(list):\n    return val\n```\n\nWhat's happening there is that if you don't supply a value for `val` it'll use a `defaultdict(list)` (it's just a dict that returns a list for all the keys even not initialized). The thing is that this dict will be initialized once and then it'll reuse the same instance (because it's set at compile time) so we can share this value between all the class instances.\nWe can then get all the pc touched during the cairo run and at the end of this run save them in the default dict shared between all the instances. Even though pc are interesting we want the cairo lines. In order to do that we'll use the `debug_info` of each file to map the pc to the cairo line. Once we have all this all we need to do is format it and print it in the terminal (no shame on the output I had to format everything myself)\n",
    'author': 'LucasLvy',
    'author_email': 'lucaslevy10@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
