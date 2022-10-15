#!python
VERSION = '0.0.1'

if __name__ == '__main__':
    import sys

    try: from setuptools import setup, find_packages
    except ImportError: from distutils.core import setup, find_packages

    SETUP_CONF = \
    dict (name = "keyblade",
          description = "Keyblade software.",
          download_url = "",

          license = "None",
          platforms = ['OS-independent', 'Many'],

          include_package_data = True,

          keywords = [],

          classifiers = [])


    SETUP_CONF['version'] = VERSION

    SETUP_CONF['author'] = ''
    SETUP_CONF['author_email'] = ''

    SETUP_CONF['long_description_content_type'] = 'text/plain'
    SETUP_CONF['long_description'] = ''

    SETUP_CONF['packages'] = []

    setup(**SETUP_CONF)
