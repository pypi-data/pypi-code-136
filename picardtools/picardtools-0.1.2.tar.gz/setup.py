import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='picardtools',
    version='0.1.2',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='python3 interface with Picard Tools from Broad institute',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/picardtools',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    entry_points={
        'console_scripts': ['picardtools-download=picardtools.download:main']
    }
)
