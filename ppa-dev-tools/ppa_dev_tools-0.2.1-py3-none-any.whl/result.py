#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Copyright (C) 2022 Authors
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.
#
# Authors:
#   Bryce Harrington <bryce@canonical.com>

"""The completed data from an autopkgtest run"""

import re
import urllib.request
from functools import lru_cache, cached_property
from typing import List, Iterator
import gzip
import time

from .subtest import Subtest
from .trigger import Trigger


class Result:
    """
    The completed data from an autopkgtest run Job.  This object
    provides access to the test run's settings and results.
    """
    VALUES = {
        'PASS': "✅",
        'FAIL': "❌",
        'BAD': "⛔"
    }

    def __init__(self, url, time, series, arch, source):
        """Initializes a new Result object.

        :param str url: HTTP path to the test log for this result.
        :param str time: The execution time of the test run.
        :param str series: The distro release series codename.
        :param str arch: The architecture for the result.
        :param str source:
        """
        self.url = url
        self.time = time
        self.series = series
        self.arch = arch
        self.source = source
        self.error_message = None
        self._log = None

    def __repr__(self) -> str:
        """Machine-parsable unique representation of object.

        :rtype: str
        :returns: Official string representation of the object.
        """
        return (f'{self.__class__.__name__}('
                f'url={self.url!r})')

    def __str__(self) -> str:
        """Human-readable summary of the object.

        :rtype: str
        :returns: Printable summary of the object.
        """
        return f"{self.source} on {self.series} for {self.arch} @ {self.timestamp}"

    @property
    def timestamp(self) -> str:
        """Formats the result's completion time as a string."""
        return time.strftime("%d.%m.%y %H:%M:%S", self.time)

    @cached_property
    def log(self) -> str:
        """Returns log contents for results, downloading if necessary.

        Retrieves the log via the result url, handles decompression, and
        caches the results internally, so that subsequent calls don't
        re-download the data.

        On error, returns None and stores the error message in
        the Result.error_message property.

        :rtype: str
        :returns: Full text of the log file, or None on error.
        """
        request = urllib.request.Request(self.url)
        request.add_header('Cache-Control', 'max-age=0')
        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.error_message = f"Failed to Download Test Log ⚪: {e}"
            return None

        result_gzip = response.read()
        try:
            return gzip.decompress(result_gzip).decode("utf-8",
                                                       errors="replace")
        except UnicodeDecodeError:
            self.error_message = "Broken Test Log ⚪"
            return None

    # TODO: Merge triggers and get_triggers()
    @cached_property
    def triggers(self) -> List[str]:
        """Returns package/version parameters used to generate this Result.

        This returns the set of triggers used to create the Result, as
        recorded in the test log.  Each trigger is a package/version
        pair corresponding to source packages to use from the proposed
        archive (instead of from the release archive).

        :rtype: list[str]
        :returns: List of package/version triggers.
        """
        regex_triggers = re.compile(r'--env=ADT_TEST_TRIGGERS=(.*?) -- ')
        header_split = self.log.split(": @@@@@@@@@@@@@@@@@@@@", 1)
        if len(header_split) < 2:
            return []
        m = re.search(regex_triggers, header_split[0])
        if not m:
            return []

        return m.group(1).strip("'").split()

    @lru_cache
    def get_triggers(self, name=None) -> Iterator[Trigger]:
        """Provides list of Triggers that were used to create this Result.

        This returns the set of Triggers used to create the Result, as
        recorded in the test log.  Each trigger identifies a
        package/version pair corresponding to source packages to use
        from the proposed archive (instead of from the release archive).

        :param str name: If defined, only return triggers starting with this name.
        :rtype: Iterator[Trigger]
        :returns: Triggers used to generate this Result, if any, or an empty list
        """
        if not self.triggers:
            return []

        for t in self.triggers:
            package, version = t.split('/', 1)
            yield Trigger(package, version, arch=self.arch, series=self.series)

    @lru_cache
    def get_subtests(self, name=None) -> List[Subtest]:
        """Provides list of Subtests that were run for this Result.

        :param str name: Only display subtests starting with this.
        :rtype: List[Subtest]
        :returns: Subtests completed for this Result, or empty list.
        """
        result_split = self.log.split("@@@@@@@@@@@@@@@@@@@@ summary", 1)
        if len(result_split) < 2:
            return []

        subtests = []
        result_sum = result_split[1]
        for line in re.findall("(.*PASS|.*SKIP|.*FAIL|.*BAD)", result_sum):
            if name and not line.startswith(name):
                continue
            subtests.append(Subtest(line))
        return subtests

    @cached_property
    def status(self) -> str:
        """Returns overall status of all subtests

        If the triggered run completed successfully, then the status will
        be either FAIL if any of the subtests failed, or PASS otherwise.

        If the run did not complete successfully, then a 'BAD' status
        will be returned, and the reason can be examined via the
        Result.error_message property.

        :rtype: str
        :returns: 'PASS', 'FAIL', or 'BAD'
        """
        if self.error_message:
            return 'BAD'

        for subtest in self.get_subtests():
            if subtest.status == 'FAIL':
                return 'FAIL'
        return 'PASS'

    @cached_property
    def status_icon(self) -> str:
        """Unicode symbol corresponding to test's overall status.

        :rtype: str
        :returns: Unicode symbol
        """
        return Result.VALUES[self.status]


