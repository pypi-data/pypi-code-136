from setuptools import setup

import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md") as readme_file:
    readme = readme_file.read()


test_deps = (["pytest", "coverage", "numpy_ringbuffer"],)
extra_deps = {"test": test_deps}

setup(
    author="Thomas Mohren",
    author_email="tlmohren@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Ringbuffer and downsampling buffer with numpy array backend",
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="numpy_array_buffer",
    packages=["numpy_array_buffer"],
    test_suite="tests",
    install_requires=["numpy"],
    tests_require=test_deps,
    extras_require=extra_deps,
    package_dir={"": "src"},
    url="https://github.com/maimonlab/numpy_array_buffer",
    version=get_version("src/numpy_array_buffer/__init__.py"),
    zip_safe=False,
)
