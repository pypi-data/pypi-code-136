# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cardanopythonlib']

package_data = \
{'': ['*']}

install_requires = \
['cerberus>=1.3.4,<2.0.0']

setup_kwargs = {
    'name': 'cardanopythonlib',
    'version': '1.0.4',
    'description': 'Cardano Python lib to interact with the blockchain',
    'long_description': '# CardanoPythonLib\n\n### Cardano Python Library\n\nThis is a Python library to interact with Cardano Blockchain. \n\n### Installation\n\n#\n\n1. Prerequesites\n\n- Minimum: Cardano-cli. You will be able to run offchain code, generate keys, create and sign transactions.\n- Desired: Cardano-node running. You will be able to submit onchain and get confirmations from the blockchain.\n- Unlock more: Cardano wallet installed. You will be able to create wallets using the Cardano Wallet API.\n\n> As a side note, we are working to allow the interaction of this library with the Cardano blockchain without the need of any cardano node or even cardano CLI/wallet/address installed locally.\n\n2. Virtual environment setup\nAs you might know, it is recommended to run python code from a virtual environment to isolate your installation and keep everything clean and organized. \n\nI work with virtualenvwrapper but you can use your prefered choice. For virtualenvwrapper:\n\n    sudo apt install python3-pip\n    sudo -H pip3 install --upgrade pip\n    sudo -H pip3 install virtualenv virtualenvwrapper\n\n    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc\n\n    echo "export WORKON_HOME=~/Env" >> ~/.bashrc\n    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc\n\nCreate the virtual environment\n\n    mkvirtualenv <pick a cool name>\n\nList all virtual environments\n\n    lsvirtualenv\n\n3. CardanoPythonLib installation\n\n> CardanoPythonlib library is in PyPi. Link to official site: https://pypi.org/project/cardanopythonlib/\n\n- Option 1. Pip installation\n\nWith the virtual environment active\n\n    pip install cardanopythonlib\n\nThe library relies on a cardano_config.ini file which connects to Cardano testnet by default. If you want to overwrite some of the parameters, please create a new ini file in your folder:\n\n    [node]\n    KEYS_FILE_PATH = ./.priv/wallets\n    TRANSACTION_PATH_FILE = ./.priv/transactions\n    CARDANO_NETWORK = testnet\n    CARDANO_NETWORK_MAGIC = 1097911063\n    CARDANO_CLI_PATH = cardano-cli\n    URL = http://localhost:8090/v2/wallets/\n\nWhen using CARDANO_NETOWRK = mainnet the CARDANO_NETWORK_MAGIC is ignored. \n\nInstantiate the class as follows:\n\n```python\nfrom cardanopythonlib import base\n\nconfig_path = \'./cardano_config.ini\' # Optional argument\nnode = base.Node(config_path) # Or with the default ini: node = base.Node()\nnode.query_tip_exec()\n```\n\n\n- Option 2. Download the library from github\n\n    git clone https://github.com/larestrepo/CardanoPythonLib.git\n\n4. Install requirements\n\nMake sure to have active your virtual environment\n\n    pip install -r requirements.txt\n\nYou should be good to go\n\n#\n\n### Working with the library\n\ncardanopythonlib folder is the package that contains the main functionalities. \n\nbase.py file contains 3 classes.\n\n- Starter\n- Node\n- Keys\n\nFor usage please go to docs folder.\n\n#\n',
    'author': 'Moxie',
    'author_email': 'luis.restrepo@ayllu.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/larestrepo/CardanoPythonLib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
