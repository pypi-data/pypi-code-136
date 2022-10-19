# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['appstore_tools', 'appstore_tools.actions', 'appstore_tools.appstore']

package_data = \
{'': ['*']}

install_requires = \
['ConfigArgParse>=1.2.3,<2.0.0',
 'PyJWT>=2.5.0,<3.0.0',
 'Pygments>=2.7.4,<3.0.0',
 'argparse-color-formatter>=1.2.2,<2.0.0',
 'colorama>=0.4.4,<0.5.0',
 'cryptography>=3.3.1,<4.0.0',
 'requests>=2.25.1,<3.0.0',
 'tqdm>=4.56.0,<5.0.0']

entry_points = \
{'console_scripts': ['appstore-tools = appstore_tools:run']}

setup_kwargs = {
    'name': 'appstore-tools',
    'version': '0.1.6',
    'description': 'Tools for the AppStore Connect API.',
    'long_description': '# appstore-tools\n\nTools for the AppStore Connect API.\n\nThis package provides methods to publish, download, and list information about AppStore meta-data (descriptions, keywords, screenshots, previews, etc).  Combined with a deployment workflow (such as github actions), the AppStore meta-data can be tracked and deployed along side the rest of the app\'s source code and assets.\n\n## Install\n\n```zsh\npip install appstore-tools\n```\n\n## Usage\n\n```zsh\nappstore-tools [-h] [--version] action [args]\n```\n\nExamples:\n\n```zsh\n# List all apps under the app store account\nappstore-tools apps\n\n# Download the assets for an app\nappstore-tools download --bundle-id com.example.myapp --asset-dir myassets\n\n# Publish the assets for an app\nappstore-tools publish --bundle-id com.example.myapp --asset-dir myassets\n```\n\n## Usage Config\n\nMost actions will require authentication with the AppStore Connect API, as well as specifying which app to target.\n\nAll these parameters can be passed via command line argument, but for convenience, they (and any others) can also be loaded from a config file.\n\nUse the default config file path of `appstore_tools.config`, or specify another with `--config-file CONFIG_FILE`.\n\n```ini\n; appstore_tools.config\n; sample contents\nissuer-id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\nkey-id=XXXXXXXXXX\nkey-file=/home/me/AppStoreConnect_AuthKey_XXXXXXXXXX.p8\nbundle-id=com.example.myapp\n```\n\n## Code\n\nThe actions provided by the command line can also be accessed by import in a python script.\n\n```python\n# Import the package\nfrom appstore_tools import appstore, actions\n\n# Get the auth credentials\nwith open("AuthKey.p8", "r") as file:\n    key = file.read()\n\nissuer_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"\nkey_id="XXXXXXXXXX"\n\n# Create an access token\naccess_token = appstore.create_access_token(\n    issuer_id=issuer_id, key_id=key_id, key=key\n)\n\n# Call the AppStore connect API\napps = appstore.get_apps(access_token=access_token)\n\n# Or call one of the AppStore-Tools Actions\nactions.list_apps(access_token=access_token)\n\n```\n\n## Asset Directory Structure\n\nThe `download` and `publish` actions look for assets in the following directory structure starting at `--asset-dir ASSET_DIR`. Screenshots and Previews are sorted alphabetically in the store listing.\n\nTo leave an attribute unaffected by the `publish` action, remove the corresponding text file from the tree. An empty text file can be used to set the attribute to an empty string.\n\nLikewise, to leave the screenshots (or previews) unaffected, remove the entire `screenshots` folder. If `screenshots` is present, the `publish` action will add/remove screenshot-display-types and their screenshots to match.\n\n```zsh\n[ASSET_DIR]\n└── com.example.myapp\n    └── en-US\n        ├── description.txt\n        ├── keywords.txt\n        ├── marketingUrl.txt\n        ├── name.txt\n        ├── previews\n        ├── privacyPolicyText.txt\n        ├── privacyPolicyUrl.txt\n        ├── promotionalText.txt\n        ├── screenshots\n        │\xa0\xa0 ├── APP_IPAD_PRO_129\n        │\xa0\xa0 │\xa0\xa0 ├── 10_Image.png\n        │\xa0\xa0 │\xa0\xa0 ├── 20_AnotherImage.png\n        │\xa0\xa0 │\xa0\xa0 ├── 30_MoreImages.png\n        │\xa0\xa0 ├── APP_IPAD_PRO_3GEN_129\n        │\xa0\xa0 │\xa0\xa0 ├── a_is_the_first_letter.png\n        │\xa0\xa0 │\xa0\xa0 ├── b_is_the_second_letter.png\n        │\xa0\xa0 │\xa0\xa0 ├── c_is_the_third_letter.png\n        │\xa0\xa0 ├── APP_IPHONE_55\n        │\xa0\xa0 │\xa0\xa0 ├── image01.png\n        │\xa0\xa0 │\xa0\xa0 ├── image02.png\n        │\xa0\xa0 │\xa0\xa0 ├── image03.png\n        │\xa0\xa0 └── APP_IPHONE_65\n        │\xa0\xa0 │\xa0\xa0 ├── image01.png\n        │\xa0\xa0 │\xa0\xa0 ├── image02.png\n        │\xa0\xa0 │\xa0\xa0 ├── image03.png\n        ├── subtitle.txt\n        ├── supportUrl.txt\n        └── whatsNew.txt\n```\n\n## Source\n\nClone the source code\n\n```zsh\ngit clone https://github.com/bennord/appstore-tools.git\n```\n\nInstall dependencies\n\n```zsh\npoetry install\n```\n\nRun from within project environment\n\n```zsh\npoetry shell\nappstore-tools --version\n```\n',
    'author': 'Ben Nordstrom',
    'author_email': 'bennord@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bennord/appstore-tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
