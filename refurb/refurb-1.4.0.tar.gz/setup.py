# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['refurb',
 'refurb.checks',
 'refurb.checks.builtin',
 'refurb.checks.contextlib',
 'refurb.checks.flow',
 'refurb.checks.function',
 'refurb.checks.iterable',
 'refurb.checks.logical',
 'refurb.checks.pathlib',
 'refurb.checks.readability',
 'refurb.checks.string',
 'refurb.visitor']

package_data = \
{'': ['*']}

install_requires = \
['mypy>=0.981,<0.982']

extras_require = \
{':python_version < "3.11"': ['tomli>=2.0.1,<3.0.0']}

entry_points = \
{'console_scripts': ['refurb = refurb.__main__:main']}

setup_kwargs = {
    'name': 'refurb',
    'version': '1.4.0',
    'description': 'A tool for refurbish and modernize Python codebases',
    'long_description': '# Refurb\n\nA tool for refurbishing and modernizing Python codebases.\n\n## Example\n\n```python\n# main.py\n\nfor filename in ["file1.txt", "file2.txt"]:\n    with open(filename) as f:\n        contents = f.read()\n\n    lines = contents.splitlines()\n\n    for line in lines:\n        if not line or line.startswith("# ") or line.startswith("// "):\n            continue\n\n        for word in line.split():\n            print(f"[{word}]", end="")\n\n        print("")\n```\n\nRunning:\n\n```\n$ refurb main.py\nmain.py:3:17 [FURB109]: Use `in (x, y, z)` instead of `in [x, y, z]`\nmain.py:4:5 [FURB101]: Use `y = Path(x).read_text()` instead of `with open(x, ...) as f: y = f.read()`\nmain.py:10:40 [FURB102]: Replace `x.startswith(y) or x.startswith(z)` with `x.startswith((y, z))`\nmain.py:16:9 [FURB105]: Use `print() instead of `print("")`\n```\n\n## Installing\n\nBefore installing, it is recommended that you setup a [virtual environment](https://docs.python.org/3/tutorial/venv.html).\n\n```\n$ pip3 install refurb\n$ refurb file.py folder/\n```\n\n> Note: Refurb only supports Python 3.10. It can check Python 3.6 code and up, but Refurb\n> itself must be ran through Python 3.10.\n\n## Explanations For Checks\n\nYou can use `refurb --explain FURB123`, where `FURB123` is the error code you are trying to look up.\nFor example:\n\n````\n$ refurb --explain FURB123\nDon\'t cast a variable or literal if it is already of that type. For\nexample:\n\nBad:\n\n```\nname = str("bob")\nnum = int(123)\n```\n\nGood:\n\n```\nname = "bob"\nnum = 123\n```\n````\n\n## Ignoring Errors\n\nUse `--ignore 123` to ignore error 123. The error code can be in the form `FURB123` or `123`.\nThis flag can be repeated.\n\n> The `FURB` prefix indicates that this is a built-in error. The `FURB` prefix is optional,\n> but for all other errors (ie, `ABC123`), the prefix is required.\n\nYou can also use inline comments to disable errors:\n\n```\nx = int(0)  # noqa: FURB123\ny = list()  # noqa\n```\n\nHere, `noqa: FURB123` specifically ignores the FURB123 error for that line, and `noqa` ignores\nall errors on that line.\n\n## Enabling/Disabling Checks\n\nCertain checks are disabled by default, and need to be enabled first. You can do this using the\n`--enable ERR` flag, where `ERR` is the error code of the check you want to enable. A disabled\ncheck differs from an ignored check in that a disabled check will never be loaded, whereas an\nignored check will be loaded, an error will be emitted, and the error will be suppressed.\n\nThe opposite of `--enable` is `--disable`, which will disable a check. When `--enable` and `--disable`\nare both specified via the command line, whichever one comes last will take precedence. When using\n`enable` and `disable` via the config file, `disable` will always take precedence.\n\n## Configuring Refurb\n\nIn addition to the command line arguments, you can also add your settings in the `pyproject.toml` file.\nFor example, the following command line arguments:\n\n```\nrefurb file.py --ignore 100 --load some_module --quiet\n```\n\nCorresponds to the following in your `pyproject.toml` file:\n\n```toml\n[tool.refurb]\nignore = [100]\nload = ["some_module"]\nquiet = true\n```\n\nNow all you need to type is `refurb file.py`!\n\nNote that the values in the config file will be merged with the values specified via the\ncommand line. In the case of boolean arguments like `--quiet`, the command line arguments\ntake precedence. All other arguments (such as `ignore` and `load`) will be combined.\n\nYou can use the `--config-file` flag to tell Refurb to use a different config file from the\ndefault `pyproject.toml` file. Note that it still must be in the same form as the normal\n`pyproject.toml` file.\n\n## Using Refurb With `pre-commit`\n\nYou can use Refurb with [pre-commit](https://pre-commit.com/) by adding the following\nto your `.pre-commit-config.yaml` file:\n\n```yaml\n  - repo: https://github.com/dosisod/refurb\n    rev: REVISION\n    hooks:\n      - id: refurb\n```\n\nReplacing `REVISION` with a version or SHA of your choosing (or leave it blank to\nlet `pre-commit` find the most recent one for you).\n\n## Plugins\n\nInstalling plugins for Refurb is very easy:\n\n```\n$ pip3 install refurb-plugin-example\n```\n\nWhere `refurb-plugin-example` is the name of the plugin. Refurb will automatically load\nany installed plugins.\n\nTo make your own Refurb plugin, see the [`refurb-plugin-example` repository](https://github.com/dosisod/refurb-plugin-example)\nfor more info.\n\n## Writing Your Own Check\n\nIf you want to extend Refurb but don\'t want to make a full-fledged plugin,\nyou can easily create a one-off check file with the `refurb gen` command.\n\n> Note that this command uses the `fzf` fuzzy-finder for getting user input,\n> so you will need to [install fzf](https://github.com/junegunn/fzf#installation) before continuing.\n\nHere is the basic overview for creating a new check using the `refurb gen` command:\n\n1. First select the node type you want to accept\n2. Then type in where you want to save the auto generated file\n3. Add your code to the new file\n\nTo get an idea of what you need to add to your check, use the `--debug` flag to see the\nAST representation for a given file (ie, `refurb --debug file.py`). Take a look at the\nfiles in the `refurb/checks/` folder for some examples.\n\nThen, to load your new check, use `refurb file.py --load your.path.here`\n\n> Note that when using `--load`, you need to use dots in your argument, just like\n> importing a normal python module. If `your.path.here` is a directory, all checks\n> in that directory will be loaded. If it is a file, only that file will be loaded.\n\n## Developing\n\nTo setup locally, run:\n\n```\n$ git clone https://github.com/dosisod/refurb\n$ cd refurb\n$ make install\n$ make install-local\n```\n\nTests can be ran all at once using `make`, or you can run each tool on its own using\n`make black`, `make flake8`, and so on.\n\nUnit tests can be ran with `pytest` or `make test`.\n\n> Since the end-to-end (e2e) tests are slow, they are not ran when running `make`.\n> You will need to run `make test-e2e` to run them.\n\n## Why Does This Exist?\n\nI love doing code reviews: I like taking something and making it better, faster, more\nelegant, and so on. Lots of static analysis tools already exist, but none of them seem\nto be focused on making code more elegant, more readable, or more modern. That is where\nRefurb comes in.\n\nRefurb is heavily inspired by [clippy](https://rust-lang.github.io/rust-clippy/master/index.html),\nthe built-in linter for Rust.\n\n## What Refurb Is Not\n\nRefurb is not a style/type checker. It is not meant as a first-line of defense for\nlinting and finding bugs, it is meant for making good code even better.\n',
    'author': 'dosisod',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dosisod/refurb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
