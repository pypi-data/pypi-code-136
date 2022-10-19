from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="klcreqs",
        version="2022.10.19",
        description="library for streamlining api requests",
        readme="README.md",
        author='Thomas Nemechek',
        author_email='tnemechek@klcapital.com',
        classifiers=["Programming Language :: Python"],
        packages=['reqs'],
        include_package_data=True,
        install_requires=['mysql_connector_repackaged>=0.3.1',
        'numpy>=1.20.3',
        'pandas>=1.4.3',
        'requests>=2.26.0']
        )