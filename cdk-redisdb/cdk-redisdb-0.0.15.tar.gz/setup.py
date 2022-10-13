import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-redisdb",
    "version": "0.0.15",
    "description": "Simple & featureful Redis on AWS - Elasticache Replication Group & MemoryDB with a unified API",
    "license": "Apache-2.0",
    "url": "https://github.com/forkfork/cdk-redisdb.git",
    "long_description_content_type": "text/markdown",
    "author": "Timothy Downs<timothydowns@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/forkfork/cdk-redisdb.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_redisdb",
        "cdk_redisdb._jsii"
    ],
    "package_data": {
        "cdk_redisdb._jsii": [
            "cdk-redisdb@0.0.15.jsii.tgz"
        ],
        "cdk_redisdb": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.8.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.68.0, <2.0.0",
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
