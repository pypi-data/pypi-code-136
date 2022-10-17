from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="diclass",
    version="1.2.0",
    author="Moses Dastmard",
    description="converts python dictoinary to class object",
    long_description=long_description,
    long_description_content_type='text/markdown'
)