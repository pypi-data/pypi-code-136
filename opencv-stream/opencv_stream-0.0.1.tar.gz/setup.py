from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '0.0.1'
DESCRIPTION = 'Wrapper over opencv for video processing and AI'
LONG_DESCRIPTION = 'A package that allows to easily use video and image processing funtionality from opencv'

setup(
    name="opencv_stream",
    version=VERSION,
    author="Oliver",
    author_email="luowensheng2018@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python'],
    keywords=['python', 'video', 'stream', "AI"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)