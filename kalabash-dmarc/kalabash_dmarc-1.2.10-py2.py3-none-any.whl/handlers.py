"""Django signal handlers for kalabash_dmarc."""

from django.urls import reverse
from django.utils.translation import ugettext as _
from django.dispatch import receiver

from kalabash.admin import signals as admin_signals

from . import models


@receiver(admin_signals.extra_domain_actions)
def dmarc_domain_actions(sender, user, domain, **kwargs):
    """Return a link to access domain report."""
    if not models.Record.objects.filter(header_from=domain).exists():
        return []
    return [{
        "name": "dmarc_report",
        "url": reverse("kalabash_dmarc:domain_report", args=[domain.pk]),
        "title": _("Show DMARC report for {}").format(domain.name),
        "img": "fa fa-pie-chart"
    }]
