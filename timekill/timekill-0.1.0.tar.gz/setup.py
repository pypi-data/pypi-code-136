# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['timekill',
 'timekill.classify',
 'timekill.load',
 'timekill.suggest',
 'timekill.test']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'desktop-notifier>=3.4.0,<4.0.0',
 'fastapi>=0.85.0,<0.86.0',
 'joblib>=1.2.0,<2.0.0',
 'openai>=0.23.1,<0.24.0',
 'pandas>=1.5.0,<2.0.0',
 'praw>=7.6.0,<8.0.0',
 'requests>=2.28.1,<3.0.0',
 'uvicorn[standard]>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['timekill = timekill.main:main']}

setup_kwargs = {
    'name': 'timekill',
    'version': '0.1.0',
    'description': 'A better way to kill time',
    'long_description': 'timekill\n========\n\n[![Build](https://github.com/ErikBjare/timekill/actions/workflows/build.yml/badge.svg)](https://github.com/ErikBjare/timekill/actions/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Typechecking: mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n\nA better way to kill time.\n\nAn app that suggests healthy ways for you to spend your time, in a context-aware way.\n\n> **Note**\n> This project is a work-in-progress.\n\nFeatures:\n\n - A day-planner that suggests activities for you to do\n   - Taking into account context like time, activity type (work, leisure, etc.), and location. \n   - When configured with activities and the conditions for recommending them, can help you sort out what to do with your days.\n\n - A recommender system for content *that you control*.\n   - Gets content from reddit (later Twitter, Hacker News, etc.)\n   - Includes WIP/experimental content classification/recommendation based on GPT-3.\n\n## Usage\n\n```\n$ timekill --help\nUsage: timekill [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  list     List content with recommendations.\n  plan     Plan a day of activity.\n  start    Entrypoint for the timekill server\n  suggest  Suggest activities to do.\n```\n\n---\n\n**Note:** the text below was written a long time ago, and does not represent the current state of the project.\n\n## Why?\n\nMost of us are guilty of using our phones too much, which wouldn\'t be a problem if most of the use was actually healthy. Instead we spend far more time than we should on social media, YouTube, Netflix, and games. What if we could wire our brains to compulsively open an app that suggested [healthy alternatives](#healthy-timekill) instead?\n\nWhat I suggest is a feed that serves cards with *healthy* and *productive* content. Content feeds are powerful tools that capture our attention by exploiting our brains\' desire for novelty. The question is: can we tame it?\n\n\n## Healthy timekill\n\nHere\'s a list of healthy ways to kill time:\n\n - Work on a task on your TODO list\n - Use learning apps like Brilliant/Khan Academy/Coursera/EdX/Duolingo\n - Work out at home or go to the gym\n - Get only the most useful/recommended content across feeds (see my wiki on [The Importance of Open Recommender Systems](https://erik.bjareholt.com/wiki/importance-of-open-recommendation-systems/))\n   - Can this actually decrease FOMO meaningfully?\n - Staying in touch with friends we haven\'t talked to in a while (as some personal relationship management systems aim to help the user do)\n\nThe important thing for things to make a list like this is that it\'s something the user could *sometimes* actually be willing to do. Different times/moods/places call for different timekill.\n\n\n## Ideas\n\n - Integrate with ActivityWatch\n   - Track how many productive hours timekill helped initiate.\n   - Show a card with the number of productive hours today\n     - You could do the same for unproductive hours, but I\'m not sure that would be very helpful as it basically just shames the user (which could lead to counterproductive results)\n - Add rewards for productive time (this might be a bad idea, would make the motivation extrinsic)\n - Distraction-distracting notifications: Try to distract the user from undesirable activities (social media, games, etc.) by sending notifications that suggest healthier alternatives\n\n## Timeline\n\n### Pre-MVP\n\n - [x] Build a CLI-version of the app (for quick iteration on new features)\n - [ ] Build a very basic web frontend? (for quick GUI iteration)\n\n### MVP\n\nHow do we build an MVP that users like and find helpful as quickly as possible?\n\n - [ ] Needs a way to configure your own activities\n   - How do we get the user to think about good ways to kill time? Offer suggestions/good defaults?\n - [ ] Make it usable from phone\n - [ ] (optional) Integrate with ActivityWatch for better context-awareness\n\n### Marketing\n\n - Set up a ProductHunt ship page (to build a mailing list of people who are interested)\n   - Link from personal, ActivityWatch, and Thankful accounts on social media\n   - Share in local college/programming/startup communities (Code@LTH, D-sektionen community, Lund Startups, Malmö Startups)\n\n\n## Name\n\nCurrent name was just how the one I happened to impulsively use when thinking about it. It might need improvement.\n\n## Similar software\n\nI\'ve discovered similar software that does part of what timekill does.\n\nAutomatic scheduling:\n - Google Calendar\'s "Goals" feature\n - https://usemotion.com/\n - https://super-productivity.com/ (maybe? Haven\'t used)\n\nSelf-hosted/open-source/personal recommender system:\n - None?\n',
    'author': 'Erik Bjäreholt',
    'author_email': 'erik@bjareho.lt',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
