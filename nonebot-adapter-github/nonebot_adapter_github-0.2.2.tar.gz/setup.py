# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot', 'nonebot.adapters.github']

package_data = \
{'': ['*']}

install_requires = \
['githubkit[auth-app]>=0.7.0,<1.0.0', 'nonebot2>=2.0.0-beta.5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-adapter-github',
    'version': '0.2.2',
    'description': 'GitHub adapter for nonebot2',
    'long_description': '<!-- markdownlint-disable-next-line MD041 -->\n<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# NoneBot-Adapter-GitHub\n\n<!-- markdownlint-capture -->\n<!-- markdownlint-disable MD036 -->\n\n_✨ GitHub 协议适配 ✨_\n\n<!-- markdownlint-restore -->\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/nonebot/adapter-github/master/LICENSE">\n    <img src="https://img.shields.io/github/license/nonebot/adapter-github" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-adapter-github">\n    <img src="https://img.shields.io/pypi/v/nonebot-adapter-github" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.8+-blue" alt="python">\n  <a href="https://results.pre-commit.ci/latest/github/nonebot/adapter-github/master">\n    <img src="https://results.pre-commit.ci/badge/github/nonebot/adapter-github/master.svg" />\n  </a>\n  <br />\n  <a href="https://jq.qq.com/?_wv=1027&k=5OFifDh">\n    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-768887710-orange?style=flat-square" alt="QQ Chat Group">\n  </a>\n  <a href="https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&appChannel=share&inviteCode=7b4a3&appChannel=share&businessType=9&from=246610&biz=ka">\n    <img src="https://img.shields.io/badge/QQ%E9%A2%91%E9%81%93-NoneBot-5492ff?style=flat-square" alt="QQ Channel">\n  </a>\n  <a href="https://t.me/botuniverse">\n    <img src="https://img.shields.io/badge/telegram-botuniverse-blue?style=flat-square" alt="Telegram Channel">\n  </a>\n  <a href="https://discord.gg/VKtE6Gdc4h">\n    <img src="https://discordapp.com/api/guilds/847819937858584596/widget.png?style=shield" alt="Discord Server">\n  </a>\n</p>\n\n## 安装\n\n```bash\npoetry add nonebot-adapter-github\n# 或者\npip install nonebot-adapter-github\n```\n\n## 加载适配器\n\n```python\nimport nonebot\nfrom nonebot.adapters.github import Adapter\n\nnonebot.init()\n\ndriver = nonebot.get_driver()\ndriver.register_adapter(Adapter)\n```\n\n## 配置\n\n### 配置 APP\n\n```dotenv\nGITHUB_APPS=\'\n[\n  {\n    "app_id": "123456",  # GitHub App ID 必填\n    "private_key": [\n      "-----BEGIN RSA PRIVATE KEY-----"\n      "...",\n      "-----END RSA PRIVATE KEY-----"\n    ],  # GitHub App 私钥必填\n    "client_id": "123456",  # OAuth App Client ID 必填，GitHub App 可选\n    "client_secret": "xxxxxx",  # OAuth App Client Secret 必填，GitHub App 可选\n    "webhook_secret": "xxxxxx"  # 可选\n  }\n]\'\n```\n\n### 其他配置\n\n```dotenv\nGITHUB_BASE_URL=https://api.github.com\nGITHUB_ACCEPR_FORMAT=full+json\nGITHUB_PREVIEWS=["starfox"]\n```\n\n## 使用\n\n### WebHook\n\nURL: `/github/webhooks/<app_id>` (GitHub APP) / `/github/webhooks/<client_id>` (OAuth APP)\n\n事件格式:\n\n```python\nclass Event(BaseModel):\n    id: str  # 事件 ID\n    name: str  # 事件名称\n    payload: Dict[str, Any]  # 事件内容\n\n    to_me: bool = False  # 是否 @ 了机器人或机器人昵称\n```\n\n具体事件类型及内容请参考 [GitHub Developer](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads)\n\n### 调用 API\n\n可以直接通过 bot 调用 API，但是请注意 **只能使用异步接口，参数必须是 keyword args**。具体使用方法参考 [githubkit](https://github.com/yanyongyu/githubkit)。\n\n```python\nasync with bot.as_installation(installation_id=1):\n    resp = await bot.rest.issues.async_get(owner="owner", repo="repo", issue_number=1)\n    issue = resp.parsed_data\n\n    resp = await bot.async_graphql(query=query)\n\n    async for issue in bot.github.paginate(bot.rest.issues.async_list_for_repo, owner="owner", repo="repo"):\n        print(issue)\n```\n\n也可以直接使用 `githubkit`，但是将绕过 NoneBot 的 `call api hook`。\n\n```python\ngithub = bot.github\n```\n',
    'author': 'yanyongyu',
    'author_email': 'yyy@nonebot.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nonebot/adapter-github',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
