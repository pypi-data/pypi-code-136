from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="funpdbe-validator",
    version="1.1.2",
    description="Validate PDBe-KB JSONs by FunPDBe Schema",
    long_description_content_type='text/markdown',
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="json funpdbe_validator",
    url="https://github.com/PDBe-KB/funpdbe-validator",
    author="Mihaly Varadi",
    author_email="mvaradi@ebi.ac.uk",
    license_file="LICENSE",
    packages=["funpdbe_validator"],
    install_requires=["jsonschema", "requests", "gemmi"],
    test_suite="tests",
    tests_require=["pytest", "pytest-cov"],
    include_package_data=True,
    zip_safe=True,
    python_requires='>=3.6',
)
