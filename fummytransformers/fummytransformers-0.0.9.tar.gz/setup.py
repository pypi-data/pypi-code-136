from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='fummytransformers',
    version='0.0.9',
    description='Fast and dummy way of using transformers to establish quick baselines',
    long_description_content_type="text/markdown",
    long_description=README,
    include_package_data=True,
    license='Apache Licence 2.0',
    packages=find_packages(),
    author='Xiaoou WANG',
    author_email='xiaoouwangfrance@gmail.com',
    keywords=['text mining', 'npl', 'corpus',
              'french', 'bert', 'transformers'],
    url='https://github.com/xiaoouwang/fummytransformers',
    download_url='https://pypi.org/project/fummytransformers',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

install_requires = [
    'numpy',
    'pandas',
    'transformers',
    'torch',
    'py7zr',
    # 'sentence_transformers',
    'sklearn',
    'tensorflow'
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
