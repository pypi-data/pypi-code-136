class MissingConfiguration(Exception):

    def __init__(self, key, message="missing environment variable"):
        self.key = key
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} : {self.key}'

