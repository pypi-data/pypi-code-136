import setuptools
from setuptools.extension import Extension
from Cython.Build import cythonize


with open("README.md", "r") as fh:
    long_description = fh.read()

extensions = [
    Extension(
        "pychronicles.chronicle",
        ["pychronicles/chronicle.py"],
        include_dirs=[], # not needed for fftw unless it is installed in an unusual place
        libraries=[],
        library_dirs=[], # not needed for fftw unless it is installed in an unusual place
    ),
]

setuptools.setup(
    name="pychronicles",
    version="0.0.9",
    author="Thomas Guyet",
    author_email="thomas.guyet@inria.fr",
    description="A package for chronicle recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.inria.fr/tguyet/pychronicles",
    install_requires=['pandas','numpy','scipy','lazr.restfulclient','lazr.uri','lark-parser'],
    packages=setuptools.find_packages(),
    ext_modules = cythonize(extensions),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
