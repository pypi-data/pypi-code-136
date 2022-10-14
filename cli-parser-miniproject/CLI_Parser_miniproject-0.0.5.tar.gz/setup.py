import setuptools

setuptools.setup(
    include_package_data=True,
    name='CLI_Parser_miniproject',
    version='0.0.5',
    description='python module',
    packages=setuptools.find_packages(),
    install_requires=['tqdm==4.64.1'],
    long_description='Command-line utility that lets us filter textual input stream based on regular expression pattern and generate log in CSV or JSON format as output stream with support for adding plugins for different formats',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)
