# coding utf8
import setuptools
from bioresource.versions import get_versions

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="BioResource",
    version=get_versions(),
    author="Yuxing Xu",
    author_email="xuyuxing@mail.kib.ac.cn",
    description="A tool for easy and fast access to biological big data",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/SouthernCD/BioResource",

    # entry_points={
    #     "console_scripts": ["BioResource = bioresource.cli:main"]
    # },    

    packages=setuptools.find_packages(),

    install_requires=[
        "toolbiox>=0.0.13"
        "beautifulsoup4>=4.11.1",
        "requests>=2.28.1",
        "retry",
    ],

    python_requires='>=3.5',
)