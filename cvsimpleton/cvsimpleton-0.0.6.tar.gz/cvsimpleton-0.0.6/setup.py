import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()


long_description = 'bundled some frequently used base functions from openCV.'
setuptools.setup(
    name="cvsimpleton",
    version="0.0.6",
    author="JiayouQin",
    author_email="JiayouQinCN@gmail.com",
    description="Write less boilerplate code in OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JiayouQin/Python-projects/tree/master/CvSimpton",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "C:\\Users\\11110024\\Anaconda3\\Lib\\site-packages"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)