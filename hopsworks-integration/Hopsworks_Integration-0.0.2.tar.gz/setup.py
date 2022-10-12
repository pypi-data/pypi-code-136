import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hopsworks_Integration",
    version="0.0.2",
    author="Syed Muneeb Hussain",
    author_email="muneebhussain94@gmail.com",
    description="A python package that exposes functions to interact with the Hopsworks feature store",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muneebsmh/hopsworks-integrations.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7,<3.10',
    install_requires=[
        'hopsworks==3.0.3',
        'pandas',
        'SQLAlchemy',
        'pytest'
    ]
)