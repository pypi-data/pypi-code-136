from setuptools import setup, find_packages


__version__ = "0.8.0"

setup(
    name="aicns-univariate-analyzer",
    version=__version__,
    description="Univariate time series analyzer library package in AICNS project",
    author="Youngmin An",
    author_email="youngmin.develop@gmail.com",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=[
        "pandas==1.1.5",
        "plotly==5.10.0",
        "pyspark==3.0.3",
        "scikit-learn==0.24.2",
        "statsmodels==0.13.2"
    ],
)
