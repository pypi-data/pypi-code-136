# encoding: utf-8
# api: python
##type: classes
# category: http
# title: request/fallback
# description: loads requests, or similuates API via urllib
# version: 0.5
# state: beta
# depends: python:requests (>= 2.5)
# config: -
# pylint: disable=invalid-name
#
# Wraps requests or fakes a http.get() implementation.
#


__all__ = ["http", "urllib", "urlencode", "quote", "quote_plus", "update_headers"]


# http preparations
import logging as log
import urllib
try:
    from urllib.parse import urlencode, quote, quote_plus
    from urllib.request import urlopen, Request
except ImportError:
    from urllib import urlencode, quote, quote_plus
    from urllib2 import urlopen, Request
#else:
#    from six.moves.urllib import urlencode, quote, quote_plus
#    from six.moves.urllib.request import urlopen, Request

try:
    import requests
    http = requests.Session()

except ImportError:

    log.error(
        "Missing library: `pip install requests` (system-wide, or into libreoffice program/ dir)"
    )

    class FakeRequests:
        """ GET only """

        content = ""
        ssl_args = {}
        headers = {}

        def __init__(self):
            """ optional ssl """
            import ssl
            if not hasattr(ssl, "create_default_context"):
                return
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            self.ssl_args["context"] = context

        def get(self, url):
            """ urlopen """
            self.content = urlopen(
                Request(url, headers=self.headers), **self.ssl_args
            ).read()
            return self

    http = FakeRequests()
    log.info("using fake_requests() for now")

# headers
def update_headers(office_version="LibreOffice/7.x", pt_version="2.0"):
    http.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Linux; " + office_version + "), PageTranslate/" + pt_version,
        "Accept-Language": "*; q=1.0",
        "Accept-Encoding": "utf-8"
    })

update_headers()
