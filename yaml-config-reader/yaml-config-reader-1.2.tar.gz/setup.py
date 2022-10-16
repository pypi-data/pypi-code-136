import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="yaml-config-reader",
    version="1.2",
    author="J4CK VVH173, Polosha",
    author_email="i78901234567890@gmail.com",
    description="Package for reading configs from yml files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/J4CKVVH173/yaml-config",
    packages=setuptools.find_packages(),
    install_requires=[
            'PyYAML==6.0.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.8',
)
