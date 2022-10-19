import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covidillness",
    version="0.0.1",
    author="Izuru Inose",
    author_email="i.inose0304@gmail.com",
    description="Graph of the number of deaths and serious injuries due to Covid-19 in Japan.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/i-inose/covidiil",
    project_urls={
        "Bug Tracker": "https://github.com/i-inose/covidill",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['covidillness'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'covidillness = covidillness:main'
        ]
    },
)
