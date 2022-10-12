# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Author:  Bryce Harrington <bryce@canonical.com>
#
# Copyright (C) 2021 Bryce W. Harrington
#
# Released under GNU AGPL or later, read the file 'LICENSE.AGPL' for
# more information.

# Extraction of bileto's lp class, for general use in other places

"""Launchpad Interface

High level wrapper object for Launchpad's API
"""

from contextlib import suppress
from functools import lru_cache

from launchpadlib.launchpad import Launchpad


class Lp:
    """
    This class wrappers the Launchpadlib service to cache object queries
    and to provide functionalies frequently needed when writing software
    for managing the Ubuntu distribution.

    This can be used as a drop-in replacement in scripts that already
    use Launchpadlib.  Simply replace your Launchpadlib.login_with() call
    with an instantiation of this class.  Any call that Lp does not handle
    itself is passed directly to the Launchpadlib object, so the entire
    API is available in exactly the same way.
    """
    ROOT_URL = 'https://launchpad.net/'
    API_ROOT_URL = 'https://api.launchpad.net/devel/'
    BUGS_ROOT_URL = 'https://bugs.launchpad.net/'
    CODE_ROOT_URL = 'https://code.launchpad.net/'

    _real_instance = None

    def __init__(self, application_name, service=Launchpad):
        """Create a Launchpad service object."""
        self._app_name = application_name
        self._service = service

    def _get_instance(self):
        """Authenticate to Launchpad."""
        return self._service.login_with(
            application_name=self._app_name,
            service_root='production',
            allow_access_levels=['WRITE_PRIVATE'],
            version='devel',  # Need devel for copyPackage.
        )

    @property
    def _instance(self):
        """Cache LP object."""
        if not self._real_instance:
            self._real_instance = self._get_instance()
        return self._real_instance

    @property
    @lru_cache()
    def _api_root(self):
        """Identify the root URL of the launchpad API."""
        return self._instance.resource_type_link.split('#')[0]

    def __getattr__(self, attr):
        """Wrap launchpadlib so tightly you can't tell the difference."""
        assert not attr.startswith('_'), f"Can't getattr for {attr}"
        instance = super(Lp, self).__getattribute__('_instance')
        return getattr(instance, attr)

    @property
    @lru_cache()
    def ubuntu(self):
        """Shorthand for Ubuntu object.

        :rtype: distribution
        :returns: The distribution object for 'ubuntu'.
        """
        return self.distributions['ubuntu']

    @lru_cache()
    def ubuntu_active_series(self):
        """Identify currently supported Ubuntu series.

        This includes the series currently under development, but not
        ones which are experimental or obsolete.

        :rtype: list of distro_series
        :returns: All active Launchpad distro series for the Ubuntu project.
        """
        return [s for s in self.ubuntu.series if s.active]

    @property
    @lru_cache()
    def debian(self):
        """Shorthand for Debian object.

        :rtype: distribution
        :returns: The distribution object for 'debian'.
        """
        return self.distributions['debian']

    @lru_cache()
    def debian_active_series(self):
        """Identify currently supported Debian series.

        :rtype: list of distro_series
        :returns: All active Launchpad distro series for the Debian project.
        """
        return [s for s in self.debian.series if s.active]

    @lru_cache()
    def debian_experimental_series(self):
        """Shorthand for Debian experimental series.

        :rtype: distro_series
        :returns: The Launchpad distro series for the Debian project.
        """
        return next(iter([s for s in self.debian.series if s.name == 'experimental']), None)

    @lru_cache()
    def get_teams(self, user):
        """List teams that user belongs to.

        :param str user: Name of the user to look up.
        :rtype: list(str)
        :returns: List of team names.
        """
        with suppress(KeyError, TypeError):
            return [
                team.self_link.partition('~')[-1].partition('/')[0]
                for team in self.people[user].memberships_details]

    def load(self, url):
        """Return a lp resource from a launchpad url.

        :param str url: The launchpad resource URL.
        :rtype: varies
        :returns: Launchpadlib object corresponding to given url.
        """
        return self._instance.load(url)
