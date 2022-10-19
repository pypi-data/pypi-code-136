#! /usr/bin/env python

''' Setup script for mellon
'''

import os
import subprocess
from distutils.cmd import Command
from distutils.command.build import build as _build

from setuptools import find_packages, setup
from setuptools.command.install_lib import install_lib as _install_lib
from setuptools.command.sdist import sdist as _sdist


class compile_translations(Command):
    description = 'compile message catalogs to MO files via django compilemessages'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os

        from django.core.management import call_command

        os.environ.pop('DJANGO_SETTINGS_MODULE', None)
        for path in ['mellon/']:
            if path.endswith('.py'):
                continue
            curdir = os.getcwd()
            os.chdir(os.path.realpath(path))
            call_command('compilemessages')
            os.chdir(curdir)


class build(_build):
    sub_commands = [('compile_translations', None)] + _build.sub_commands


class eo_sdist(_sdist):
    sub_commands = [('compile_translations', None)] + _build.sub_commands

    def run(self):
        print("creating VERSION file")
        if os.path.exists('VERSION'):
            os.remove('VERSION')
        version = get_version()
        version_file = open('VERSION', 'w')
        version_file.write(version)
        version_file.close()
        _sdist.run(self)
        print("removing VERSION file")
        if os.path.exists('VERSION'):
            os.remove('VERSION')


class install_lib(_install_lib):
    def run(self):
        self.run_command('compile_translations')
        _install_lib.run(self)


def get_version():
    """Use the VERSION, if absent generates a version with git describe, if not
    tag exists, take 0.0- and add the length of the commit log.
    """
    if os.path.exists('VERSION'):
        with open('VERSION') as v:
            return v.read()
    if os.path.exists('.git'):
        p = subprocess.Popen(
            ['git', 'describe', '--dirty=.dirty', '--match=v*'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        result = p.communicate()[0]
        if p.returncode == 0:
            result = result.decode('ascii').strip()[1:]  # strip spaces/newlines and initial v
            if '-' in result:  # not a tagged version
                real_number, commit_count, commit_hash = result.split('-', 2)
                version = '%s.post%s+%s' % (real_number, commit_count, commit_hash)
            else:
                version = result
            return version
        else:
            return '0.0.post%s' % len(subprocess.check_output(['git', 'rev-list', 'HEAD']).splitlines())
    return '0.0'


setup(
    name="django-mellon",
    version=get_version(),
    license="AGPLv3 or later",
    description="SAML 2.0 authentication for Django",
    long_description=open('README').read(),
    url="http://dev.entrouvert.org/projects/django-mellon/",
    author="Entr'ouvert",
    author_email="info@entrouvert.org",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'django>=2.2,<3.3',
        'requests',
        'isodate',
        'atomicwrites',
    ],
    setup_requires=[
        'django>=1.10,<3.3',
    ],
    tests_require=[
        'nose>=0.11.4',
    ],
    dependency_links=[],
    cmdclass={
        'build': build,
        'install_lib': install_lib,
        'compile_translations': compile_translations,
        'sdist': eo_sdist,
    },
)
