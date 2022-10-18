import re

from setuptools import find_namespace_packages, setup

URL = 'https://github.com/annotell/annotell-python'

package_name = 'kognic-openlabel'

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

# resolve version by opening file. We cannot do import during install
# since the package does not yet exist
with open('kognic/openlabel/__init__.py', 'r') as fd:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE)
    version = match.group(1) if match else None

if not version:
    raise RuntimeError('Cannot find version information')

# https://packaging.python.org/guides/packaging-namespace-packages/
packages = find_namespace_packages(include=['kognic.*'])

setup(
    name=package_name,
    packages=packages,
    namespace_packages=["kognic"],
    version=version,
    description='Kognic OpenLABEL Datamodel',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Kognic',
    author_email='New Annotation <new-annotation@kognic.com>',
    license='MIT',
    url=URL,
    download_url='%s/tarball/%s' % (URL, version),
    keywords=['Kognic', "OpenLABEL"],
    python_requires='>=3.7',
    include_package_data=True,
    package_data={
        '': ['*.md', 'LICENSE', '*.json'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)
