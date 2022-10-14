# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notion2md',
 'notion2md.console',
 'notion2md.console.commands',
 'notion2md.console.ui',
 'notion2md.convertor',
 'notion2md.exporter']

package_data = \
{'': ['*']}

install_requires = \
['cleo==1.0.0a4', 'notion-client>=1.0.1']

entry_points = \
{'console_scripts': ['notion2md = notion2md.console.application:main']}

setup_kwargs = {
    'name': 'notion2md',
    'version': '2.8.0',
    'description': 'Notion Markdown Exporter with Python Cli',
    'long_description': '![Notion2Md logo - an arrow pointing from "N" to "MD"](Notion2md.jpg)\n\n<br/>\n\n## About Notion2Md\n\n[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)\n[![Code Quality](https://github.com/echo724/notion2md/actions/workflows/code_quality.yaml/badge.svg)](https://github.com/echo724/notion2md/actions/workflows/code_quality.yaml)\n<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fecho724%2Fnotion2md&count_bg=%23949191&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=visited&edge_flat=false"/></a>\n\n- Notion Markdown Exporter using **official notion api** by [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)\n\n### Notion2Medium\n\n- Check out [Notion2Medium](https://github.com/echo724/notion2medium) that publishes a **Medium** post from **Notion** using Notion2Md.\n\n## API Key(Token)\n\n- Before getting started, create [an integration and find the token](https://www.notion.so/my-integrations). → [Learn more about authorization](https://developers.notion.com/docs/authorization).\n\n- Then save your api key(token) as your os environment variable\n\n```Bash\n$ export NOTION_TOKEN="{your integration token key}"\n```\n\n## Install\n\n```Bash\n$ pip install notion2md\n```\n\n## Usage: Shell Command\n\n![Terminal output of the `notion2md -h` command](notion2md_options.png)\n\n- Notion2md requires either `id` or `url` of the Notion page/block.\n\n- **download** option will download files/images in the `path` directory.\n\n- **unzipped** option makes Notion2Md export ***unzipped*** output of Notion block.\n\n```Bash\nnotion2md --download -n post -p ~/MyBlog/content/posts -u https://notion.so/...\n```\n\n- This command will generate "**post.zip**" in your \'**~/MyBlog/content/posts**\' directory.\n\n## Usage: Python\n\n```Python\nfrom notion2md.exporter.block import MarkdownExporter, StringExporter\n\n# MarkdownExporter will make markdown file on your output path\nMarkdownExporter(page_id=\'...\',output_path=\'...\',download=True).export()\n\n# StringExporter will return output as String type\nmd = StringExporter(page_id=\'...\',output_path=\'...\').export()\n```\n\n## To-do\n\n- [x] Download file object(image and files)\n- [x] Table blocks\n- [x] Synced Block\n- [ ] Page Exporter\n- [ ] Child page\n- [ ] Column List and Column Blocks\n\n## Contribution\n\nPlease read [Contribution Guide](CONTRIBUTION.md)\n\n## Donation\n\nIf you think **Notion2Md** is helpful to you, you can support me here:\n\n<a href="https://www.buymeacoffee.com/echo724" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 54px;" height="54"></a>\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'echo724',
    'author_email': 'eunchan1001@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/echo724/notion2md.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
