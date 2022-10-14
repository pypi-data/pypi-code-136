# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['egg_timer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'egg-timer',
    'version': '1.0.1',
    'description': 'A simpler way to handle timeouts in Python',
    'long_description': '# EggTimer\n\nThere are some ubiquitous patterns that are elegant and simple. There are\nothers that are not.\n\n```python\nfrom time import time, sleep\n\nstart_time = time()\ntimeout_sec = 42.0\nmax_sleep_time_sec = 1.5\n\nwhile time() - start_time < timeout_sec:\n    # Do or check some stuff\n\n    time_remaining = timeout_sec - (time() - start_time)\n    if time_remaining > 0:\n        sleep(min(time_remaining, max_sleep_time_sec))\n    else:\n        sleep(max_sleep_time_sec)\n```\n\nWhat is the purpose of this loop? Oh, I see, it\'s a timeout. Is the order of\noperations correct in my loop condition? Have I correctly calculated\n`time_remaining`?  Is my `if` clause correct? Hint: it\'s not. How many times\nhave I duplicated this code within my application?\n\nWe can do better. **EggTimer** can help.\n\n```python\nfrom egg_timer import EggTimer\n\ntimer = EggTimer()\ntimer.set(42.0)\nmax_sleep_time_sec = 1.5\n\nwhile not timer.is_expired():\n    # Do or check some stuff\n\n    sleep(min(timer.time_remaining_sec, max_sleep_time_sec))\n```\n\nAh, that\'s better. Clear, concise, reusable, and expressive. The risk of\ndefects is significantly lower, too!\n\n## Installation\nInstall with `pip install -U egg-timer`\n\n## Documentation\n\n```pycon\nPython 3.10.4 (main, Jun 29 2022, 12:14:53) [GCC 11.2.0] on linux\nType "help", "copyright", "credits" or "license" for more information.\n>>> from egg_timer import EggTimer\n>>> help(EggTimer)\nHelp on class EggTimer in module egg_timer.egg_timer:\n\nclass EggTimer(builtins.object)\n |  A class for checking whether or not a certain amount of time has elapsed.\n |\n |  Methods defined here:\n |\n |  __init__(self)\n |      Initialize self.  See help(type(self)) for accurate signature.\n |\n |  is_expired(self)\n |      Check whether or not the timer has expired\n |\n |      :return: True if the elapsed time since set(TIMEOUT_SEC) was called is greater than\n |               TIMEOUT_SEC, False otherwise\n |\n |  reset(self)\n |      Reset the timer without changing the timeout\n |\n |  set(self, timeout_sec: float)\n |      Set a timer\n |\n |      :param timeout_sec: A non-negative floating point number expressing the number of\n |                          seconds to set the timeout for.\n |\n |  ----------------------------------------------------------------------\n |  Readonly properties defined here:\n |\n |  time_remaining_sec\n |      Return the amount of time remaining until the timer expires.\n |\n |      :return: The number of seconds until the timer expires. If the timer is expired, this\n |               function returns 0 (it will never return a negative number).\n |\n |  ----------------------------------------------------------------------\n |  Data descriptors defined here:\n |\n |  __dict__\n |      dictionary for instance variables (if defined)\n |\n |  __weakref__\n |      list of weak references to the object (if defined)\n\n>>>\n```\n\n## Running the tests\n\nRunning the tests is as simple as `poetry install && poetry run pytest`\n',
    'author': 'Mike Salvatore',
    'author_email': 'mike.s.salvatore@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mssalvatore/egg-timer',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
