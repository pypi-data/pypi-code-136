from setuptools import setup

setup(
    name='codect',
    version='0.1.2',    
    description='Python package to protect your code',
    url='https://github.com/mategol/codect-python',
    author='Mateusz Golembowski',
    author_email='mateusz@golembowski.pl',
    license='MIT',
    packages=['codect'],
    install_requires=['pycryptodome',
                      'pybase64',
                      'hashlib',
                      'sys'                     
                      ],

    classifiers=[
        'License :: OSI Approved :: MIT License',      
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
)