try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name='art_to_ascii',
    version="1.0.0",
    license='MIT', 
    classifiers=classifiers,
    description="turn image to ascii art",
    author="Noam Avned",
    packages=[
        'arttoascii',
    ],
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
)
