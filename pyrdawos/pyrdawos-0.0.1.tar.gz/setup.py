from setuptools import setup, find_packages

setup(
    name='pyrdawos',
    version='0.0.1',
    description='Python RDA AWOS',
    author='YangHyeonJi',
    author_email='yanghj@epilab.kr',
    url='https://gitlab.com/yanghjep/pyrdawos',
    install_requires=[
        'geopandas',
        'python-dateutil',
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    keywords=['rda', 'aws'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
