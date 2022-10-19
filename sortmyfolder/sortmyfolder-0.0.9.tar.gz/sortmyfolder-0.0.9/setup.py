import pathlib
from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent.resolve()
install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

VERSION='0.0.9'
DESCRIPTION = 'Auto sorting tool to allow you organise any file or folder in a directory using the file extensions'

with open("README.md", "r") as fh:
    long_description=fh.read()

setup(
    #name="sortmyfolder",
    version=VERSION,
    description=DESCRIPTION,
    #package_dir={'':'auto_group'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': "auto_group"},
    packages=find_packages('auto_group'),
    install_requires=install_requires,
    keywords=['python', 'automation', 'sorting'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'sortmyfolder=auto_group.determine_location:main',
        ],
    },
)
