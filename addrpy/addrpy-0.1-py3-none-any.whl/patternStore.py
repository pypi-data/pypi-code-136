class addrStore:
    def __init__(self, addr_factory=None):
        self._addr_factory = addr_factory

    def show_addr(self):
        addr = self._addr_factory.get_addr()
        # return print('Input Address: ', addr.show_addr())
        return addr.show_addr()

    def fix_addr(self):
        addr = self._addr_factory.fix_address()
        # print("================================")
        # print("-- After being processed: ", format(addr.fixing_addr()))
        return addr.fixing_addr()

