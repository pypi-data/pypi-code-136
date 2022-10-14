from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='makeit',
    version='2.10.8',  # year.month.version
    packages=['tests', 'makeit', 'makeit.contrib'],
    url='',
    license='Public Domain',
    author='Dmitrii Ushanov',
    author_email='ushanov.dmitry@gmail.com',
    description='Make util for applications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Utilities"
    ],
    python_requires=">=3.10",
    install_requires=[
        'loguru',
        'graphviz'
    ],
)
