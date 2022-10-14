# from setuptools import setup
from distutils.core import setup

# import versioneer

requirements = [
    # package requirements go here
]

setup(
    name="rdhyee_test",
    version="0.1.3",
    description="a test package ",
    license="MIT",
    author="Raymond Yee",
    author_email="ryee@iha.org",
    url=None,
    packages=["rdhyee_test"],
    py_modules=["rdhyee_test"],
    install_requires=requirements,
    keywords="rdhyee_test",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
