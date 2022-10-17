import os
import setuptools


base_dir = os.path.abspath(os.path.dirname(__file__))

# Readme
with open("README.md") as fp:
    readme = fp.read()

# About
version = {}
with open(
    os.path.join(base_dir, "cdk_resources", "__version__.py"), encoding="utf-8"
) as f:
    exec(f.read(), version)

print(version)


setuptools.setup(
    name=version["__name__"],
    version=version["__version__"],
    description=version["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=version["__author__"],
    packages=setuptools.find_packages(
        exclude=["tests*", "samples*", "mkdocs*"]
    ),
    # package_dir={"": "cdk_resources"},
    package_data={"": ["LICENSE"]},
    install_requires=["aws-cdk-lib>=2.43.1", "boto3==1.20.23"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: AWS CDK :: 1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
