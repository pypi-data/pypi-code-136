import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="okcolor",
    version="1.0.0",
    author="Parth Parikh",
    author_email="parthparikh1999p@gmail.com",
    description="Generates aesthetically pleasing RGB colors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pncnmnp/okcolor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
                'Pillow'
                 ],
    python_requires='>=3.6',
    include_package_data=True,
)