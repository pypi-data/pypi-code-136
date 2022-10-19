from setuptools import find_packages, setup

setup(
    name = 'im2mesh',
    packages = find_packages(include=['im2mesh']),
    version = '0.1.2',
    description = 'Python library to create Finite Element meshes from segmented image stacks',
    long_description = 'For further information please visit the GitHub repository (https://github.com/cborau/im2mesh) or the documentation site (https://cborau.github.io/im2mesh/html/index.html)',
    author = 'Diego Sainz-DeMena & Carlos Borau-Zamora (UNIZAR)',
    author_email = "cborau@unizar.es",
    license = 'MIT',
    url = ' https://github.com/cborau/im2mesh ',
    install_requires = ['easygui==0.98.3','pymeshlab==2022.2.post2','gmsh==4.10.5',
     'open3d==0.15.1', 'nibabel==4.0.2', 'numpy==1.23.2', 'opencv-python==4.6.0.*',
     'pydicom==2.3.0', 'pydicom-seg==0.4.0', 'scikit-image==0.19.3', 'scipy==1.9.1'],
     classifiers=[
     'Programming Language :: Python :: 3.9']
)