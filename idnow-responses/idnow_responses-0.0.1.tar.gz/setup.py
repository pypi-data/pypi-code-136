import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="idnow_responses",
    version="0.0.1",
    author="Martin Thoma",
    author_email="info@martin-thoma.de",
    maintainer="Martin Thoma",
    maintainer_email="info@martin-thoma.de",
    license="Unlicense",
    url="https://github.com/MartinThoma/responses-idnow",
    description=(
        "A third-party pytest plugin that provides a fixture to mock "
        "the IdNow identification service"
    ),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=["idnow_responses"],
    py_modules=["idnow_responses"],
    python_requires=">=3.8",
    install_requires=["pytest", "responses"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: Public Domain",
    ],
    entry_points={
        "pytest11": [
            "idnow_responses = idnow_responses",
        ],
    },
)
