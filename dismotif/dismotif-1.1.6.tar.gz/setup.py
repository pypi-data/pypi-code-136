import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dismotif',
    version='1.1.6',
    author='Anthony Aylward, Joshua Chiou',
    author_email='aaylward@salk.edu',
    description='disrupted motifs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/dismotif',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['pybedtools','pyhg19'],
    entry_points={'console_scripts': ['dismotif=dismotif.check_motifs:main',]},
    include_package_data=True
)
