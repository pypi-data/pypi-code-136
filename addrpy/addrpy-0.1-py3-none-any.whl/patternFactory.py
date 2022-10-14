from addrPatterns import addrpattern1, addrpattern2, addrpattern3

class addrpatternfactory():
    def __init__(self, address):
        self._address = address

    def get_addr(self):
        return addrpattern1(self._address)

    def fix_address(self):
        if self._address.count(', ') == 3:
            # print('Address Pattern 1 - splitting into four elems => ')
            return addrpattern1(self._address)

        if self._address.count(',') == 1:
            # print('Address Pattern 2 - splitting into three elems => ')
            return addrpattern2(self._address)

        if self._address.count(',') == 2:
            # print('Address Pattern 3 - splitting into three elems')
            return addrpattern3(self._address)
