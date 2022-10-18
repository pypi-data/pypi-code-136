from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='servo_serial',
    version='0.0.2',
    packages=['servo_serial'],
    url='https://github.com/Adam-Software/Servo-serial',
    license='MIT',
    author='vertigra',
    author_email='a@nesterof.com',
    description='Common class for connect to servo',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=['feetech-servo-sdk'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Other',
        'Programming Language :: Python :: 3'
    ]
)
