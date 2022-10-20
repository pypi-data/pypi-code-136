from setuptools import setup, find_packages

setup(
    name='AT_CRM_Cleaning',
    version='0.0.1',
    license='MIT',
    author='Krishna Moorthy Babu',
    packages=find_packages('src'),
    package_dir={'':'src'},
    url='',
    keywords= 'at_crm_cleaning',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),

)