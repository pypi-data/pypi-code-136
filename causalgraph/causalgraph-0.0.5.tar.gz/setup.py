from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    # variable will be filled with the README content and used
    # as the long description of the package
    long_description = fh.read()

setup(
    name="causalgraph",
    #name='causalgraph-dev',
    version="0.0.5",
    author="Fraunhofer IWU",
    author_email="causalgraph@iwu.fraunhofer.de",
    description="A Python package made for the representation of Causal Graphs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=[
        "*tests*",
        '*pycache*'
    ]),
    package_data={
        #'causalgraph.learn': ['*','*/*','*/*/*'],
        'causalgraph.store': ['*','*/*','*/*/*'],
        'causalgraph.utils': ['*','*/*','*/*/*'],
        'data.logs': ['*','*/*','*/*/*'],
        'data': ['*','*/*','*/*/*'],
        'config': ['*','*/*','*/*/*']
    },
    include_package_data=True,
    exclude_package_data={'': ['*__pycache__*']},
    install_requires=[
        'owlready2==0.35',
        'networkx==2.6.3',
        'matplotlib==3.5.1',
        'ecs_logging==1.1.0',
        'numpy==1.22.1'
    ]
)