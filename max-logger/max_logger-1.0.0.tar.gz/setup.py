# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['max_logger']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'rich[all]>=12.6.0,<13.0.0', 'ujson>=5.5.0,<6.0.0']

entry_points = \
{'console_scripts': ['my-script = main:main']}

setup_kwargs = {
    'name': 'max-logger',
    'version': '1.0.0',
    'description': "Max's custom loguru sinks, logger helper functions, rich tracebacks and other helper functions for rich.",
    'long_description': '---\ntitle: max_logger README\nauthor: Max Ludden\nemail: dev@maxludden.com\nedited: 10-20-2022\nCSS: style.css\n---\n\n# `max_logger`\nThe main purpose of the module is to automate my custom logging. It\'s based on the most excellent [loguru](https://github.com/Delgan/loguru) module and automatically sets up the loguru sinks that I find most useful. In addition it also provides a number of helper functions for working with Rich Python by [Textualize](https://www.textualize.io/), including the ability to print gradient text and panels.\n\n## Instillation\n\n<br />\n<br />\n\n### Install using `pipx`\n```bash\npipx install max_logger\n```\n\n<br />\n<br />\n\n### Install using `pip`\n```bash\npip install max_logger\n```\n<br />\n<br />\n\n### Install using `poetry`\n```bash\npoetry add max_logger\n```\n<br />\n\nIt\'s as simple as that. This module is available on PyPi and can be installed using your favorite python package manager (`pipx`, `pip`, `poetry`).\n\n<br />\n<br />\n<br />\n\n# Usage\n```Python\nfrom max_logger import log\n\n>>> log.info("Hello, World!)\n```\nIt\'s as simple as that. It is useful to note that you may import a custom formatted Rich Console & Progress from the modules as well. This is useful if you want to use the same console for your own logging.\n\n\n\n```Python\nfrom time import sleep\nfrom max_logger import console, progress\n\nwith progress:\n    task1 = progress.add_task("task1", total=10)\n    for i in range(1,11):\n        progress.update(task1, advance=1)\n        sleep(0.1)\n        smiles = ":smile:" * i\n        console.print(f"[bright_red]♥︎[/] [bold purple1]I really like Max\'s Logger![/][#00ff00] ☘︎[/]")\n```\n\n\n\n<figure>\n    <img src=https://i.imgur.com/IdKDdzE.png alt="Example of Rich Console" />\n    <figcaption>Example of Rich Console</figcaption>\n</figure>\n\n\n\n<br />\n<br />\n<br />\n\n# Gradient Text\nThere are also a number of helper function to allow the printing of gradient text.\n\n## `rainbow`\n```Python\ndef rainbow(message: str, num_of_gradients: int = 4) -> Text:\n    """Prints a rainbow gradient of the message.\n\n    Args:\n        message (str): The message to print.\n        num_of_gradients (int, optional): The number of gradients to use. Defaults to 4. Must be between 1 and 6.\n\n    Returns:\n        Text: The message as a Gradient Rich Text object.\n    """\n```\n\n```Python\nfrom max_logger import rainbow\n\nconsole.print(rainbow("I think this is a lot more fun. 🌈"))\n```\n<br />\n<figure>\n    <img src="https://i.imgur.com/4PDNxIA.png" alt="Example of rainbow text" />\n    <figcaption>Example of rainbow text</figcaption>\n</figure>\n\n<br />\n<br />\n\n## Gradient Panel\nThis automates the creation of a panel with gradient text and an optional title.\n\n\n```Python\ndef gradient_panel(text: str, title: str | None = None, num_of_gradients: int = 4) -> Panel:\n    """\n        Args:\n            text (str): The content of the panel.\n            title (Optional[str]): The title of the panel.\n            num_of_gradients (Optional[int]): The number of gradients to use. Valid arguments are between 1 - 6.\n\n        Returns:\n            panel (Panel): A gradient panel.\n    """\n\nconsole.print(gradient_panel("This is even better!!!, title="Gradient Panel"))\n```\n\n<figure>\n    <img src="https://i.imgur.com/5H2qksr.png" alt="Gradient Panel" />\n    <figcaption>Gradient Panel Example</figcaption>\n</figure>\n\n<br />\n<br />\n\n## `gradient`\n\n\n```Python\ndef gradient(message: str, start_color: str, end_color: str) -> Text:\n    """Prints a gradient of the message.\n\n    Args:\n        message (str): The message to print.\n        start_color (str): The HEX start color of the gradient.\n        end_color (str): The HEX end color of the gradient.\n\n    Returns:\n        Text: The message as a Gradient Rich Text object.\n    """\n```\n\n##### Example `gradient` usage:\n```Python\nfrom max_logger import gradient\n\nconsole.print("gradient[^gradient]Simple is always nice...[/]", "#FF0000", "#FF8800"), justify="center")\n```\n\n\n<figure>\n    <img src="https://i.imgur.com/CBZ79sC.png" alt="Two Color Gradient" />\n    <figcaption>Gradient Panel Example</figcaption>\n</figure>\n',
    'author': 'Max Ludden',
    'author_email': 'dev@maxludden.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
