import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pydbsnp',
    version='2.0.2',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='Interface with dbSNP VCF data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/pydbsnp',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['pysam'],
    entry_points={
        'console_scripts': [
            'pydbsnp-download=pydbsnp.download:main',
            'pydbsnp-index=pydbsnp.index:main',
            'pydbsnp-query=pydbsnp.query:main'
        ]
    }
)
