from setuptools import setup, find_packages

setup(
    name='PythConfig',
    version='v1.0',
    description='',
    url='https://github.com/transbee', 
    author='zedzee',
    author_email='',
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    ],
    keywords=['python', 'config', 'auto config'],
    packages=find_packages(),
        entry_points = {
        'console_scripts': ['pyconfig=pyconfig:main'],
    }
)