# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bottango_playback_interface']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bottango-playback-interface',
    'version': '0.4.2.dev2',
    'description': 'Bottango Playback Interface',
    'long_description': '# bottango_playback_interface\nControl Bottango through its Web API from python.\n\nThis python3.7+ module is made to interface with Bottango, a Hardware/Robot/Animatronics animation software created by Evan McMahon\n\n## [What is Bottango](https://www.bottango.com/)\n\n## Installation\nInstall through pip with\n\n`pip install bottango_playback_interface`\n\n## Usage\nStart by creating your animations with Bottango, enable the Web API and enter the \'Animate\' mode\n\nThen from your python script\n\n```python\nfrom bottango_playback_interface import BottangoPlaybackInterface\n\nbpi = BottangoPlaybackInterface("localhost", 59224)\nbpi.play_animation("animation_name_to_play")\nbpi.wait_animation_done()\n\n```\n\n### Methods\n```python\nbpi.play_animation("animation_name_to_play")     # Plays the animation with the corresponding name\nbpi.pause_animation()                            # Pause the current animation\nbpi.resume_animation()                           # Resume the current animation\nbpi.get_playback_state()                         # Get various informations from bottango\nbpi.wait_animation_done(timeout=max_wait_time)   # Wait until the animation is over before returning or the timeout runs out.\nbpi.get_animation_list()                         # Returns an array with all available animation names\nbpi.emergency_stop()                             # Turn off live mode from Bottango, must be reenable from there.\n```\n\n\n## Development\ngit clone this project\n\nCreate a new venv\n\n`python3 -m venv --system-site-packages ./venv`\n\nSource it\n\n`source ./venv/bin/activate`\n\nInstall all dependancies with poetry\n\n`poetry install`\n\nInstall git hooks\n\n`pre-commit install`\n\n### Upload to pypi\n\nSource the venv\n\n`source ./venv/bin/activate`\n\nInstall twine\n\n`pip install twine`\n\nConfig your pypi credentials in the file `~/.pypirc`\n\n```python\n[pypi]\nusername = pypi_username\npassword = pypi_password\n```\n\nRun\n\n```python\npoetry install\ntwine check dist/*\ntwine upload dist/*\n```\n',
    'author': 'Martin Rioux',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
