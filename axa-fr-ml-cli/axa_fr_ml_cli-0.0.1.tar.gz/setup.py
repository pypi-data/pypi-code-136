import setuptools

# sys.argv[1] to run test suite : test and to build wheel file is : bdist_wheel

#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()
#
#with open('requirements-nutella.txt') as f:
#    requirements.extend(f.read().splitlines())

setuptools.setup(
    name='axa_fr_ml_cli',
    version='0.0.1',
    # always get packages this way because it will find it recursively but exclude all test dir and it's subdir
    packages=setuptools.find_packages(exclude=["tests", "tests.*"], where='src'),
    package_dir={'': 'src'},
   # install_requires=requirements,
   # package_data={'': ['cni_zoning_model/*']},
    # metadata for pyPi
    author="Axa_france",
    author_email="",
    url='',
    description="this is the repo for CNI for batch and api",
    long_description="this is the repo for CNI for batch and api",
    platforms='POSIX',
    classifiers=["Programming Language :: Python :: 3 :: Only",
                 "Programming Language :: Python :: 3.8",
                 "Topic :: Scientific/Engineering :: Information Analysis",
                 ]
)
