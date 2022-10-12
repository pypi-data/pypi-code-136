# This file is placed in the Public Domain.


"object programming"


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="objectprogramming",
    version="101",
    author="Bart Thate",
    author_email="operbot100@gmail.com",
    url="http://github.com/operbot/op",
    description="object programming",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    packages=["op", "opm"],
    scripts=["bin/op", "bin/opc", "bin/ops", "bin/opi"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
