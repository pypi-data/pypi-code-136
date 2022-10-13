import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'numpy==1.19.5',
    'pandas==1.1.5',
    'plotly==5.4.0'
]

setuptools.setup(
    name="vivplots",
    version="0.0.6",
    author="Thomas Meacham",
    author_email="thomas.meacham@vivent.ch",
    description="Common plotting modules for Vivent",
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vivent-sarl/vivplots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)