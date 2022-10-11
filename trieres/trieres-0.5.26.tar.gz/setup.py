#  *
#  *                       cloudFPGA
#  *     Copyright IBM Research, All Rights Reserved
#  *    =============================================
#  *     Created: Feb. 2021
#  *     Authors: DID
#  *
#  *     Description:
#  *      A setup file used for buidling a PyPi package.
#  *
#  *    License:
#  *     Apache Version 2.0

import os
import shutil
import glob
import subprocess
try:
    from setuptools import setup, Extension, Command, find_packages
    from setuptools.command.build_py import build_py as build_py
    from setuptools.command.build_ext import build_ext as build_ext
except:
    from distutils import setup, Extension, Command
    from distutils.command.build_py import build_py as build_py  
    from distutils.command.build_ext import build_ext as build_ext

# Module name (must be the same than the one in .i file)
module_name = "trieres"

# Add C++ body source files and the unique SWIG interface file in extensions list (see build_ext command)
#cpps = glob.glob(os.path.join('cFp_Zoo/HOST/custom/uppercase/languages/cplusplus/src/','*.cpp', 'cFp_Zoo/HOST/PracticalSockets/src/PracticalSockets.cpp'))
#module_int = os.path.join('cFp_Zoo/HOST/custom/uppercase/languages/python/', module_name + '.i')
#module_ext = Extension('_' + module_name,
#                       sources = cpps + [module_int], # Keep SWIG interface file in last position
#                       swig_opts = ['-c++'], # https://lists.debian.org/debian-user/2008/03/msg01744.html
#                      )

class MyBuildExt(build_ext):
    """ Override build_ext command so that some customized commands are executed:
        1- Python wrapper interface generation (swig)
    """ 
    def run(self):
        return super().run() # Run swig thanks to extensions list above


# https://github.com/pypa/setuptools/issues/1347#issuecomment-387802255
class MyClean(Command):
    description = "Custom clean command to really remove all undesirable stuff"
    user_options = []
    
    to_be_cleaned = ['./dist',
                     './build',
                     './setup.cfg',
                     './src/*.egg-info',
                     './src/__pycache__',
                     './src/' + module_name + '.py',
                     './src/' + module_name + '_wrap.*',
                     './src/*.so',
                     './doxygen/html',
                     './doxygen/xml',
                     './src/documentation.i']

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Get directory containing setup.py
        root_dir = os.path.abspath(os.path.dirname(__file__))

        # Parse all stuff to be cleaned and deleted
        for path_pattern in self.to_be_cleaned:
            # Make paths absolute
            abs_paths = glob.glob(os.path.join(root_dir, path_pattern))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(root_dir):
                    # Die if path in to_be_cleaned is outside root directory
                    raise ValueError("%s is not a path inside %s" % (path, root_dir))
                print('Removing %s' % os.path.relpath(path))
                if (os.path.isfile(path)):
                    os.remove(path)     # remove one file
                else:
                    shutil.rmtree(path) # rmtree does not know how to remove files

# https://stackoverflow.com/questions/29477298/setup-py-run-build-ext-before-anything-else
class MyBuildPy(build_py):
    """ Override build_py command so that build_ext command is executed before building the package.""" 
    def run(self):
        self.run_command("build_ext")
        return super().run() # Really run build_py

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


version_path = os.path.dirname(os.path.abspath(__file__))+"/trieres/version.txt"
with open(version_path,"r") as fh:
    for line in fh:
        __version__ = line.rstrip("\n")
fh.close()

setup(
    name="trieres", 
    version=__version__,    
    author="Dionysios Diamantopoulos",
    author_email="did@zurich.ibm.com",
    description="A cloud-native python library for domain-specific cloud FPGAs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudFPGA/trieres",
    # this package contains one module,
    # which resides in the subdirectory mymodule
    #packages=find_packages(),
    packages=find_packages(include=['trieres','trieres/cFp_Zoo/HOST/vision/vision.py','trieres/cFp_Zoo/HOST/custom/custom.py']),

    setup_requires=['wheel'],

    # make sure the shared library is included
    #package_data={'trieres': ['_trieres.so', 'cFp_Zoo/HOST/vision/']},
    package_data={'trieres': ['trieres/cFp_Zoo/HOST/vision/vision.py', 'trieres/cFp_Zoo/HOST/custom/custom.py']},
    
    include_package_data=True,
    
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    #ext_modules=[module_ext],
    #py_modules=[module_name],
    #package_dir={"": "cFp_Zoo/HOST/"},    
    python_requires='>=3.7',
)

fh.close()

