from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='keras-cortex',
    version='0.0.3',
    description='Keras Implementations of Goal-driven models of (parts of) cortex',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/weidler/keras-cortex',
    author='Tonio Weidler',
    author_email='research@tonioweidler.de',
    license='Apache-2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tensorflow==2.10.0",
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
