class InvalidArgumentUseError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class InvalidFlagUseError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
