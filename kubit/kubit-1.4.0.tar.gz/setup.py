import setuptools

kubit = 'kubit'

with open('VERSION') as f:
    kubit_version = f.read().strip()

with open('README') as f:
    kubit_readme = f.read().strip()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(name=kubit,
                 version=kubit_version,
                 description=kubit,
                 long_description=kubit_readme,
                 author='Kubit AI, Inc.',
                 author_email='info@kubit.co',
                 packages=[kubit],
                 install_requires=required,
                 license='MIT License',
                 zip_safe=False)
