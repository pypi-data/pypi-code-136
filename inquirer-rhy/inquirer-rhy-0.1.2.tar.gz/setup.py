from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
VERSION = "0.1.2"

setup(
    name='inquirer-rhy',
    version=VERSION,
    description='inquirer in modern python3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='inquirer',
    author='RhythmLian',
    url="https://github.com/Rhythmicc/inquirer-rhy",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['prompt_toolkit>=3.0, <3.1.0', 'Pygments>=2.2.0'],
    entry_points={},
)
