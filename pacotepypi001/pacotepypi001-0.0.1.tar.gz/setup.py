from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pacotepypi001',
    version='0.0.1',
    url='https://github.com/marcos-de-sousa/pacotepypi',
    license='MIT License',
    author='João Vitor Cardoso Queiroz',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='jvcq15@outlook.com',
    keywords='Pacote',
    description='Pacote python para exibir número de 1 a 9',
    packages=['pacotepypi001'],
    install_requires=['numpy'],)