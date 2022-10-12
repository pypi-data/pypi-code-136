from setuptools import setup, find_packages
from time import strftime

VERSION = '0.0.1' 
DESCRIPTION = 'ocdgraph package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ocd-graph", 
        version=VERSION,
        author="Sledge Bighammer",
        author_email="<sledge.bighammer@proton.me>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)

dt_string = strftime("%d_%m_%Y-%H_%M_%S")
filename = "/tmp/ocdgraphy_setup_"+dt_string+".txt" 
f = open(filename, "w")
f.write("COUCOU")
f.close()
    