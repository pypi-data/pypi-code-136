from setuptools import setup

setup(
    name="pyrmv",
    version="0.3.2",
    author="Profitroll",
    description="Small module that makes your journey with RMV REST API somehow easier.",
    long_description="Small module that makes your journey with RMV REST API somehow easier. Based fully on official RMV API reference and HAFAS documentation.\n\n## Requirements\n\n* RMV API key (Get it [here](https://opendata.rmv.de/site/start.html))\n* Python3 (Tested versions are 3.7.9 and 3.9.13)\n* git (Only for installation from source)\n\n## Installation\n\nIf you have everything listed in [requirements](#requirements), then let's begin.\n\n### Variant 1\n\n1. `python -m pip install pyrmv`\n\n### Variant 2\n\n1. `git clone https://git.end-play.xyz/profitroll/PythonRMV.git`\n2. `cd PythonRMV`\n3. `python setup.py install`\n\n## Usage\n\n```py\nimport pyrmv\n\n# Define a Client with API key\nclient = pyrmv.Client(\"AcessId\")\n\n# Get origin's and destination's location\norigin = client.stop_by_name(\"Frankfurt Hauptbahnhof\", max_number=3)[0]\ndestination = client.stop_by_coords(50.099613, 8.685449, max_number=3)[0]\n\n# Find a trip by locations got\ntrip = client.trip_find(origin_id=origin.id, dest_id=destination.id)\n```\n\n## Frequently Asked Questions\n\n* [Why are there raw versions and formatted ones?](#why-are-there-raw-versions-and-formatted-ones)\n* [Some methods work slightly different](#some-methods-work-slightly-different)\n\n### Why are there raw versions and formatted ones?\n\nFor the purposes of my projects I don't really need all the stuff RMV gives (even though it's not much).\nI only need some specific things. However I do understand that in some cases other users may find\nthose methods quite useful so I implemented them as well.\n\n### Some methods work slightly different\n\nCan be. Not all function arguments written may work perfectly because I simply did not test each and\nevery request. Some of arguments may be irrelevant in my use-case and the others are used quite rare at all.\nJust [make an issue](https://git.end-play.xyz/profitroll/PythonRMV/issues/new) and I'll implement it correct when I'll have some free time.\n\n## To-Do\n\n### General\n\n* [ ] Docs in Wiki\n* [ ] Tickets",
    long_description_content_type="text/markdown",
    author_email="profitroll@end-play.xyz",
    url="https://git.end-play.xyz/profitroll/PythonRMV",
    project_urls={
        "Bug Tracker": "https://git.end-play.xyz/profitroll/PythonRMV/issues",
        "Documentation": "https://git.end-play.xyz/profitroll/PythonRMV/wiki",
        "Source Code": "https://git.end-play.xyz/profitroll/PythonRMV.git",
    },
    packages=[
        "pyrmv",
        "pyrmv.raw",
        "pyrmv.const",
        "pyrmv.enums",
        "pyrmv.errors",
        "pyrmv.utility",
        "pyrmv.classes"
    ],
    install_requires=[
        "requests",
        "xmltodict",
        "isodate"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ]
)