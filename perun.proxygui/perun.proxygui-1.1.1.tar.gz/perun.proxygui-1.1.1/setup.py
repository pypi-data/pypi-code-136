from setuptools import setup, find_packages

setup(
    name="perun.proxygui",
    python_requires=">=3.9",
    url="https://gitlab.ics.muni.cz/perun-proxy-aai/python/perun-proxygui.git",
    description="Module with gui for perun proxy",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "PyYAML~=6.0",
        "Flask~=2.2",
        "jwcrypto~=1.3",
        "Flask-Babel~=2.0",
    ],
)
