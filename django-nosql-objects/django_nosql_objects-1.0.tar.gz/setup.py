import os
import sys

from setuptools import find_packages, setup

__version__ = "1.0"

f = open("README.md")
readme = f.read()
f.close()

if sys.argv[-1] == "publish":
    #if os.system("pip freeze | grep wheel"):
    #    print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
    #    sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (__version__, __version__))
    print("  git push --tags")
    sys.exit()

setup(
    name="django_nosql_objects",
    version=__version__,
    description=(
        "Django_nosql_objects is an app for allowing users store JSON documents"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Osvaldo Molina",
    author_email="osvaldo.molina.128@gmail.com",
    url="https://github.com/osval-do/django-nosql-storage/tree/main",
    packages=find_packages(exclude=["tests*"]),
    project_urls={
        "Documentation": "https://github.com/osval-do/django-nosql-storage",
        "Changelog": "https://github.com/osval-do/django-nosql-storage/blob/main/CHANGES.rst",
        "Bug Tracker": "https://github.com/osval-do/django-nosql-storage/issues",
        "Source Code": "https://github.com/osval-do/django-nosql-storage",
    },
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "Django>=3.2",
        "djangorestframework",
        "django-filter",
        "django-guardian",
        "djangorestframework-guardian",
    ],
)