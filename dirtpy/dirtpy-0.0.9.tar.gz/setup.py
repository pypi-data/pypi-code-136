from setuptools import setup, find_packages

VERSION = '0.0.9'
DESCRIPTION = 'An Entity Component System for your instancing needs'
LONG_DESCRIPTION = 'An ECS designed for entity instancing with serialization to/from JSON utilizing pydantic. A System update structure built arounds tickrates and priority'

setup(
    name='dirtpy',
    version=VERSION,
    author='Auraven',
    author_email='grandbossanvoa@gmail.com',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pydantic'],
    keywords=['python','pygame','ecs','instance','json','entity','component','system','game'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows'
    ]
)