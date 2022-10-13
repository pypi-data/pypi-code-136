from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="mongoengine-stubs",
    description="PEP 561 type stubs for mongoengine",
    version="0.24.0",
    packages=["mongoengine-stubs"],
    # PEP 561 requires these
    install_requires=[
        "mongoengine",
        'typing_extensions>=3.7.4; python_version<"3.8"',
    ],
    package_data=find_stubs("mongoengine-stubs"),
    zip_safe=False,
)
