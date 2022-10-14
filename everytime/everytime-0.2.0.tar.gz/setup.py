# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['everytime']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'everytime',
    'version': '0.2.0',
    'description': 'Schedule asyncio coroutines',
    'long_description': '# everytime - Schedule asyncio coroutines\n\n## TLDR\n```python\n@schedule(every.other.wednesday.at(hour=12), loop)\nasync def do_something():\n    ...\n```\nto schedule `do_something()` every second Wednesday at 12:00 on the `asyncio.EventLoop` called `loop`. `loop` has to be running for that.\n\n## Full Example\n```python\nimport asyncio\nfrom everytime import *\n\nloop = asyncio.new_event_loop()\n\nasync def greet():\n    print("Hello")\n\nevery(5).seconds.do(greet, loop)\nloop.run_forever()\n```\n\n## Schedule with do()\nYou can schedule actions with the `do` function.\n```python\nasync def greet():\n    print("Hello")\n\nevery(5).seconds.do(greet, loop)\n```\n\n## Schedule with decorators\nIf you prefer, you can decorate your action with an everytime expression.\n```python\n@schedule(every(5).seconds, loop)\nasync def greet():\n    print("Hello")\n```\n\n## Schedule custom times\n`@schedule` accepts datetime iterables. The following schedules work:\n```python\n@schedule([datetime.fromisoformat(\'2022-11-01T12:00:00\'), datetime.fromisoformat(\'2023-01-01T12:00:00\')], loop)\n\n@schedule(itertools.islice(every.day, 5), loop)\n\n@schedule(map(lambda _: datetime.now() + timedelta(seconds=1), sys.stdin), loop)\n```\n\n## Supported Expressions\n\n### Quantification\nEvery time unit can be quantified by `every`, `every.other` or `every(n)`:\n- `every.second`\n- `every.other.second`\n- `every(5).seconds`\n\n### Supported time units\nThe supported time units are\n- `millisecond`\n- `second`\n- `minute`\n- `hour`\n- `day`\n- `week`\n\n### Weekdays\nAlso, weekdays `monday` through `sunday` are supported. `every.wednesday` starts on the next Wednesday. If today is a Wednesday, `every.wednesday` starts today.\n\n### Specific time of the day\n`day` and the weekdays can be scheduled for a specific time of the day:\n```python\nevery.day.at(hour=12, minute=15)\n```\n(Note that `hour` is 24-hour based)\n',
    'author': 'meipp',
    'author_email': 'meipp@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/meipp/every/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
