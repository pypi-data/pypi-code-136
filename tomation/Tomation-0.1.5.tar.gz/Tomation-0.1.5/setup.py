from pyparsing import Keyword
import setuptools
from setuptools import *

setup(
    name="Tomation",   
    version="0.1.5",
    author="Eekk2k2",
    author_email="eekk2k2@gmail.com",
    description="Automation library for small or big tasks.",
    long_description=open('README.md').read() + '\n\n' + open("CHANGELOG.txt").read(),
    # long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    keywords='Task Automation',
    packages=setuptools.find_packages(),
    install_requires=['pyautogui', "psutil", "win32", "PIL", "selenium", "webdriver_manager", "bs4", "os", "sys", "re", "numpy"]
)
