from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Convert one file size type to another'
LONG_DESCRIPTION = 'Convert one file size type to another'

setup(
        name="convertsize",
        version=VERSION,
        author="Wolf Software",
        author_email="<pypi@wolfsoftware.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'convert_size'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
