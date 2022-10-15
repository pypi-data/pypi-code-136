import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uscovid",
    version="0.0.7",
    author="junya toyokura",
    author_email="j.toyokura@agreement.jp",
    description="covid19 in US states",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Junya-Toyokura/uscovid",
    project_urls={
        "Bug Tracker": "https://github.com/Junya-Toyokura/uscovid",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['uscovid'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'uscovid = uscovid:main'
        ]
    },
)
