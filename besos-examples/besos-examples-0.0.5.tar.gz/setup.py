from setuptools import setup, find_packages
setup(
    name="besos-examples",
    version="0.0.5",
    description="A collection of examples for the besos python package",
    long_description="A collection of examples for the besos python package",
    long_description_content_type="text/markdown",
    author="Ralph Evins",
    author_email="besos@uvic.ca",
    url="https://gitlab.com/energyincities/besos",
    packages=["besos"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)
