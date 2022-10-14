from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()
requirements = ["httpx", "websocket-client==1.4.1", "websockets==10.3", "setuptools"]

setup(
    name="pymino",
    license='MIT',
    author="forevercynical",
    version="0.3.5",
    author_email="me@cynical.gg",
    description="Amino API wrapper to make bots easier to use",
    url="https://github.com/forevercynical/pymino",
    packages=find_packages(),
    long_description = long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    keywords=[
        'aminoapps', 'amino', 'amino-bots', 'amino-bot', 'amino-bot-api', 'amino-bot-api-python', 'amino-bot-api-python3', 'amino-bot-api-python3-library', "pymino"
    ],
    python_requires='>=3.6',
)
