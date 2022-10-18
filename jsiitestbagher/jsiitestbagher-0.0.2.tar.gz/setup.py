import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "jsiitestbagher",
    "version": "0.0.2",
    "description": "jsiitestbagher",
    "license": "Apache-2.0",
    "url": "https://github.com/mbasadi/jsiitestbagher.git",
    "long_description_content_type": "text/markdown",
    "author": "mbasadi<asadi.mohammadbagher@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/mbasadi/jsiitestbagher.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "jsiitestbagher",
        "jsiitestbagher._jsii"
    ],
    "package_data": {
        "jsiitestbagher._jsii": [
            "jsiitestbagher@0.0.2.jsii.tgz"
        ],
        "jsiitestbagher": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "jsii>=1.69.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
