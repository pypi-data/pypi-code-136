import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='text_to_list',
    author='Sezer BOZKIR',
    version="0.0.1",
    author_email='admin@sezerbozkir.com',
    description='Example PyPI (Python Package Index) Package',
    keywords='example, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/natgho/text_to_list',
    project_urls={
        'Documentation': 'https://github.com/natgho/text_to_list',
        'Bug Reports':
        'https://github.com/natgho/text_to_list/issues',
        'Source Code': 'https://github.com/natgho/text_to_list',
    },
    package_dir={'': 'text_to_list'},
    packages=setuptools.find_packages(where='text_to_list'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
)