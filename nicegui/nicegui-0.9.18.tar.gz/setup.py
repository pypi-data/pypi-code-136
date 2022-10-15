# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nicegui', 'nicegui.elements', 'nicegui.static.templates']

package_data = \
{'': ['*'],
 'nicegui': ['static/*'],
 'nicegui.elements': ['lib/*'],
 'nicegui.static.templates': ['css/*',
                              'highcharts/*',
                              'js/*',
                              'local/*',
                              'local/fontawesome/css/*',
                              'local/fontawesome/webfonts/*',
                              'local/ionicons/*',
                              'local/materialdesignicons/iconfont/*',
                              'local/robotofont/*',
                              'local/tailwind/*']}

install_requires = \
['Pygments>=2.9.0,<3.0.0',
 'asttokens>=2.0.5,<3.0.0',
 'docutils>=0.17.1,<0.18.0',
 'httpx>=0.23.0,<0.24.0',
 'justpy>=0.2.3,<0.3.0',
 'markdown2>=2.4.3,<3.0.0',
 'matplotlib>=3.4.1,<4.0.0',
 'typing-extensions>=3.10.0',
 'uvicorn>=0.18.0,<0.19.0',
 'watchfiles>=0.16.1,<0.17.0',
 'websockets>=10.3,<11.0']

