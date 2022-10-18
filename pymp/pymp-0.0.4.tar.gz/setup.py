import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymp",
    version="0.0.4",
    author="Michael J Tallhamer MSc DABR",
    author_email="mike.tallhamer@pm.me",
    description="A small package of medical physics toys",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tallhamer/pymp",
    packages=setuptools.find_packages(),
    package_data={'pymp': ['test/*.py', 'resource/*']},
    install_requires=[
        "numpy >= 1.16.3",
        "scipy >= 1.3.0",
        "pandas >= 0.25.0",
        "numba >= 0.48.0",
        "param >= 1.12.0",
        "panel >= 0.13.1",
        "pytest"
     ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
