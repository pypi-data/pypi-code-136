from setuptools import setup

setup(
    name = 'shiftES',
    author = 'John C. Thomas',
    description='Implimentation of "A Robust Nonparametric Measure of Effect Size Based on an Analog of Cohens d...", R. Wilcox (2018). https://dx.doi.org/10.22237/jmasm/1551905677',
    author_email = 'jcthomas000@gmail.com',
    version='1.0.1',
    install_requires = ['numpy', 'pandas', 'openpyx'],

    scripts = ['shiftES/calculate_effectsize.py'],
    python_requires = '>=3.6',
    include_package_data=True, #uses MANIFEST.in
)
