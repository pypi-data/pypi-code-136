
from setuptools import setup

setup(name='dynamic_rename',
        version='0.0.3',
        description='Column rename  in pyspark dataframe',
        packages=['dynamic_rename'],
        author_email='ranjitmaity95@gmail.com',
        zip_safe=False,
        long_description_content_type="text/markdown",
        long_description=open('README.md').read(),
        )