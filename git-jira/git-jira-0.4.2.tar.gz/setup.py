import pathlib

from setuptools import find_packages, setup

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
    name="git-jira",
    description="A git addon to manage Jira from git",
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.4.2",
    license="MIT",
    author="rloredo",
    author_email="loredo.rod@gmail.com",
    url="https://github.com/rloredo/git-jira",
    keyword="git, jira",
    python_requires=">=3.6.2",
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        git-jira=git_jira.cli:cli
    """,
    install_requires=[
        "click==8.0",
        "jira==3.4",
        "PyYAML==6.0",
        "sh==1.14",
        "pick==2.0",
        "prettytable==3.4"
    ],
    extras_require={
        "dev": [
            "tox==3.26",
            "pytest==7.1",
            "mypy==0.981",
            "black==22.8",
            "pylint==2.15",
            "isort==5.10.1",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
