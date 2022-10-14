from setuptools import setup, find_packages

setup(
    name= "mensajes-kelvinnieves",
    version= "5.0",
    description= "un Paquete para saludar y despedir",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author= "Kenmaster",
    author_email="kenmaster@gmail.com",
    url= "https://kenmaster.cl",
    license_files=['LICENSE'],
    packages= find_packages(),
    scripts= [],
    test_suite='tests',
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',

    ]
)
