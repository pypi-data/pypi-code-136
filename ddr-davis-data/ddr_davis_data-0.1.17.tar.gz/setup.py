from setuptools import setup, find_packages
import sys
import os 

module_name = 'ddr_davis_data'
gihub_url = r'https://github.com/ddrathod121294/' + module_name

p1 = os.path.join(r'src', module_name)
sys.path.insert(0, os.path.join(os.getcwd(),p1))

from version import version 

with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = ["numpy",
                "pandas",
                "matplotlib",
                "openpyxl",
                ]

setup_requirements = []

test_requirements = []

setup(
    name=module_name,
    version=version,
    packages=find_packages(where="src"),  # Required
    url=gihub_url,
    description="Package to handle davis data files", # Optional
    keywords='ddr,davis,davis_data,davis_data_manager,' + module_name, # Optional

    python_requires=">=3.10, <4",
    author="Darshan Rathod", # Optional
    author_email='darshan.rathod1994@gmail.com', # Optional
    classifiers=[ # Optional
        'Development Status :: 2 - Pre-Alpha',
        
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        
        'Natural Language :: English',

        "License :: OSI Approved :: MIT License",
        
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python :: 3.10'
    ],
    package_dir={"": "src"},  # Optional
    install_requires=requirements, # Optional 
    long_description=readme, # Optional
    long_description_content_type="text/markdown", # Optional 

    # setup_requires=setup_requirements,
    # test_suite='tests',
    # tests_require=test_requirements,
    # zip_safe=False,
    # include_package_data=True,
)


