class _Login:
    '''
    Store username when user logs in successfully
    '''

    def __init__(self):
        self.username = None

    def login(self, username):
        self.username = username
