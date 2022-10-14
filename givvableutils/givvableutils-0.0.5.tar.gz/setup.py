from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='givvableutils',
    version='0.0.5',    
    description='utility tools for givvable',
    py_modules=['db', 'blob'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://dev.azure.com/givvable/givvable%20data/_git/givvableutils',
    author='Jatin Wadhwa',
    author_email='jatin@givvable.com',
    license='MIT',
    # packages=['db'],
    install_requires=[
        'psycopg2-binary >= 2.9.3',
        'azure-storage-file-datalake >= 12.8.0',
        'azure-core >= 1.24.0'
    ],
    extras_require={
        "dev": [
            "pytest >= 3.7",
            "twine >= 3.4.2"
        ],
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        # 'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',        
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)