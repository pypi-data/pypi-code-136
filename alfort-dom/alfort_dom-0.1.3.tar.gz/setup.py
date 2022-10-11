# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alfort_dom']

package_data = \
{'': ['*']}

install_requires = \
['alfort>=0.1.9,<0.2.0']

setup_kwargs = {
    'name': 'alfort-dom',
    'version': '0.1.3',
    'description': 'A simple Elm like web application framework',
    'long_description': '# Alfort-DOM\n[![Build][build-shiled]][build-url]\n[![Version][version-shield]][version-url]\n[![Downloads][download-shield]][download-url]\n[![Contributors][contributors-shield]][contributors-url]\n[![Issues][issues-shield]][issues-url]\n[![Codecov][codecov-shield]][codecov-url]\n[![Apache License 2.0 License][license-shield]][license-url]\n\nAlfort-DOM is Elm-like web application framework for Python. It uses [Alfort](https://github.com/ar90n/alfort) to handle Vritual DOM and [Pyodide](https://pyodide.org/en/stable/) to run its codes on browser.\n\n## Installation\n```bash\n$ pip install alfort-dom\n```\n\n## Example\n```python\nfrom dataclasses import dataclass\nfrom typing import TypeAlias\n\nfrom alfort import Effect\nfrom alfort.vdom import VDom, el\n\nfrom alfort_dom import AlfortDom\n\n\n@dataclass(frozen=True)\nclass CountUp:\n    value: int = 1\n\n\n@dataclass(frozen=True)\nclass CountDown:\n    value: int = 1\n\n\nMsg: TypeAlias = CountUp | CountDown\n\n\ndef title(text: str) -> VDom:\n    return el("h1", {}, [text])\n\n\ndef count(cnt: int) -> VDom:\n    return el("div", {"style": {"margin": "8px"}}, [str(cnt)])\n\n\ndef buttons() -> VDom:\n    button_style = {"margin": "4px", "width": "50px"}\n    return el(\n        "div",\n        {},\n        [\n            el("button", {"style": button_style, "onclick": CountDown(10)}, ["-10"]),\n            el("button", {"style": button_style, "onclick": CountDown()}, ["-"]),\n            el("button", {"style": button_style, "onclick": CountUp()}, ["+"]),\n            el("button", {"style": button_style, "onclick": CountUp(10)}, ["+10"]),\n        ],\n    )\n\n\ndef view(state: dict[str, int]) -> VDom:\n    return el(\n        "div",\n        {\n            "style": {\n                "display": "flex",\n                "justify-content": "center",\n                "align-items": "center",\n                "flex-flow": "column",\n            }\n        },\n        [title("Simple Counter"), count(state["count"]), buttons()],\n    )\n\n\ndef init() -> tuple[dict[str, int], list[Effect[Msg]]]:\n    return ({"count": 0}, [])\n\n\ndef update(msg: Msg, state: dict[str, int]) -> tuple[dict[str, int], list[Effect[Msg]]]:\n    match msg:\n        case CountUp(value):\n            return ({**state, "count": state["count"] + value}, [])\n        case CountDown(value):\n            return ({**state, "count": state["count"] - value}, [])\n\n\napp = AlfortDom[dict[str, int], Msg](\n    init=init,\n    view=view,\n    update=update,\n)\napp.main(root="root")\n\n```\n\n![simple counter](https://raw.githubusercontent.com/ar90n/alfort-dom/assets/images/example.gif)\n\nIf you need more exmplaes, please check the [examples](https://github.com/ar90n/alfort-dom/tree/main/docs/examples).\n\n## For development\n### Install Poery plugins\n```bash\n$ poetry self add "poethepoet[poetry_plugin]"\n```\n\n### Run tests\n```bash\n$ poetry poe test\n```\n\n### Run linter and formatter\n```bash\n$ poetry poe check\n```\n### Run examples\n```bash\n$ poetry poe run-example\n```\n\n## See Also\n* [Elm](https://elm-lang.org/)\n* [Pyodide](https://pyodide.org/en/stable/)\n* [Alfort](https://github.com/ar90n/alfort)\n\n## License\n[Apache-2.0](https://github.com/ar90n/alfort-dom/blob/main/LICENSE)\n\n\n[download-shield]: https://img.shields.io/pypi/dm/alfort-dom?style=flat\n[download-url]: https://pypi.org/project/alfort-dom/\n[version-shield]: https://img.shields.io/pypi/v/alfort-dom?style=flat\n[version-url]: https://pypi.org/project/alfort-dom/\n[build-shiled]: https://img.shields.io/github/workflow/status/ar90n/alfort-dom/CI%20testing/main\n[build-url]: https://github.com/ar90n/alfort-dom/actions/workflows/ci.yml\n[contributors-shield]: https://img.shields.io/github/contributors/ar90n/alfort-dom.svg?style=flat\n[contributors-url]: https://github.com/ar90n/alfort-dom/graphs/contributors\n[issues-shield]: https://img.shields.io/github/issues/ar90n/alfort-dom.svg?style=flat\n[issues-url]: https://github.com/ar90n/alfort-dom/issues\n[license-shield]: https://img.shields.io/github/license/ar90n/alfort-dom.svg?style=flat\n[license-url]: https://github.com/ar90n/alfort-dom/blob/master/LICENSE.txt\n[codecov-shield]: https://codecov.io/gh/ar90n/alfort-dom/branch/main/graph/badge.svg?token=8GKU96ODLY\n[codecov-url]: https://codecov.io/gh/ar90n/alfort-dom\n',
    'author': 'Masahiro Wada',
    'author_email': 'argon.argon.argon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ar90n/alfort-dom',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
