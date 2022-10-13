from setuptools import setup, find_packages

def load_readme() -> str:
    with open('README.md','r') as readme:
        return readme.read()

setup(
    name='jbac',
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    version='0.0.1',
    packages=find_packages(include=['src','src.*']),
    package_data={
        '': list(
            '../requirements.txt'
        ),
        'src': list(
            "cfg/args.yaml"
        )
    },
    install_requires=['argsy>=1.0.3', 'requests', 'python-dotenv'],
    entry_points={
        'console_scripts': ['jbac=src.app:main']
    }
)


