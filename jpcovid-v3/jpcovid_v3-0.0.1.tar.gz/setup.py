import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jpcovid_v3",
    version="0.0.1",
    author="toshiki miyagawa",
    author_email="s1922033@stu.musashino-u.ac.jp",
    description="A package for calculating time transition policy scores against COVID-19 in Japan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miyagawa-toshiki/jpcovid_v3",
    project_urls={
        "Bug Tracker": "https://github.com/miyagawa-toshiki/jpcovid_v3",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['jpcovid_v3'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'jpcovid_v3 = jpcovid_v3:main'
        ]
    },
)
