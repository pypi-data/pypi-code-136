from setuptools import setup

long_description = open('README.md').read()

setup(
    name='robodyno',
    version='0.2',
    maintainer='robottime',
    maintainer_email='lab@robottime.cn',
    author='song',
    author_email='zhaosongy@126.com',
    description='The Robodyno Robot SDK for Python 3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/robottime/Robodyno-Python-API',
    keywords=['robodyno', 'robot', 'robot module'],
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Framework :: Robot Framework',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=[
        'robodyno', 
        'robodyno.components', 
        'robodyno.interfaces', 
        'robodyno.interfaces.can_bus',
        'robodyno.interfaces.webots',
        'robodyno.robots',
        'robodyno.robots.six_dof_collaborative_robot',
        'robodyno.robots.utils',
    ],
    package_dir={'robodyno.robots': 'robodyno_robots'},
    python_requires='>=3.6',
    install_requires=['numpy>=1.10.0'],
    extras_require={
        ':sys_platform == "win32"': [
            'candle_driver'
        ],
        ':"linux" in sys_platform': [
            'python-can>=3.2.0, <4.0'
        ],
    },
)
