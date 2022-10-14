import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythonagent", # Replace with your own username
    version="0.0.17",
    author="Cavisson System",
    author_email="pythonagent@cavisson.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    #package_data={'pythonagent': ['*.txt']},
    include_package_data=True,
    #python_requires='>=3.6',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',
)
