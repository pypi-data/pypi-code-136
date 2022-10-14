from setuptools import setup 

VERSION = '0.0.20'
DESCRIPTION = 'Streaming video data via networks'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="Mrhellotesthere",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    description='Say hello',
    py_modules=["helloworld"],
    package_dir={'':'src'},
)
