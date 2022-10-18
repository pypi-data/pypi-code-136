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
    name='chefs_ttg',
    version="1.1.1",
    license='MIT', 
    classifiers=classifiers,
    description="create and save empty truth table",
    author="Noam Avned",
    packages=[
        'cttg',
    ],
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
)
