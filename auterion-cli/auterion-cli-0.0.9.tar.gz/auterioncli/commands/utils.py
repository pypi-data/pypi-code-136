class Device:
    def __init__(self, address, version):
        self._address = address
        self._version = version

    @property
    def address(self):
        return self._address

    @property
    def version(self):
        return self._version


def error(msg, code=1):
    print(msg)
    exit(code)

