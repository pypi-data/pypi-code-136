import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "lllfahaider-test-cdk-construct-01",
    "version": "0.0.1",
    "description": "test",
    "license": "Apache-2.0",
    "url": "https://github.com/DarthHaider/darthhaider_cdk_projen_test.git",
    "long_description_content_type": "text/markdown",
    "author": "Faraz Haider<fhaider2@gmu.edu>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/DarthHaider/darthhaider_cdk_projen_test.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "lllfahaider-test_cdk_construc-01",
        "lllfahaider-test_cdk_construc-01._jsii"
    ],
    "package_data": {
        "lllfahaider-test_cdk_construc-01._jsii": [
            "test@0.0.1.jsii.tgz"
        ],
        "lllfahaider-test_cdk_construc-01": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.45.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
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
