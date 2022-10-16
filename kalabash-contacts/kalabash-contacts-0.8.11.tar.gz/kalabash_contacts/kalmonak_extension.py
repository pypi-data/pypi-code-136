"""Declare and register the contacts extension."""

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy

from kalabash.core.extensions import KalmonakExtension, exts_pool
from kalabash.parameters import tools as param_tools

from . import __version__
from . import forms


class Contacts(KalmonakExtension):
    """Plugin declaration."""

    name = "kalabash_contacts"
    label = ugettext_lazy("Contacts")
    version = __version__
    description = ugettext_lazy("Address book")
    url = "contacts"
    topredirection_url = reverse_lazy("kalabash_contacts:index")

    def load(self):
        param_tools.registry.add(
            "user", forms.UserSettings, ugettext_lazy("Contacts"))


exts_pool.register_extension(Contacts)
