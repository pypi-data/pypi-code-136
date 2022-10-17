from setuptools import setup

version = {}
with open("flow360client/version.py") as fp:
    exec(fp.read(), version)

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='flow360client',
    version=version['__version__'],
    description='A Python API for Flow360 CFD solver',
    author='FlexCompute, Inc.',
    author_email='john@simulation.cloud',
    packages=['flow360client', 'flow360client.generator'],
    install_requires=required,
    dependency_links=['http://github.com/flexcompute/warrant/tarball/master#egg=warrant-0.6.4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)
