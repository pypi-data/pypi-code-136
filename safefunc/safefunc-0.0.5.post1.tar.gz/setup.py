from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = "safefunc",
    version = "0.0.5.post1",
    license = "MIT",
    description = "Make sudden erros not stop your program",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "phoenixR",
    py_modules = ["safefunc"],
    package_dir = {"": "src"},
    classifiers = [
        "Development Status :: 7 - Inactive"
    ]
)