from setuptools import setup, find_packages

requires = [
    "requests",
    "jsonschema",
    "dimod",
    "dwave-networkx",
    "numpy",
]

setup(
    name='beit-qubo-solver',
    version='0.1.1',
    author="BEIT",
    author_email="qubo-solver@beit.tech",
    description='Client package for the exact qubo solver by BEIT available at Amazon Marketplace.',
    packages=["beit", "beit.qubo_solver", "beit.qubo_solver.schemas"],
    python_requires=">=3.7",
    install_requires=requires,
    package_data={'beit': ['qubo_solver/schemas/*.json']},
    include_package_data=True,
)

