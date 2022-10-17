import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jpscore",
    version="0.0.7",
    author="yoshiyasu takefuji",
    author_email="takefuji@keio.jp",
    description="A package for scoring prefecture COVID-19 policies in Japan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytakefuji/covid_score_japan",
    project_urls={
        "Bug Tracker": "https://github.com/ytakefuji/covid_score_japan",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['jpscore'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'jpscore = jpscore:main'
        ]
    },
)
