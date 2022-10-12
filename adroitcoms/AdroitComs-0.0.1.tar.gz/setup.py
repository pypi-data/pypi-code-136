import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="AdroitComs",
    version="0.0.1",
    author="Cameron Devine",
    author_email="camdev@uw.edu",
    description="A package for communicating with HDT Adroit robots over CAN.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'python-can',
        'numpy',
    ]
)
