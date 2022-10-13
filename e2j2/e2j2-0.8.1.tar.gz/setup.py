from setuptools import find_packages, setup

description = (
    "e2j2 is a commandline utility to render text/configuration files from jinja2 templates"
    + "from shell environment variables"
)

setup(
    name="e2j2",
    version="0.8.1",
    description=description,
    long_description=open("README.rst").read(),
    install_requires=[
        "jinja2>=2.10.1",
        "python-consul>=0.6.0",
        "deepmerge>=0.0.4",
        "dnspython",
        "jsonschema",
        "rfc3987",
        "munch",
        "dpath>=2.0.1",
        "termcolor>=1.1.0",
    ],
    tests_require=["mock", "unittest2", "requests-mock", "callee"],
    url="https://gitlab.com/solvinity/e2j2",
    author="Johan Bakker",
    author_email="johan.bakker@solvinity.com",
    license="MIT",
    package_data={"": ["LICENSE", "README.rst", "CHANGELOG.rst"]},
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    e2j2=e2j2.scripts.e2j2:cli
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Systems Administration",
        "Topic :: Software Development :: Libraries",
    ],

   test_suite="tests",
    zip_safe=True,
)
