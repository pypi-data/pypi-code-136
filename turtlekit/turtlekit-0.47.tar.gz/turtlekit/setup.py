from setuptools import setup, find_packages

VERSION = "0.47"
DESCRIPTION = "A module for easily drawing shapes in python."
setup(
    name= "turtlekit",
    author = 'Wyatt Garrioch',
    author_email = "w.garrioch456@gmail.com",
    version = VERSION,
    description = DESCRIPTION,
    long_description = open("turtlekit/README.md").read(),
    long_description_content_type="text/markdown",
    scripts=["turtlekit/turtlesuite.py", "turtlekit/__init__.py"],
    packages = find_packages(),
    install_requires = ["turtle"],
    keywords=["python", "Turtle"],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
    
)