"""Management command tests."""

from kalabash.admin import factories as admin_factories
from kalabash.lib.tests import KalmonakTestCase

from . import mixins
from .. import models


class ManagementCommandTestCase(mixins.CallCommandMixin, KalmonakTestCase):
    """Test management command."""

    @classmethod
    def setUpTestData(cls):
        super(ManagementCommandTestCase, cls).setUpTestData()
        cls.domain = admin_factories.DomainFactory(name="ngyn.org")

    def test_import_from_archive(self):
        """Import report from archive."""
        self.import_reports()
        self.import_fail_reports()
        self.assertTrue(self.domain.record_set.exists())
        self.assertTrue(
            models.Reporter.objects.filter(
                org_name="FastMail Pty Ltd").exists())
