"""Django signal handlers for kalabash_admin_relaydomains."""

from django.dispatch import receiver

from kalabash.lib.email_utils import split_mailbox

from kalabash_admin import models as admin_models
from kalabash_admin.signals import use_external_recipients

from . import models


@receiver(use_external_recipients)
def check_relaydomain_alias(sender, **kwargs):
    """Allow the creation of an alias on a relaydomain."""
    recipient = kwargs.get("recipients")
    if not recipient:
        return
    localpart, domain = split_mailbox(recipient)
    if not (models.RelayDomain.objects.select_related().filter(
            domain__name=domain).exists()):
        return False
    if (admin_models.Mailbox.objects.select_related("domain").filter(
            domain__name=domain, address=localpart).exists()):
        return False
    return True
