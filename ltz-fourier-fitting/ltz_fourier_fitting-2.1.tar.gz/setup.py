from distutils.core import setup
import setuptools
packages = ['ltz_fourier_fitting']

setup(
    name='ltz_fourier_fitting',
    version='2.1',
    author='ltz',
    packages=packages,
    description= '#划分微元时不按照单位长度进行，傅里叶级数设置为精度的一半较好;若按照单位长度进行，傅里叶级数设置为len*精度的一般较好',
)