def get_results(response, base_url, arches=None, sources=None) -> Iterator[Result]:
    """Returns iterator of Results from the base URL for given criteria

    Retrieves the autopkgtest results limited to the given architectures
    and source packages.  If unspecified, returns all results.

    :param str base_url: URL for the autopkgtest results.
    :param list[str] arches: Architectures to include in results.
    :param list[str] sources: Source packages to include in results.
    :rtype: Iterator[Result]
    :returns: Iterable results, if any, or an empty list on error
    """
    if response is None:
        return []
    for line in response.read().split(b'\n'):
        if line == b'' or not line.endswith(b"log.gz"):
            continue
        result = line.decode("utf-8")
        series, arch, _, source, timestamp = result.split('/')[:5]
        if (arches and (arch not in arches)):
            continue
        if (sources and (source not in sources)):
            continue
        yield Result(
            url=base_url + result,
            time=time.strptime(timestamp[:-7], "%Y%m%d_%H%M%S"),
            series=series,
            arch=arch,
            source=source)


if __name__ == "__main__":
    import os

    from ppa.io import open_url
    from ppa.constants import ARCHES_AUTOPKGTEST, URL_AUTOPKGTEST

    print("### Result class smoke test ###")

    timestamp = time.strptime('20030201_040506', "%Y%m%d_%H%M%S")
    result_1 = Result('url-here', timestamp, 'kinetic', 'amd64', 'my-package')
    print(repr(result_1))
    print(result_1)
    print()

    data_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), "../tests/data"))
    url = f"file://{data_dir}/results-six-s390x.log.gz"
    result_2 = Result(url, timestamp, 'kinetic', 'amd64', 'my-package')
    print("Log Head:")
    print("\n".join(result_2.log.splitlines()[0:4]))
    print()

    # TODO: Implement something that dumps the passing tests for given package from -proposed
    # TODO: Filter to items with only Pass, Not a regression, or No test results

    print("Loading live excuses data")
    base_results_fmt = f"{URL_AUTOPKGTEST}/results/autopkgtest-%s-%s-%s/"
    base_results_url = base_results_fmt % ('kinetic', 'bryce', 'nginx-merge-v1.22.0-1')
    url = f"{base_results_url}?format=plain"
    response = open_url(url)

    for result in get_results(response, base_results_url, arches=ARCHES_AUTOPKGTEST):
        print(f"* {result}")
        print(f"  - Triggers: " + ', '.join([str(r) for r in result.get_triggers()]))

        for subtest in result.get_subtests():
            print(f"  - {subtest}")

        print()
