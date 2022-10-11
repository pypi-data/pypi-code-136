from setuptools import setup, find_namespace_packages

setup(
    name='cross_monitor_bot',
    version='0.1.0.dev1',
    description='Cross ping units and send notification to messager.',
    url='https://github.com/glowlex/cross_monitor_bot',
    author='glowlex',
    author_email='antonioavocado777@gmail.com',
    license='GPLv3',
    packages=find_namespace_packages(include=['cross_monitor_bot', 'cross_monitor_bot.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "croniter>=1.3.0,<2.0.0",  # 1.3.7
        "aiogram>=2.0.0,<3.0.0",  # 2.22.1
        "requests>=2.0.0,<3.0.0",  # 2.28.1
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 4 - Beta',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Utilities',
    ],
)
