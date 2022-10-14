"""Plugin navigation menu items."""
from nautobot.extras.plugins import PluginMenuItem


menu_items = (
    PluginMenuItem(
        link="plugins:nautobot_meme_otd:meme-otd",
        link_text="Meme Of The Day",
    ),
)
