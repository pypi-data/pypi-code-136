from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Flashcards Study App'

# Setting up
setup(
    name="Flashcards Terminal App",
    version=VERSION,
    author="jasonl27 (Jason Layvand)",
    author_email="<jasonlayvand@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['os', 'getpass', 'csv', 'random'],
    keywords=['python', 'terminal', 'app', 'study'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)