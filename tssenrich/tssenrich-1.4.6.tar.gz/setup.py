import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tssenrich',
    version='1.4.6',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='Calculate TSS enrichment for ATAC-seq data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/tssenrich',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['pybedtools'],
    entry_points={
        'console_scripts': ['tssenrich=tssenrich.tssenrich:main',]
    },
    include_package_data=True
)
