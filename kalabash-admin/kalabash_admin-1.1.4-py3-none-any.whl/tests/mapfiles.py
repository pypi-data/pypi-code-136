"""Test map files generation."""

from django.test import TestCase

from kalabash.lib.test_utils import MapFilesTestCaseMixin


class MapFilesTestCase(MapFilesTestCaseMixin, TestCase):

    """Test case for kalabash_admin."""

    extension = "kalabash_admin"

    MAP_FILES = [
        "sql-domains.cf", "sql-domain-aliases.cf", "sql-aliases.cf",
        "sql-maintain.cf"
    ]
