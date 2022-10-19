from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["matplotlib>=3.1.1", "fire>=0.2.1"]

setup(
    name="PyplotAnnotation",
    python_requires='>=3.6',
    version="1.1.1",
    author="Aurélien COLIN",
    author_email="aureliencolin@hotmail.com",
    description="Quickly draw segmentation dataset",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Rignak/PyplotAnnotation",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
