import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dssdk",
    version="0.0.1",
    author="zhangping",
    author_email="teleping@gmail.com",
    description="sdk for dataset system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" https://pypi.org/project/dssdk/",
    project_urls={
        "Bug Tracker": "https://pypi.org/project/dssdk/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=["numpy", "pandas", "requests"],
)
