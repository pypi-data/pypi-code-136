from setuptools import setup


def README():
    with open("README.md", "rt", encoding="utf-8") as f:
        readme = f.read()
    return readme


setup(
    name="psindex",
    version="0.0.2",
    author="Luciana Trento Raineri",
    author_email="luciana.traineri@gmail.com",
    url="https://github.com/luraineri/psindex",
    project_urls={"Documentation": "https://luraineri.github.io/psindex/"},
    description=("Population Stability Index (PSI) implementation for python."),
    long_description=README(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=["psindex"],
    python_requires=">=3.7,<4.0",
    install_requires=[],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
