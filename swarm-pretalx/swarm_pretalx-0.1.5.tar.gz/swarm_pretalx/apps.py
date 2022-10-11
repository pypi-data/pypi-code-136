from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = "swarm_pretalx"
    verbose_name = "Pretalx plugin for exporting the agenda to Swarm"

    class PretalxPluginMeta:
        name = gettext_lazy("Pretalx plugin for exporting the agenda to Swarm")
        author = "cmdctrlesc"
        description = gettext_lazy("Pretalx plugin for exporting the agenda to Swarm")
        visible = True
        version = "0.0.0"

    def ready(self):
        from . import signals  # NOQA
