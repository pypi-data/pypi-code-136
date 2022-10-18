class LikesUtility:
    def __init__(self):
        self.enabled = False
        self.percentage = 0

    def set_enabled(self, enabled: bool):
        self.enabled = enabled

    def set_percentage(self, percentage: int):
        self.percentage = percentage