from importlib_metadata import version
import setuptools

setuptools.setup(
    name='yashpyproject',
    version='0.0.4',
    author="Yashraj Baila",
    author_email="yashrajbaila@gmail.com",
    description="This package is for basic calculus and basic 2-D and 3-D mensuration",
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'sympy'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)