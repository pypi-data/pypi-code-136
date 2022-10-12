#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Copyright (C) 2022 Authors
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.
#
# Authors:
#   Bryce Harrington <bryce@canonical.com>

"""A directive to run a DEP8 test against a source package"""

from functools import cached_property

from .constants import URL_AUTOPKGTEST


class Trigger:
    """
    A trigger indicates a source package that should be installed from a
    given series (generally to a specific version) when running
    autopkgtests for a Job.

    A Job can have multiple Triggers, each against a different source
    package and/or architectures, but all such Triggers must be against
    the same series as the Job itself.
    """
    def __init__(self, package, version, arch, series):
        """Initializes a new Trigger for a given package and version.

        :param str package: The source package name.
        :param str version: The version of the source package to install.
        :param str arch: The architecture for the trigger.
        :param str series: The distro release series codename.
        """
        self.package = package
        self.version = version
        self.arch = arch
        self.series = series

    def __repr__(self) -> str:
        """Machine-parsable unique representation of object.

        :rtype: str
        :returns: Official string representation of the object.
        """
        return (f'{self.__class__.__name__}('
                f'package={self.package!r}, version={self.version!r}, '
                f'arch={self.arch!r}, series={self.series!r})')

    def __str__(self) -> str:
        """Human-readable summary of the object.

        :rtype: str
        :returns: Printable summary of the object.
        """
        return f"{self.package}/{self.version}"

    @cached_property
    def autopkgtest_url(self) -> str:
        """Renders the trigger as a URL to the job history.

        :rtype: str
        :returns: tbd
        """
        if self.package.startswith('lib'):
            prefix = self.package[0:4]
        else:
            prefix = self.package[0]
        pkg_str = f"{prefix}/{self.package}"
        return f"{URL_AUTOPKGTEST}/packages/{pkg_str}/{self.series}/{self.arch}"


if __name__ == "__main__":
    print("### Trigger class smoke test ###")

    trigger = Trigger('my-package', '1.2.3', 'amd64', 'kinetic')
    print(trigger)
    print(trigger.autopkgtest_url)
