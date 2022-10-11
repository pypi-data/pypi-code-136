"""
Lifeguard integration with MS Teams
"""
from lifeguard.notifications import append_notification_implementation

from lifeguard_notification_msteams.notifications import MSTeamsNotificationBase


class LifeguardNotificationMSTeams:
    def __init__(self, lifeguard_context):
        self.lifeguard_context = lifeguard_context
        append_notification_implementation(MSTeamsNotificationBase)


def init(lifeguard_context):
    LifeguardNotificationMSTeams(lifeguard_context)
