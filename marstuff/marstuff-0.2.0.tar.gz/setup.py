# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marstuff', 'marstuff.objects']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.2,<9.0.0', 'httpx[http2]>=0.19.0,<0.20.0']

setup_kwargs = {
    'name': 'marstuff',
    'version': '0.2.0',
    'description': "A Python Wrapper for NASA's Mars Rover Photos API",
    'long_description': '<p align="center"><img width=\'900\' src="https://mars.nasa.gov/system/content_pages/main_images/374_mars2020-PIA21635.jpg"></p>\n<h1 align=\'center\'>Marstuff</h1>\n<h3 align=\'center\'>API Wrapper for NASA\'s Mars Rover Photos API</h3>\n<p align="center">\n  <a href="https://pypi.python.org/pypi/marstuff/"><img src=\'https://img.shields.io/badge/MADE%20WITH-Python-red?style=for-the-badge\'/></a>\n  <a href="https://pypi.python.org/pypi/marstuff/"><img src=\'https://img.shields.io/pypi/pyversions/marstuff?style=for-the-badge\'/></a>\n  <a href="https://pypi.python.org/pypi/marstuff/"><img src=\'https://img.shields.io/pypi/status/marstuff?style=for-the-badge\'/></a>\n  <a href="https://pypi.python.org/pypi/marstuff/"><img src=\'https://img.shields.io/pypi/l/marstuff?style=for-the-badge\'/></a>\n  <a href="https://pypi.python.org/pypi/marstuff/"><img src=\'https://img.shields.io/pypi/v/marstuff?style=for-the-badge\'/></a>\n</p>\n\n\n## 📝 Description\nThis is a **Work-In-Progress** Python API Wrapper for NASA\'s Mars Rover Photos API\nwhich provides both **Synchronous** and **Asynchronous** support.\n\n## 🔥 Getting Started\n- ### ⬇️ Installation\n  - Via pip\n    ```\n    pip install marstuff\n    ```\n- ### ✨ Getting a NASA Developer Key\n  - Goto https://api.nasa.gov/\n  - Navigate to `Generate API Key` at the top navbar.\n  ![image](https://user-images.githubusercontent.com/90889682/136913433-d1324685-4205-4497-a2c7-0619fb1dd97b.png)\n  - Fill in your details, and tap `Signup`\n  ![image](https://user-images.githubusercontent.com/90889682/136914064-40e4fbfc-e8f3-46b2-b02e-b270c7cd5c09.png)\n  - Copy Your API Key\n  ![image](https://user-images.githubusercontent.com/90889682/136915687-fcfdc223-e85e-41f6-bcbb-4781ef1e97bc.png)\n- ### ⚡ Quickstart\n  - Synchronously getting, Viewing and Saving the `Latest Photo` of NASA\'s `Curiosity` Rover\n    ```py\n    from marstuff import Client # Import the Client class\n    client = Client("Your API Token") # Make a new Client\n    \n    # Get the latest Photo\n    photo = client.get_latest_photo(client.curiosity)\n    # OR\n    photo = client.curiosity.get_latest_photo()\n    \n    # Display the Photo\n    photo.show()\n    # Save the Photo\n    photo.save("Latest photo of Curiosity.png")\n    ```\n  - Asynchronously getting all the photos taken by the `Rear Hazard Avoidance Camera` of NASA\'s `Curiosity` Rover on sol `3259`\n    ```py\n    from marstuff import AsyncClient # Import the AsyncClient class\n    from marstuff.objects.camera import CAMERAS # Import the list of all CAMERAS\n    import asyncio # Import asyncio\n    \n    client = AsyncClient("Your API Token") # Make a new Client\n    \n    # Make a function for running asyncio\n    async def get_photos():\n        # Get the photo by Curiosity on sol 3259 with the RHAZ camera\n        photos = await client.curiosity.get_all_photos_by_sol(3259, CAMERAS.RHAZ)\n        # OR\n        photos = await client.curiosity.rhaz.get_all_photos_by_sol(3259)\n        print(photos)\n    \n    asyncio.run(get_photos())\n    \n- #### 🧠 General Need-to-Know Stuff!!\n  This API currently provides access to 4 NASA Rovers (`Perseverance`, `Curiosity`, `Opportunity`, and `Spirit`)\n  Each rover, takes photos of the surface of mars via different cameras\n  \n  - The cameras of the `Perseverance` Rover are\n  \n    Abbreviation | Camera                       \n    ------------ | ------------------------------\n    EDL_RUCAM|Rover Up-Look Camera\n    EDL_RDCAM|Rover Down-Look Camera\n    EDL_DDCAM|Descent Stage Down-Look Camera\n    EDL_PUCAM1|Parachute Up-Look Camera A\n    EDL_PUCAM2|Parachute Up-Look Camera B\n    NAVCAM_LEFT|Navigation Camera - Left\n    NAVCAM_RIGHT|Navigation Camera - Right\n    MCZ_RIGHT|Mast Camera Zoom - Right\n    MCZ_LEFT|Mast Camera Zoom - Left\n    FRONT_HAZCAM_LEFT_A|Front Hazard Avoidance Camera - Left\n    FRONT_HAZCAM_RIGHT_A|Front Hazard Avoidance Camera - Right\n    REAR_HAZCAM_LEFT|Rear Hazard Avoidance Camera - Left\n    REAR_HAZCAM_RIGHT|Rear Hazard Avoidance Camera - Right\n    SKYCAM|MEDA Skycam\n    SHERLOC_WATSON|SHERLOC WATSON Camera\n    \n  - Cameras of other Rovers are\n  \n    Abbreviation | Camera                         | Curiosity | Opportunity | Spirit\n    ------------ | ------------------------------ | --------  | ----------- | ------ |\n    FHAZ|Front Hazard Avoidance Camera|✔|✔|✔|\n    RHAZ|Rear Hazard Avoidance Camera|✔|✔|✔|\n    MAST|Mast Camera| ✔||\n    CHEMCAM|Chemistry and Camera Complex  |✔||\n    MAHLI|Mars Hand Lens Imager|✔||\n    MARDI|Mars Descent Imager|✔||\n    NAVCAM|Navigation Camera|✔|✔|✔|\n    PANCAM|Panoramic Camera| |✔|✔|\n    MINITES|Miniature Thermal Emission Spectrometer (Mini-TES)| |✔|✔|\n    \n  You can query via `sol` or `earth_date`\n  - `sol` means `Martian rotation or day` which can be (0 to `Current Sol of Rover`)\n  - `earth_date` is in the format of `YYYY-MM-DD`\n',
    'author': 'Ajay Ratnam',
    'author_email': 'ajratnam.dev@gmail.com',
    'maintainer': 'Ajay Ratnam',
    'maintainer_email': 'ajratnam.dev@gmail.com',
    'url': 'https://github.com/ajratnam/marstuff',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
