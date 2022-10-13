# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eskiz_sms']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'eskiz-sms',
    'version': '0.1.18',
    'description': 'Package for eskiz.uz/sms',
    'long_description': '# eskiz-sms\n\neskiz-sms package for eskiz.uz/sms\n\n# Installation\n\n```\npip install eskiz_sms\n```\n\n# Quickstart\n\n```python\nfrom eskiz_sms import EskizSMS\n\nemail = "your_email@mail.com"\npassword = "your_password"\neskiz = EskizSMS(email=email, password=password)\neskiz.send_sms(\'998991234567\', \'message\', from_whom=\'4546\', callback_url=None)\n```\n\n### Using pre-saved token\n\nif after getting a token, you want to save it somewhere and use until it expires, You can pass token value to the\neskiz_sms instance\n\n```python\nfrom eskiz_sms import EskizSMS\n\nyour_saved_token = \'eySomething9320\'\neskiz = EskizSMS(\'email\', \'password\')\neskiz.token.set(your_saved_token)\n\neskiz.send_sms(\'998901234567\', message=\'message\')\n```\n\n### Saving token to env file\n\nIf you set `save_token=True` it will save the token to env file\n\n```python\nfrom eskiz_sms import EskizSMS\n\neskiz = EskizSMS(\'email\', \'password\', save_token=True, env_file_path=\'.env\')\n```',
    'author': 'Malikov',
    'author_email': 'oopanndaa@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/malikovss/eskiz-sms',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
