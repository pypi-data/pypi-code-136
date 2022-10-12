# (c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, DSI, 2021.

import io

import setuptools

long_description = io.open("README.md", encoding="utf-8").read()
version = __import__("django_epflmail").__version__
source_url = "https://github.com/epfl-si/django-epfl-mail"

setuptools.setup(
    name="django-epfl-mail",
    version=version,
    url=source_url,
    author="William Belle",
    author_email="william.belle@gmail.com",
    description="A Django application with templates for emails.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    zip_safe=False,
    project_urls={
        "Changelog": source_url + "/blob/main/CHANGELOG.md",
        "Source": source_url,
        "Tracker": source_url + "/issues",
    },
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
