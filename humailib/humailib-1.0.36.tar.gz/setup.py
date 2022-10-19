from setuptools import setup
from setuptools import find_packages

REQUIRED_PACKAGES = [
    'pandas-gbq',
    'pathlib',
    'google-cloud-datastore','google-cloud-bigquery','google-cloud-storage','tqdm','google-cloud-bigquery-storage',
    'pyarrow',
    'pandas==1.0.0'
]

setup(
    name='humailib',
    version='1.0.36',
    description='HUMAI data science framework',
    url='',
    author='HUMAI Limited',
    author_email='willem@humai.nl',
    license='',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    zip_safe=False
)