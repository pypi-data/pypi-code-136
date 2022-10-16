import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='betabernsum',
    version='0.1.3',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='Sums of beta-bernoulli random variables',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/betabernsum',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['accelasc', 'scipy']
)
