import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="wsy",
    version="1.0.0",
    author="Suluoya",
    author_email="1931960436@qq.com",
    maintainer='Suluoya',
    maintainer_email='1931960436@qq.com',
    description="A package for my girlfriend, wsy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Su-luoya",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas',
                      'numpy',
                      'scipy',
                      'statsmodels',
                      'tqdm',
                      'pretty_errors',
                      ]
)

