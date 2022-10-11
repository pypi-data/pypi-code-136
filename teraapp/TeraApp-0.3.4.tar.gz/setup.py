from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='TeraApp',
    version='0.3.4',
    description='A very simple app creator',
    long_description=open('README.txt').read(),
    url='',
    author='oren',
    author_email='orennadle@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='appcreator computerapps exe app apps creator maker appmaker makerapp makerapps creatorapps appscreator',
    packages=find_packages(),
    install_requires=['PyQt5','requests','pyqtwebengine']
)