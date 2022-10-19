from remotemanager.storage.sendablemixin import SendableMixin


class placeholder_option(SendableMixin):
    """
    Stub class to sit in place of an option within a computer.
    """

    def __init__(self, mode):
        self.mode = mode

    def __hash__(self):
        return hash(self.mode)

    def __bool__(self):
        """
        Make the objects "falsy" this enables rapid defaulting:

        `value = option or default`
        """
        return False


required = placeholder_option('required')
optional = placeholder_option('optional')
