import setuptools

setuptools.setup(
    name='natalie',
    version='2.8',
    packages=setuptools.find_packages(),
    license='GPL-3.0',
    author='jack',
    author_email='kinginjack@gmail.com',
    description='an automation software made for my friend natalie',
    install_requires=['colorama', 'datetime', 'cryptography', 'termcolor', 'tinydb','PyQt5','requests','cloudscraper','bs4','pymongo[srv]'],
    python_requires='>=3.8'
)
