from setuptools import setup, find_packages
__version__ = "1.0.4"
setup(
    name='dl_common',
    version=__version__,
    license='MIT',
    author="Zaheer ud Din Faiz",
    author_email='zaheer@datalogz.io',
    packages=find_packages(exclude=["test*"]),
    install_requires=[
        'attrs>=19.0.0',
        'marshmallow>=3.0',
        'marshmallow3-annotations>=1.0.0',
        'Flask>=1.0.2',
    ]
)
