import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = "hive-nektar",
    packages = ["nektar"],
    version = "0.9.26",
    license="MIT",
    description = "Nektar, Hive API SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = "Rodney Maniego Jr.",
    author_email = "rodney.maniegojr@gmail.com",
    url = "https://github.com/rmaniego/nektar",
    download_url = "https://github.com/rmaniego/nektar/archive/v1.0.tar.gz",
    keywords = ["nektar", "hive", "blockchain", "api", "sdk"],
    install_requires=["ecdsa", "requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers", 
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.9"
)