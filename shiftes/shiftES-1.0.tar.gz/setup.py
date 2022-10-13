from setuptools import setup

setup(
    name = 'shiftES',
    author = 'John C. Thomas',
    author_email = 'jcthomas000@gmail.com',
    version='1.0',
    install_requires = ['numpy', 'pandas', 'openpyx'],

    scripts = ['shiftES/calculate_effectsize.py'],
    python_requires = '>=3.6',
    include_package_data=True, #uses MANIFEST.in
)
