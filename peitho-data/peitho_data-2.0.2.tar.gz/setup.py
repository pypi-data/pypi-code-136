from setuptools import setup

setup(
    name="peitho_data",
    version="2.0.2",
    description="An opinionated Python package on Big Data Analytics",
    url="https://github.com/QubitPi/peitho-data",
    author="Jiaqi liu",
    author_email="jack20191124@proton.me",
    license="Apache-2.0",
    packages=["peitho_data"],
    python_requires='>=3.10',
    install_requires=[
        "bs4",
        "wordcloud",
        "pycodestyle",
        "requests",
        "sphinx-rtd-theme",
        "matplotlib",
        "ebooklib"
    ],
    zip_safe=False,
    include_package_data=True
)
