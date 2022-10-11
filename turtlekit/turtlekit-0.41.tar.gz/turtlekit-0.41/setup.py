from setuptools import setup, find_packages

DESCRIPTION = "A module for easily drawing shapes in python."

setup(
    name="turtlekit",
    version = "0.41",
    author="Wyatt Garrioch",
    author_email= "w.garrioch456@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md", "r").read(),
    long_description_content_type = "text/markdown",
    packages=find_packages(),
    install_requires = "turtle",
    keywords=["Python", "Turtle"],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
)