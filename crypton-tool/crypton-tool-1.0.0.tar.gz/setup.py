# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crypton_tool']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=38.0.1,<39.0.0']

entry_points = \
{'console_scripts': ['crypton = crypton_tool.cli:main']}

setup_kwargs = {
    'name': 'crypton-tool',
    'version': '1.0.0',
    'description': 'Crypton Tool simple way to cryptography files and content',
    'long_description': '# Crypton Tool\n\nCrypton Tool é baseado no pacote <a href="https://cryptography.io/" target="_blank">cryptography.io</a> e tem por objetivo disponibilizar métodos para cryptar arquivos e conteúdos, além de disponibilizar comandos CLI. \n\n**Documentação:** <a href="https://msbar.github.io/crypton-tool" target="_blank">https://msbar.github.io/crypton-tool</a>\n\n**Source code:** <a href="https://github.com/msbar/crypton-tool" target="_blank">https://github.com/msbar/crypton-tool</a>\n\n## Instalação:\n\n```\npip install crypton-tool\n```\n\n## Exemplos:\n\n### Criptando um arquivo ou arquivos em uma pasta.\n```Python linenums="1"\nfrom crypton_tool.crypton import Crypton\n\nCrypton.generate_key(to_file=\'seu/caminho\')\ntoken = Crypton.read_token_file("seu/caminho/token.crypton")\n```\n\n### Criptando um arquivo ou arquivos em uma pasta.\n```Python linenums="1"\ncrypt.encrypt_file(\'caminho/para/arquivo_ou_pasta\')\n```\n\n### Decriptando um arquivo ou arquivos em uma pasta.\n```Python linenums="1"\ncrypt.decrypt_file(\'caminho/para/arquivo_ou_pasta\')\n```',
    'author': 'Marciel Barcellos',
    'author_email': 'msbar2@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/msbar/crypton-tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
