# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['explain_me']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'explain-me',
    'version': '0.2.0',
    'description': 'package explain data concept python',
    'long_description': '# Explain Me\n\n# Example\n```\nfrom explain_me.visual import visualize_package\n\n\n\n\n\nwith open(\'preview.html\', \'w+\') as file:\n    file.write("""\n<html>\n    <body>\n        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>\n        <script>\n            mermaid.initialize({ startOnLoad: true });\n            \n            \n//get svg element.\nvar svg = document.getElementsByTagName(\'svg\')[0];\n\n            \n            \n        </script>\n\n        <div class="mermaid">\n            classDiagram\n    """)\n    \n\n    for line in visualize_package(nama_library):\n        file.write(line+"\\n")\n\n    file.write("""\n            \n        </div>\n        <a id="link" href="#">download</a>\n    </body>\n</html>\n        """)\n```',
    'author': 'vaziria',
    'author_email': 'manorder123@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
