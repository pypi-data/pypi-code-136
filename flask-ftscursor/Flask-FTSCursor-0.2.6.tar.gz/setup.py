"""
Flask-FTSCursor
-------------

An extension to facilitate using FTSCursor with flask
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Flask-FTSCursor',
    version='0.2.6',
    url='https://gitlab.com/aaylward/flask-ftscursor',
    license='MIT',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='An extension to facilitate using FTSCursor with flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask', 'ftscursor'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
