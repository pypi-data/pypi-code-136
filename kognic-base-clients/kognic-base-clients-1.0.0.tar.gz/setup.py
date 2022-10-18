from setuptools import setup, find_namespace_packages
import re

URL = 'https://github.com/annotell/annotell-python'

package_name = 'kognic-base-clients'

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

# resolve version by opening file. We cannot do import during install
# since the package does not yet exist
with open('kognic/base_clients/__init__.py', 'r') as fd:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE)
    version = match.group(1) if match else None

if not version:
    raise RuntimeError('Cannot find version information')

# https://packaging.python.org/guides/packaging-namespace-packages/
packages = find_namespace_packages(include=['kognic.*'])

release_status = "Development Status :: 5 - Production/Stable"

setup(
    name=package_name,
    packages=packages,
    namespace_packages=["kognic"],
    version=version,
    description='Kognic Base Clients',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Kognic',
    author_email='Scenes & Predictions <scenes-and-predictions@kognic.com>',
    license='MIT',
    url=URL,
    download_url='%s/tarball/%s' % (URL, version),
    keywords=['API', 'Kognic'],
    install_requires=[
        'kognic-auth>=3.0.0<4',
        'requests>=2.23.0',
        'pydantic',
        'pyhumps',
    ],
    python_requires='~=3.7',
    include_package_data=True,
    package_data={
        '': ['*.md', 'LICENSE'],
    },
    classifiers=[
        release_status,
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)
