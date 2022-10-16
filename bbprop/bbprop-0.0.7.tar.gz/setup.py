import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bbprop',
    version='0.0.7',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='Hypothesis test for difference of beta-binomial proportions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/bbprop',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['bbpmf', 'scipy']
)
