"""DMARC tools for Kalabash."""

from django.utils.translation import ugettext_lazy

from kalabash.core.extensions import KalmonakExtension, exts_pool
from kalabash.parameters import tools as param_tools

from . import __version__
from . import forms


class DmarcExtension(KalmonakExtension):
    """Extension registration."""

    name = "kalabash_dmarc"
    label = ugettext_lazy("DMARC tools")
    version = __version__
    description = ugettext_lazy(
        "A set of tools to ease DMARC integration"
    )
    url = "dmarc"

    def load(self):
        """Extension loading."""
        param_tools.registry.add("global", forms.ParametersForm, "DMARC")


exts_pool.register_extension(DmarcExtension)
