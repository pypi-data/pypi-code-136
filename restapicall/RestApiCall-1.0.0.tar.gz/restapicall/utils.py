#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import urllib


class Utils(object):

    @staticmethod
    def build_uri(endpoint, uri, args):
        """
        Build the URL using the endpoint, uri and args.
        :param endpoint: str
        :param uri: tuple
        :param args: dict
        :return: str
        """

        uri_items = [endpoint]
        for x in uri:
            uri_items.append(str(x))

        url = "/".join(uri_items)
        if args:
            url = url + "?" + urllib.parse.urlencode(args)
        return url
