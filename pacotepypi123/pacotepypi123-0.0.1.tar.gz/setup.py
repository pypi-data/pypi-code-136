from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pacotepypi123',
    version='0.0.1',
    url='https://github.com/aAmoraP?tab=repositories',
    license='MIT License',
    author='Amora Sofia da Paixão',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='amorapaixaodev@gmail.com',
    keywords='Pacote',
    description='Pacote python para exibir número de 1 a 9',
    packages=['pacotepypi123'],
    install_requires=['numpy'],)