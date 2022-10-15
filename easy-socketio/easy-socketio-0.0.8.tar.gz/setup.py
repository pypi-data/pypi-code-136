from setuptools import setup, find_packages


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()


def read_file(file):
    with open(file) as f:
        return f.read()


requirements = read_requirements("requirements.txt")

setup(
    name='easy-socketio',
    version='0.0.8',
    author='Tarik Gün (tarik56)',
    url='https://github.com/tarik56/easy-socketio',
    description='A simple wrapper around python-socketio that handles a simple que and threading.',
    long_description_content_type="text/markdown",
    long_description="socketio.start_server()\nsocketio.send('Hello clients')\n\nSee Github Readme for a more and detailed guide.",
    license="MIT license",
    packages=['easy_socketio'],
    package_dir={'': 'src'},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
