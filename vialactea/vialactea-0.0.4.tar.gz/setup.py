from setuptools import setup
from pathlib import Path

this_dir = Path(__file__).parent

long_description = (this_dir / 'README.md').read_text()

setup(
    version='0.0.4',
    name='vialactea',
    packages=['vialactea'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)

