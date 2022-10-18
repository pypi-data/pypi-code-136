import setuptools

with open("./EAP/docs/Documentation.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "EAP", # package name
    version = "1.1.11", # version
    author = "whyecofiliter", # author name
    author_email = "why_ecofiliter@126.com",
    description = "This package is designed for empirical asset pricing", # description
    long_description = long_description, # documnetation
    long_description_content_type = "text/markdown", # documentation type
    url = "https://whyecofiliter.github.io/EAP/", # url in Github
    packages = setuptools.find_packages(), # automatic package searching
    # proto data
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # dependent package
    install_requires = [
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'statsmodels',
        'prettytable',
        'tensorflow',
        'pywavelets',
        'seaborn',
    ],
    python_requires = '>=3',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/whyecofiliter/EAP/issues",
        "Documentation": "https://whyecofiliter.github.io/EAP/Documentation.html",
        "Source Code": "https://github.com/whyecofiliter/EAP",
    },
)