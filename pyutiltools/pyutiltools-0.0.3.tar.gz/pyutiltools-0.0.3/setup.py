from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyutiltools',
    version='0.0.3',
    description='A package for general utilities.',
    author= 'Ateendra Jha',
    author_email="ateendrajha@live.com",
    url = 'https://www.drateendrajha.com/projects/pyutiltools',
    long_description_content_type="text/markdown",
    long_description = long_description,
    packages=setuptools.find_packages(),
    keywords=['mouse', 'random_mouse', 'random_cursor'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['pydlmodels'],
    package_dir={'':'src'},
    install_requires = [
        'keyboard',
        'pyautogui',
        'datetime'
    ]
)