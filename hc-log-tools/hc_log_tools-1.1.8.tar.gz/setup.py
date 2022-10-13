from setuptools import setup, find_packages
import os

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

# get requirements from requirements.txt
install_reqs = parse_requirements("requirements.txt", session=False)
requirements = list(install_reqs)


try:
    requirements = [str(ir.req) for ir in requirements]
except:
    requirements = [str(ir.requirement) for ir in requirements]

# print(f"++++++++++++++++++++++++++++requirements: {requirements}")


setup(
    packages=find_packages(),
    install_requires = requirements,
    entry_points={
        'console_scripts': [
            'hc_log_tools = src.entry:entry',
        ]
    },
)