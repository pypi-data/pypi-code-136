# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['everytime']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'everytime',
    'version': '0.2.1',
    'description': 'Schedule asyncio coroutines',
    'long_description': '# everytime - Schedule asyncio coroutines\n\n## TLDR\n```python\n@every.other.wednesday.at(hour=12)\nasync def do_something():\n    ...\n```\n\n## Full Example\n```python\nfrom everytime import every\nimport everytime\n\n@every(5).seconds\nasync def greet():\n    print("Hello")\n\neverytime.run_forever()\n```\n\n## How to schedule coroutines\n\n### everytime expressions as decorators\nAll everytime expressions can be used as function decorators.\n```python\n@every(5).seconds\nasync def greet():\n    print("Hello")\n```\n\n### @schedule\nAternatively you can wrap the everytime expression into a call to `@schedule`.\n```python\n@schedule(every(5).seconds)\nasync def greet():\n    print("Hello")\n```\nThis allows you to pass custom datetime iterables to `@schedule` (see [Schedule custom times](#schedule-custom-times)).\n\n<a id="schedule-custom-times"/>\n\n#### Schedule custom times\n`@schedule` accepts datetime iterables. The following schedules work:\n```python\n@schedule([datetime.fromisoformat(\'2022-11-01T12:00:00\'), datetime.fromisoformat(\'2023-01-01T12:00:00\')])\n\n@schedule(itertools.islice(every.day, 5))\n\n@schedule(map(lambda _: datetime.now() + timedelta(seconds=1), sys.stdin))\n```\n\n### do()\nIf you prefer to keep your function definitions and scheduling rules separate, use the `do`-function.\n```python\nasync def greet():\n    print("Hello")\n\nevery(5).seconds.do(greet)\n```\n\n## Supported Expressions\n\n### Quantification\nEvery time unit can be quantified by `every`, `every.other` or `every(n)`:\n- `every.second`\n- `every.other.second`\n- `every(5).seconds`\n\n### Supported time units\nThe supported time units are\n- `millisecond`\n- `second`\n- `minute`\n- `hour`\n- `day`\n- `week`\n\n### Weekdays\nAlso, weekdays `monday` through `sunday` are supported. `every.wednesday` starts on the next Wednesday. If today is a Wednesday, `every.wednesday` starts today.\n\n### Specific time of the day\n`day` and the weekdays can be scheduled for a specific time of the day:\n```python\nevery.day.at(hour=12, minute=15)\n```\n(Note that `hour` is 24-hour based)\n\n## Event Loops\neverytime uses `asyncio` and schedules coroutines on an event loop.\n\n### Default Behavior\nBy default, all coroutines are scheduled on the same event loop. After all schedules are set, the loop must be invoked with `everytime.run_forever()`\n```python\n@schedule(every.second)\nasync def greet():\n    print("Hello")\n\neverytime.run_forever()\n```\n\n\n### Async Environment\nIf called in an async environment (i.e. there is already an event loop running), coroutines are scheduled on `asyncio.get_running_loop()`.\n\n```python\nasync def main():\n    @schedule(every.second)\n    async def greet():\n        print("Hello")\n\n    await asyncio.sleep(10)\n\nasyncio.run(main())\n```\n\nNote, that the scheduling only works while the loop is running. In this case, `greet` will only be called every second, while `main` is still running.\n\n### Custom Event Loops\nYou can schedule your coroutines to run on a custom event loop by passing an optional argument `loop` to`@schedule` or `do()`.\n\n```python\nl = asyncio.new_event_loop()\n\n@schedule(every.second, loop=l)\nasync def greet():\n    print("Hello")\n\nl.run_forever()\n```\n\n```python\nl = asyncio.new_event_loop()\n\nasync def greet():\n    print("Hello")\n\nevery.second.do(greet, loop=l)\nl.run_forever()\n```\n',
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
