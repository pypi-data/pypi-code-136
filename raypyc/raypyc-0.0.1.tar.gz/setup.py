from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A python wrapper for raylib'
LONG_DESCRIPTION = 'A python wrapper for raylib using ctypes'

# Setting up
setup(
    name="raypyc",
    version=VERSION,
    author="Dor Shapira",
    author_email="<sdor2803@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['inflection'],
    keywords=['python', 'raylib', 'simple', 'easy-to-use', 'video games', 'graphic library'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)