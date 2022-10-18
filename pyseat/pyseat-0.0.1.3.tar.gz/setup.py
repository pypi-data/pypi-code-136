
import setuptools
from pyseat.version import __version__

# with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="pyseat",
    version=__version__,
    author="Lingxi Chen",
    author_email="chanlingxi@gmail.com",
    description="Structure Entropy hierArchy deTection (SEAT) for clustering, ordering, and embedding",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/deepomicslab/seat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'cycler>=0.11.0',
        'fonttools>=4.37.1',
        'joblib>=1.1.0',
        'kiwisolver>=1.4.4',
        'kmeans1d>=0.3.1',
        'matplotlib>=3.5.3',
        'networkx>=2.8.6',
        'numpy>=1.23.3',
        'packaging>=21.3',
        'pandas>=1.4.4',
        'Pillow>=9.2.0',
        'pyparsing>=3.0.9',
        'python-dateutil>=2.8.2',
        'pytz>=2022.2.1',
        'scikit-learn>=1.1.2',
        'scipy>=1.9.1',
        'seaborn>=0.12.0',
        'six>=1.16.0',
        'sklearn>=0.0',
        'threadpoolctl>=3.1.0',
        'torch>=1.12.1',
        'typing_extensions>=4.3.0'
    ]
)
