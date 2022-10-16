from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'The utilities for spatialWeb web server'
LONG_DESCRIPTION = 'The utilities for spatialWeb web server'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="spatialWeb", 
        version=VERSION,
        author="Kevin Lee",
        author_email="2101112223@pku.edu.cn",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['spatial transcriptome', 'web server'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
        ]
)
