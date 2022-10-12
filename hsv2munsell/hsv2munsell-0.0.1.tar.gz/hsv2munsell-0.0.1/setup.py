from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Utility to convert HSV to Munsell scale'
LONG_DESCRIPTION = 'Utility to convert HSV to Munsell scale'

# Setting up
setup(
        name="hsv2munsell", 
        version=VERSION,
        author="Sumit Badal",
        author_email="<sbadal01@yahoo.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'munsell'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
