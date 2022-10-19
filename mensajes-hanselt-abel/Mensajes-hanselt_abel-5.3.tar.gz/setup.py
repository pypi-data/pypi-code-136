from setuptools import setup, find_packages

setup(
    name='Mensajes-hanselt_abel',
    version='5.3',
    description='Un paquete para saludar y despedir',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hanselt Baca',
    author_email='hanselt_a14@hotmail.com',
    url='https://twitter.com/hanselt_abel',
    license_files=['LICENSE'],
    packages=find_packages(),    
    scripts=[],
    install_requires=[paquete.strip()   for paquete in open("requirements.txt").readlines()],
    test_suite='tests',
    classifiers=[
        #Categorias
        'Environment :: Console',
        'Topic :: Artistic Software',
        'License :: Free For Educational Use',
        'Programming Language :: Python :: 3'
    ]
)
