#!/usr/bin/python

from setuptools import setup, Extension

Version = '1.0.3'

longDesk = '''
ENG:

ENS(text) -> encrypt text

DEC(text) -> decrypt the text

Encryption example:
    text = ENS('this is text')

    print(text)

Conclusion:
   le=g116S%$L2=0104S%$Ll=e105S%$l2=¿115S%$se=132S%$Lz=6105S%$ly=q115S%$Sx=132S%$Ls=@116S%$L%=h101S%$Lu=9120S%$Lm=%116

decryption example:
    text = DEC('le=g116S%$L2=0104S%$Ll=e105S%$l2=¿115S%$se=132S%$Lz=6105S%$ly=q115S%$Sx=132S%$Ls=@116S%$L%=h101S%$Lu=9120S%$Lm=%116')

    print(text)

Conclusion:
    this is text

'''

setup(
    name='encoderPy',
    version=Version,

    author='AlmazCode',
    author_email='diamondplay43@gmail.com',

    description='Simple encoder & text decryptor',
    long_description=longDesk,

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['encoderPy'],

    classifiers=['License :: OSI Approved :: Apache Software License',
                'Operating System :: OS Independent',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: Developers',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
                'Programming Language :: Python :: 3.10',
                'Programming Language :: Python :: Implementation :: PyPy',
                'Programming Language :: Python :: Implementation :: CPython'
                ]
)