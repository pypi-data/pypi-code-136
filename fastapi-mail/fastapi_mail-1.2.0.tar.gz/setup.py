# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_mail', 'fastapi_mail.email_utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'aiosmtplib>=1.1.6,<2.0.0',
 'blinker>=1.5,<2.0',
 'email-validator>=1.1.3,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'starlette==0.20.4']

extras_require = \
{'aioredis': ['aioredis[aioredis]>=2.0.1,<3.0.0'],
 'httpx': ['httpx[httpx]>=0.23.0,<0.24.0']}

setup_kwargs = {
    'name': 'fastapi-mail',
    'version': '1.2.0',
    'description': 'Simple lightweight mail library for FastApi',
    'long_description': '\n# Fastapi-mail\n\nThe fastapi-mail simple lightweight mail system, sending emails and attachments(individual && bulk)\n\n\n[![MIT licensed](https://img.shields.io/github/license/sabuhish/fastapi-mail)](https://raw.githubusercontent.com/sabuhish/fastapi-mail/master/LICENSE)\n[![GitHub stars](https://img.shields.io/github/stars/sabuhish/fastapi-mail.svg)](https://github.com/sabuhish/fastapi-mail/stargazers)\n[![GitHub forks](https://img.shields.io/github/forks/sabuhish/fastapi-mail.svg)](https://github.com/sabuhish/fastapi-mail/network)\n[![GitHub issues](https://img.shields.io/github/issues-raw/sabuhish/fastapi-mail)](https://github.com/sabuhish/fastapi-mail/issues)\n[![Downloads](https://pepy.tech/badge/fastapi-mail)](https://pepy.tech/project/fastapi-mail)\n\n\n###  🔨  Installation ###\n\n\n```bash\npython3 -m venv .venv\n\nsource .venv/bin/activate\n\npip install fastapi-mail\n\nfor aioredis and httpx\n\npip install \'fastapi-mail[aioredis]\'\npip install \'fastapi-mail[httpx]\'\n\n```\n\nAlternatively, if you prefer to use `poetry` for package dependencies:\n\n```bash\npoetry shell\n\npython add fastapi-mail\n\nfor aioredis and httpx\n\npython add \'fastapi-mail[aioredis]\'\npython add \'fastapi-mail[httpx]\'\n```\n\n---\n**Documentation**: [FastApi-MAIL](https://sabuhish.github.io/fastapi-mail/)\n---\n\n\nThe key features are:\n\n-  sending emails with either with FastApi or using asyncio module \n-  sending emails using FastApi background task managment\n-  sending files either from form-data or files from server\n-  Using Jinja2 HTML Templates\n-  email utils (utility allows you to check temporary email addresses, you can block any email or domain)\n-  email utils has two available classes ```DefaultChecker``` and  ```WhoIsXmlApi```\n-  Unittests using FastapiMail\n\nMore information on [Getting-Started](https://sabuhish.github.io/fastapi-mail/getting-started/)\n\n\n### Guide\n\n\n```python\n\nfrom typing import List\n\nfrom fastapi import BackgroundTasks, FastAPI\nfrom fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType\nfrom pydantic import BaseModel, EmailStr\nfrom starlette.responses import JSONResponse\n\n\n\nclass EmailSchema(BaseModel):\n    email: List[EmailStr]\n\n\nconf = ConnectionConfig(\n    MAIL_USERNAME ="username",\n    MAIL_PASSWORD = "**********",\n    MAIL_FROM = "test@email.com",\n    MAIL_PORT = 465,\n    MAIL_SERVER = "mail server",\n    MAIL_STARTTLS = False,\n    MAIL_SSL_TLS = True,\n    USE_CREDENTIALS = True,\n    VALIDATE_CERTS = True\n)\n\napp = FastAPI()\n\n\nhtml = """\n<p>Thanks for using Fastapi-mail</p> \n"""\n\n\n@app.post("/email")\nasync def simple_send(email: EmailSchema) -> JSONResponse:\n\n    message = MessageSchema(\n        subject="Fastapi-Mail module",\n        recipients=email.dict().get("email"),\n        body=html,\n        subtype=MessageType.html)\n\n    fm = FastMail(conf)\n    await fm.send_message(message)\n    return JSONResponse(status_code=200, content={"message": "email has been sent"})     \n```\n\n## List of Examples\n\nFor more examples of using fastapi-mail please check: \n[example](https://sabuhish.github.io/fastapi-mail/example/) section.\n\n\n## Contributors ✨\n\nThanks goes to these wonderful\n[People](https://sabuhish.github.io/fastapi-mail/contributors.txt)\n\n\n# Contributing\nContributions of any kind are welcome!\n\nBefore you start, please read [CONTRIBUTING](https://github.com/sabuhish/fastapi-mail/blob/master/CONTRIBUTING.md)\n\n\n## LICENSE\n\n[MIT](LICENSE)\n',
    'author': 'Sabuhi Shukurov',
    'author_email': 'sabuhi.shukurov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sabuhish/fastapi-mail',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
