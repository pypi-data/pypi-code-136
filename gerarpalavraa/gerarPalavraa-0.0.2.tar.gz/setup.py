from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='gerarPalavraa',
    version='0.0.2',
    url='',
    license='MIT License',
    author='Pedro Benitah Vieira Sanchez de Melo',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='pedrobenitah@gmail.com',
    keywords='Pacote',
    description='Pacote python para gerar, armazenar e exibir palavras dissilabas',
    packages=['gerador', 'base', 'Main'],
    install_requires=[''],)