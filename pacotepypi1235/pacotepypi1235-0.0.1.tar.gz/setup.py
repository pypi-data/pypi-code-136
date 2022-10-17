from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pacotepypi1235',
    version='0.0.1',
    url='https://github.com/Fabreba/pypacotinho.git',
    license='MIT License',
    author='Fabricio José Sousa Silva',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='fabricioj49@gmail.com',
    keywords='Pacote',
    description='Pacote python para exibir número de 1 a 9',
    packages=['pacotepypi1235'],
    install_requires=['numpy'],)