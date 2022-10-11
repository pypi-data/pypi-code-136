class Notification:
    BOLD = '\033[1m'
    BLUE = '\033[94m'
    BLUE_BOLD = BLUE + BOLD
    GREEN = '\033[92m'
    GREEN_BOLD = GREEN + BOLD
    YELLOW = '\033[93m'
    YELLOW_BOLD = YELLOW + BOLD
    RED = '\033[91m'
    RED_BOLD = RED + BOLD
    RESET = '\033[0m'
    RED_ALERT = f'[{RED}!{RESET}]'
    YELLOW_ALERT = f'[{YELLOW}!{RESET}]'
    QUESTION = f'[{YELLOW}?{RESET}]'

    def __init__(self, color):
        self.colorname = color
        self.reset = Notification.RESET
        if self.colorname == 'bold':
            self.color = Notification.BOLD
        elif self.colorname == 'blue':
            self.color = Notification.BLUE
        elif self.colorname == 'blue_bold':
            self.color = Notification.BLUE_BOLD
        elif self.colorname == 'green':
            self.color = Notification.GREEN
        elif self.colorname == 'green_bold':
            self.color = Notification.GREEN_BOLD
        elif self.colorname == 'yellow':
            self.color = Notification.YELLOW
        elif self.colorname == 'yellow_bold':
            self.color = Notification.YELLOW_BOLD
        elif self.colorname == 'red':
            self.color = Notification.RED
        elif self.colorname == 'red_bold':
            self.color = Notification.RED_BOLD
        elif self.colorname == 'red_alert':
            self.color = Notification.RED_ALERT
        elif self.colorname == 'yellow_alert':
            self.color = Notification.YELLOW_ALERT
        elif self.colorname == 'question':
            self.color = Notification.QUESTION

    def print(self, message):
        if self.colorname in ['red_alert', 'yellow_alert']:
            print(f'{self.color} {message}{self.reset}')
        else:
            print(f'{self.color}{message}{self.reset}')

    def text(self, message):
        return input(f'{self.color} {message}{self.reset}: ')
