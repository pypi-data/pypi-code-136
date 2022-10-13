from setuptools import find_packages, setup


with open("README.rst") as f:
    description = f.read()


entry_points = {"pytest11": ["pytest_anything = pytest_anything"]}

setup_kwargs = {
    "name": "pytest-anything",
    "version": "0.1.3",
    "description": "Pytest fixtures to assert anything and something",
    "long_description": description,
    "long_description_content_type": "text/x-rst",
    "author": "Oliver Berger",
    "author_email": "diefans@gmail.com",
    "url": "https://gitlab.com/diefans/pytest-anything",
    "package_dir": {"": "src"},
    "packages": find_packages("src"),
    "py_modules": ["pytest_anything"],
    # "package_data": {"": ["*"]},
    "install_requires": ["pytest"],
    "extras_require": {"tests": ["pytest>=4.6,<5.0", "pytest-mock", "pdbpp"]},
    "entry_points": entry_points,
    "python_requires": ">=3.7,<4.0",
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Framework :: Pytest",
    ],
}

setup(**setup_kwargs)
