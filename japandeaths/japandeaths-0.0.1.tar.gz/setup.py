import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="japandeaths",
    version="0.0.1",
    author="izuru inose",
    author_email="i.inose0304@gmail.com",
    description="Visualization of Japanese age and number of deaths in Covid-19.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/i-inose/jpdeaths",
    project_urls={
        "Bug Tracker": "https://github.com/i-inose/jpdeaths",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['japandeaths'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'japandeaths = japandeaths:main'
        ]
    },
)
