from setuptools import setup, find_packages

setup(
    name='md5any',
    version="0.11",
    author="bing",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'md5any = src.__main__:main'
        ]
    }
)
