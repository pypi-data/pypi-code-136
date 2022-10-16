"""Radicale management frontend."""

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy

from kalabash.core.extensions import KalmonakExtension, exts_pool
from kalabash.parameters import tools as param_tools

from . import __version__
from . import forms


class Radicale(KalmonakExtension):
    """Radicale extension declaration."""

    name = "kalabash_radicale"
    label = ugettext_lazy("Radicale management")
    topredirection_url = reverse_lazy("kalabash_radicale:index")
    version = __version__
    url = "calendars"
    description = ugettext_lazy(
        "Management frontend for Radicale, a simple calendar and contact "
        "server."
    )

    def load(self):
        """Plugin loading."""
        param_tools.registry.add(
            "global", forms.ParametersForm, "Radicale")

exts_pool.register_extension(Radicale)
