#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Author:  Bryce Harrington <bryce@canonical.com>
#
# Copyright (C) 2019 Bryce W. Harrington
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.

from .ppa import Ppa
from .text import o2str

from functools import lru_cache
from lazr.restfulclient.errors import BadRequest


class PpaAlreadyExists(BaseException):
    '''Exception indicating a PPA operation could not be performed'''

    def __init__(self, ppa_name, message=None):
        """
        :param str ppa_name: The name of the pre-existing PPA.
        :param str message: An error message.
        """
        self.ppa_name = ppa_name
        self.message = message

    def __str__(self):
        """Printable error message

        :rtype str:
        :return: Error message about the failure
        """
        if self.message:
            return self.message
        elif self.ppa_name:
            return f"The PPA {self.ppa_name} already exists"


class PpaGroup:
    """Represents a team or person that owns one or more PPAs.

    This class provides a proxy object for interacting with collections
    of PPA.
    """
    def __init__(self, service, name='me'):
        """
        :param launchpadlib.service service: The Launchpad service object.
        :param str name: Launchpad username
        """
        assert(service is not None)
        self.service = service

        if name == 'me':
            me = self.service.me
            self.name = me.name
        else:
            self.name = name

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'service={self.service!r}, name={self.name!r})')

    def __str__(self):
        return 'tbd'

    @property
    @lru_cache
    def team(self):
        """The team that owns this collection of PPAs.

        :rtype: tbd
        :returns: tbd
        """
        return self.service.people[self.name]

    def create(self, ppa_name='ppa', ppa_description=None):
        """Registers a new PPA with Launchpad.

        If a description is not provided a default one will be generated.

        :param str ppa_name: Name for the PPA to create.
        :param str ppa_description: Text description of the PPA.
        :rtype: Ppa
        :returns: A Ppa object that describes the created PPA.

        :raises PpaAlreadyExists: Raised if a PPA by this name already exists in Launchpad.
        """
        ppa_displayname = ''
        if ppa_description is None:
            ppa_description = ppa_name
            ppa_displayname = ppa_name

        try:
            self.team.createPPA(
                name=ppa_name,
                description=ppa_description,
                displayname=ppa_displayname)
            self.team.lp_save()
        except BadRequest as e:
            if "You already have a PPA" in o2str(e.content):
                raise PpaAlreadyExists(ppa_name, e.content)
            else:
                raise e

        return Ppa(ppa_name, self.name, ppa_description, service=self.service)

    @property
    @lru_cache
    def ppas(self):
        """Generator to access the PPAs in this group
        :rtype: Iterator[ppa.Ppa]
        :returns: Each PPA in the group as a ppa.Ppa object
        """
        for lp_ppa in self.team.ppas:
            if '-deletedppa' in lp_ppa.name:
                continue
            yield Ppa(lp_ppa.name, self.name,
                      service=self.service)

    @lru_cache
    def get(self, ppa_name):
        """Provides a Ppa for the named ppa.
        :rtype: ppa.Ppa
        :returns: A Ppa object describing the named ppa.
        """
        lp_ppa = self.team.getPPAByName(name=ppa_name)
        if not lp_ppa:
            return None
        return Ppa(lp_ppa.name, self.name,
                   service=self.service)
