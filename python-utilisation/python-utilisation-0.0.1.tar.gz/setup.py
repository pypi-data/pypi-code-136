import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-utilisation",
    version="0.0.1",
    author="Jen-Yves Badette",
    author_email="jeanyvesbadette@gmail.com",
    description="Useful tools Python Utilisation",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Djeevs-Jean/",
    keywords=["python-utilisation", "python-utils", "python", "utilisation"],
    install_requires=[""],

    packages=setuptools.find_packages(),

    license="MIT",

    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


