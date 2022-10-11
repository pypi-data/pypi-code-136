"""
Lifeguard MongoDB Settings
"""
from lifeguard.settings import SettingsManager

SETTINGS_MANAGER = SettingsManager(
    {
        "LIFEGUARD_MSTEAMS_DEFAULT_CHAT_ROOM": {
            "default": "",
            "description": "Incoming webhook full address",
        },
    }
)

MSTEAMS_DEFAULT_CHAT_ROOM = SETTINGS_MANAGER.read_value(
    "LIFEGUARD_MSTEAMS_DEFAULT_CHAT_ROOM"
)
