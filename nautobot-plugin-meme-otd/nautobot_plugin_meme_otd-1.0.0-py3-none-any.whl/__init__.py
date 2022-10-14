"""Plugin declaration for nautobot_meme_otd."""

__version__ = "1.0.0"

from nautobot.extras.plugins import PluginConfig


class NautobotMemeOTDConfig(PluginConfig):
    """Plugin configuration for the nautobot_meme_otd plugin."""

    name = "nautobot_meme_otd"
    verbose_name = "Nautobot Meme Of The Day Plugin"
    version = __version__
    author = "Jeremy White"
    description = "Nautobot Meme Of The Day Plugin."
    base_url = "meme-otd"
    required_settings = []
    min_version = "1.4.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotMemeOTDConfig  # pylint:disable=invalid-name
