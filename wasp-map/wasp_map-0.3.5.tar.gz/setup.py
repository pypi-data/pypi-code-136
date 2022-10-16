import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wasp_map',
    version='0.3.5',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='Utilites for the mapping pipeline from WASP',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/wasp_map',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['gitpython', 'pyhg19', 'seqalign'],
    entry_points={
        'console_scripts': [
            'wasp_map-set-ldlib=wasp_map.ldlib:main',
            'wasp_map-download=wasp_map.download:main',
            'wasp_map-map=wasp_map.map:main'
        ]
    }
)
