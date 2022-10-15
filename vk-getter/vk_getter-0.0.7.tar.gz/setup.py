from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.7'
DESCRIPTION = 'Getting data from vk.com in a pythonic way.'
LONG_DESCRIPTION = 'A package that allows to get data from groups in vk.com in just few lines of code.'

# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# setting up
setup(
    name="vk_getter",
    version=VERSION,
    author="Crawlic (Nikita Kuznetsov)",
    author_email="nikitosik0726@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'vk', 'api', 'data', 'images', 'posts', 'get'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)