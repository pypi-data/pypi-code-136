"""Python setup file to organise package setup."""


import os

from setuptools import find_packages, setup

setup(
    name="qub-amphibian-report-generator",
    version="0.0.34",
    description="Generate reports from amphibian info dataset",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    license="LICENSE",
    repository = "https://github.com/ccushnahan/report_generator",
    documentation="https://ccushnahan.github.io/report_generator/",
    author="Ciaran Cushnahan",
    packages=find_packages(
        exclude=[
            "report_generator.tests",
            "tests",
            "rg-venv",
            "__pycache__",
            "docs",
            "dist",
            ".tox",
            ".mypy_cache",
        ]
    ),
    install_requires=[
        "docopt<= 0.6.2",
        "PyQt5<=5.15.7",
        "pandas<=1.4.4",
        "openpyxl<=3.0.10",
        "loguru<=0.6.0",
        "PyPDF2<=2.10.4",
        "fpdf2<=2.5.5",
        "PyMuPDF<=1.20.2",
        "PyYAML<=6.0",
        "requests<=2.28.1",
        "tqdm<=4.64.1",
    ],
    entry_points={
        "console_scripts": [
            "report-generator = report_generator.app:main",
            "create-report-generator = report_generator.project_setup.new_report_project:main",
        ]
    },
)
