from setuptools import find_packages, setup

setup(
    name='django_shopify_app',
    version='v0.0.3',
    author='Moship',
    author_email='hello@moship.io',
    packages=find_packages(),
    scripts=[],
    url='http://pypi.python.org/pypi/django_shopify_app/',
    license="MIT",
    description='A django app with all the tools required to make a Shopify app',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "Django >= 4.0.0",
        "pytest",
        "shopifyapi"
    ],
)
