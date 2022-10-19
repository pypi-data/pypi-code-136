# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['manim_voiceover', 'manim_voiceover.services']

package_data = \
{'': ['*']}

install_requires = \
['azure-cognitiveservices-speech[azure]>=1.24.0,<2.0.0',
 'gTTS[gtts]>=2.2.4,<3.0.0',
 'manim>=0.16.0.post0,<0.17.0',
 'mutagen>=1.46.0,<2.0.0',
 'pydub>=0.25.1,<0.26.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'pyttsx3[pyttsx3]>=2.90,<3.0',
 'sox>=1.4.1,<2.0.0']

entry_points = \
{'manim.plugins': ['manim_voiceover = manim_voiceover']}

setup_kwargs = {
    'name': 'manim-voiceover',
    'version': '0.1.0',
    'description': 'Manim plugin for all things voiceover',
    'long_description': '# manim-voiceover\n\n![Github Actions Status](https://github.com/ManimCommunity/manim-voiceover/workflows/Build/badge.svg)\n[![License](https://img.shields.io/github/license/ManimCommunity/manim-voiceover.svg?color=blue)](https://github.com/ManimCommunity/manim-voiceover/blob/main/LICENSE)\n[![](https://dcbadge.vercel.app/api/server/qY23bthHTY?style=flat)](https://manim.community/discord)\n\n`manim-voiceover` is a [Manim](https://manim.community) plugin for all things voiceover:\n\n- Add voiceovers to Manim videos _directly in Python_ without having to use a video editor.\n- Develop an animation with an auto-generated AI voice without having to re-record and re-sync the audio.\n- Record a voiceover and have it stitched back onto the video instantly. (Note that this is not the same as AI voice cloning)\n\nCurrently supported TTS services:\n\n- [Azure Text to Speech](https://azure.microsoft.com/en-us/services/cognitive-services/text-to-speech/) (Recommended)\n- [gTTS](https://github.com/pndurette/gTTS/)\n- [pyttsx3](https://github.com/nateshmbhat/pyttsx3)\n\n## Installation\n\nInstall from PyPI with the extras `azure` and `gtts`:\n\n```sh\npip install manim-voiceover manim-voiceover[azure] manim-voiceover[gtts]\n```\n\nCheck whether your installation works correctly:\n\n```sh\nmanim -pql examples/gtts-example.py --disable_caching\n```\n\nThe `--disable_caching` flag is required due to a Manim bug. TODO: Remove once the bug is fixed.\n\n[The example above](examples/gtts-example.py) uses [gTTS](https://github.com/pndurette/gTTS/) which calls the Google Translate API and therefore needs an internet connection to work. If it throws an error, there might be a problem with your internet connection or the Google Translate API.\n\n### Installing SoX\n\n`manim-voiceover` can make the output from speech synthesizers faster or slower using [SoX](http://sox.sourceforge.net/) (version 14.4.2 or higher is required).\n\nInstall SoX on Mac with Homebrew:\n\n`brew install sox`\n\nInstall SoX on Debian based distros:\n\n`sudo apt-get install sox`\n\nOr install [from source](https://sourceforge.net/projects/sox/files/sox/).\n\n## Basic Usage\n\nTo use `manim-voiceover`, you simply import the `VoiceoverScene` class from the plugin\n\n```py\nfrom manim_voiceover import VoiceoverScene\n```\n\nYou make sure your Scene classes inherit from `VoiceoverScene`:\n\n```py\nclass MyAwesomeScene(VoiceoverScene):\n    def construct(self):\n        ...\n```\n\n`manim-voiceover` offers multiple text-to-speech engines, some proprietary and some free. A good one to start with is gTTS, which uses Google Translate\'s proprietary API. We found out that this is the best for beginners in terms of cross-platform compatibility---however it needs an internet connection.\n\n```py\nfrom manim_voiceover import VoiceoverScene\nfrom manim_voiceover.interfaces import GTTSService\n\nclass MyAwesomeScene(VoiceoverScene):\n    def construct(self):\n        self.set_speech_service(GTTSService())\n```\n\nThe logic for adding a voiceover is pretty simple. Wrap the animation inside a `with` block that calls `self.voiceover()`:\n\n```py\nwith self.voiceover(text="This circle is drawn as I speak.") as tracker:\n    ... # animate whatever needs to be animated here\n```\n\nManim will animate whatever is inside that with block. If the voiceover hasn\'t finished by the end of the animation, Manim will simply wait until it does. You can further use the `tracker` object for getting the total or remaining duration of the voiceover programmatically, which gives you finer control over the video:\n\n```py\nwith self.voiceover(text="This circle is drawn as I speak.") as tracker:\n    self.play(Create(circle), run_time=tracker.duration)\n```\n\nUsing with-blocks results in clean code, allows you to chain sentences back to back and also serve as a documentation of sorts, as the video is neatly compartmentalized according to whatever lines are spoken during the animations.\n\nSee the [examples directory](./examples) for more examples. We recommend starting with the [gTTS example](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/gtts-example.py).\n\n## Configuring Azure\n\nThe highest quality text-to-speech services available to the public is currently offered by Microsoft Azure. To use it, you need to create an Azure account.\n\nThen, you need to find out your subscription key and service region. Check out [Azure docs](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/) for more details.\n\nCreate a file called `.env` that contains your authentication information in the same directory where you call Manim.\n\n```sh\nAZURE_SUBSCRIPTION_KEY="..."\nAZURE_SERVICE_REGION="..."\n```\n',
    'author': 'The Manim Community Developers',
    'author_email': 'contact@manim.community',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ManimCommunity/manim-voiceover',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