setup_kwargs = {
    'name': 'nicegui',
    'version': '0.9.18',
    'description': 'Web User Interface with Buttons, Dialogs, Markdown, 3D Scences and Plots',
    'long_description': '<img src="https://raw.githubusercontent.com/zauberzeug/nicegui/main/sceenshots/ui-elements.png" width="300" align="right">\n\n# NiceGUI\n\nNiceGUI is an easy-to-use, Python-based UI framework, which shows up in your web browser.\nYou can create buttons, dialogs, markdown, 3D scenes, plots and much more.\n\nIt is great for micro web apps, dashboards, robotics projects, smart home solutions and similar use cases.\nYou can also use it in development, for example when tweaking/configuring a machine learning algorithm or tuning motor controllers.\n\nNiceGUI is available as [PyPI package](https://pypi.org/project/nicegui/), [Docker image](https://hub.docker.com/r/zauberzeug/nicegui) and on [GitHub](https://github.com/zauberzeug/nicegui).\n\n[![PyPI version](https://badge.fury.io/py/nicegui.svg)](https://pypi.org/project/nicegui/)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/nicegui)](https://pypi.org/project/nicegui/)\n[![Docker Pulls](https://img.shields.io/docker/pulls/zauberzeug/nicegui)](https://hub.docker.com/r/zauberzeug/nicegui)<br />\n[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/zauberzeug/nicegui)](https://github.com/zauberzeug/nicegui/graphs/commit-activity)\n[![GitHub issues](https://img.shields.io/github/issues/zauberzeug/nicegui)](https://github.com/zauberzeug/nicegui/issues)\n[![GitHub forks](https://img.shields.io/github/forks/zauberzeug/nicegui)](https://github.com/zauberzeug/nicegui/network)\n[![GitHub stars](https://img.shields.io/github/stars/zauberzeug/nicegui)](https://github.com/zauberzeug/nicegui/stargazers)\n[![GitHub license](https://img.shields.io/github/license/zauberzeug/nicegui)](https://github.com/zauberzeug/nicegui/blob/main/LICENSE)\n\n## Features\n\n- browser-based graphical user interface\n- implicit reload on code change\n- standard GUI elements like label, button, checkbox, switch, slider, input, file upload, ...\n- simple grouping with rows, columns, cards and dialogs\n- general-purpose HTML and markdown elements\n- powerful high-level elements to\n  - plot graphs and charts,\n  - render 3D scenes,\n  - get steering events via virtual joysticks\n  - annotate and overlay images\n  - interact with tables\n  - navigate foldable tree structures\n- built-in timer to refresh data in intervals (even every 10 ms)\n- straight-forward data binding to write even less code\n- notifications, dialogs and menus to provide state of the art user interaction\n- shared and individual web pages\n- ability to add custom routes and data responses\n- capture keyboard input for global shortcuts etc\n- customize look by defining primary, secondary and accent colors\n- live-cycle events and session data\n\n## Installation\n\n```bash\npython3 -m pip install nicegui\n```\n\n## Usage\n\nWrite your nice GUI in a file `main.py`:\n\n```python\nfrom nicegui import ui\n\nui.label(\'Hello NiceGUI!\')\nui.button(\'BUTTON\', on_click=lambda: ui.notify(\'button was pressed\'))\n\nui.run()\n```\n\nLaunch it with:\n\n```bash\npython3 main.py\n```\n\nThe GUI is now available through http://localhost:8080/ in your browser.\nNote: NiceGUI will automatically reload the page when you modify the code.\n\n## Documentation and Examples\n\nThe API reference is hosted at [https://nicegui.io/reference](https://nicegui.io/reference) and provides a ton of live examples.\nThe whole content of [https://nicegui.io](https://nicegui.io) is [implemented with NiceGUI itself](https://github.com/zauberzeug/nicegui/blob/main/main.py).\n\nYou may also have a look at the following examples for in-depth demonstrations of what you can do with NiceGUI:\n\n- [Slideshow](https://github.com/zauberzeug/nicegui/tree/main/examples/slideshow/main.py):\n  implements a keyboard-controlled image slideshow\n- [Authentication](https://github.com/zauberzeug/nicegui/blob/main/examples/authentication/main.py):\n  shows how to use sessions to build a login screen\n- [Customization](https://github.com/zauberzeug/nicegui/blob/main/examples/customization/main.py):\n  provides an example of how to modularize your application into multiple files and create a specialized `@ui.page` decorator\n- [Map](https://github.com/zauberzeug/nicegui/blob/main/examples/map/main.py):\n  uses the JavaScript library [leaflet](https://leafletjs.com/) to display a map at specific locations\n- [AI User Interface](https://github.com/zauberzeug/nicegui/blob/main/examples/ai_interface/main.py):\n  utilizes the great but non-async API from <https://replicate.com> to perform voice-to-text transcription and generate images from prompts with Stable Diffusion\n- [3D scene](https://github.com/zauberzeug/nicegui/blob/main/examples/3d_scene/main.py):\n  creates a 3D scene and loads an STL mesh illuminated with a spotlight\n\n## Why?\n\nWe like [Streamlit](https://streamlit.io/) but find it does [too much magic when it comes to state handling](https://github.com/zauberzeug/nicegui/issues/1#issuecomment-847413651).\nIn search for an alternative nice library to write simple graphical user interfaces in Python we discovered [JustPy](https://justpy.io/).\nWhile we liked the approach, it is too "low-level HTML" for our daily usage.\n\nTherefore we created NiceGUI on top of [JustPy](https://justpy.io/),\nwhich itself is based on the ASGI framework [Starlette](https://www.starlette.io/) (like [FastAPI](https://fastapi.tiangolo.com/)) and the ASGI webserver [Uvicorn](https://www.uvicorn.org/).\n\n## Docker\n\nYou can use our [multi-arch Docker image](https://hub.docker.com/repository/docker/zauberzeug/nicegui):\n\n```bash\ndocker run --rm -p 8888:8080 -v $(pwd):/app/ -it zauberzeug/nicegui:latest\n```\n\nThis will start the server at http://localhost:8888 with the code from your current directory.\nThe file containing your `ui.run(port=8080, ...)` command must be named `main.py`.\nCode modification triggers an automatic reload.\n\n## Deployment\n\nTo deploy your NiceGUI app, you will need to execute your `main.py` (or whichever file contains your `ui.run(...)`) on your server infrastructure.\nYou can either install the [NiceGUI python package via pip](https://pypi.org/project/nicegui/) on the server or use our [pre-built Docker image](https://hub.docker.com/r/zauberzeug/nicegui) which contains all necessary dependencies (see above).\nFor example you can use this `docker run` command to start the script `main.py` in the current directory on port 80:\n\n```bash\ndocker run -p 80:8080 -v $(pwd)/:/app/ -d --restart always zauberzeug/nicegui:latest\n```\n\nThe example assumes `main.py` uses the port 8080 in the `ui.run` command (which is the default).\nThe `--restart always` makes sure the container is restarted if the app crashes or the server reboots.\nOf course this can also be written in a docker compose file:\n\n```yaml\nnicegui:\n  image: zauberzeug/nicegui:latest\n  restart: always\n  ports:\n    - 80:8080\n  volumes:\n    - ./:/app/\n```\n\nWhile it is possible to provide SSL certificates directly through NiceGUI (using [JustPy config](https://justpy.io/reference/configuration/)), we also like reverse proxies like [Traefik](https://doc.traefik.io/traefik/) or [NGINX](https://www.nginx.com/).\nSee our [docker-compose.yml](https://github.com/zauberzeug/nicegui/blob/main/docker-compose.yml) as an example.\n',
    'author': 'Zauberzeug GmbH',
    'author_email': 'info@zauberzeug.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zauberzeug/nicegui',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
