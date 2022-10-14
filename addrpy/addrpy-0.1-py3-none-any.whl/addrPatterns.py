class addrpattern1():
    ''' addrpattern1 follows the pattern : e.g. street address, city, state, zipcode
     for example, 1020 Wall Street, New York, New York, 12345
     '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = self._addrString
        addr_list = addrvalue.split(',')
        # print(addr_list[3])
        if addr_list[3][addr_list[3].isnumeric()]:
            # print('Detecting Zipcode: ',addr_list[3])
            if addr_list[2][addr_list[2].isalpha()]:
                addr_list[2] = addr_list[2].strip()
                # print('Detecting Statename:', addr_list[2])
                if addr_list[1][addr_list[1].isalpha()]:
                    addr_list[1] = addr_list[1].strip()
                    # print('Detecting Cityname:', addr_list[1])
                    if addr_list[0][addr_list[0].isalnum()]:
                        # print(addr_list[0])
                        addr_dict = {'street_address': addr_list[0].strip(),
                                     'city': addr_list[1].strip(),
                                     'state': addr_list[2].strip(),
                                     'zipcode': addr_list[3].strip()}
                        return addr_dict

class addrpattern2():
    ''' addrpattern2 follows the pattern : e.g. street address, city and zipcode combind.
        for example, input_address: 1020 Wall Street, New York 12345
                    output_address: {'street_address': 1020 Wall Street,'city': New York, 'zip': 12345}
     '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = self._addrString
        addr_list = addrvalue.split(',')
        print(addr_list)
        if not addr_list[1].isalpha():
            # print(addr_list[1])
            if not addr_list[0].isalpha():
                # print(addr_list[0])
                city_zip = addr_list[1].split(' ')
                # print(city_zip)
                if city_zip[city_zip[2].isdigit()]:
                    if city_zip[city_zip[1].isalpha()]:
                        if addr_list[0][addr_list[0].isalnum()]:
                            addr_dict = {'street_address': addr_list[0].strip(),'city': city_zip[1].strip(), 'zipcode': city_zip[2].strip()}
                            return addr_dict

class addrpattern3():
    ''' addrpattern3 follows the pattern: e.g. street_address, city, zipcode all separated by commas
    for example: input_address: 1020 Wall Street, New York, 12345
                output_address: { 'street_address': '1020 Wall Street', 'city': 'New York', 'zipcode:' 12345 }
    '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = self._addrString
        addr_list = addrvalue.split(',')
        if addr_list[2][addr_list[2].isdigit()]:
           if addr_list[1][addr_list[1].isalpha()]:
               if addr_list[0][addr_list[0].isalnum()]:
                   # print(addr_list[0])
                   addr_dict = {'street_address': addr_list[0].strip(), 'city': addr_list[1].strip(), 'zipcode': addr_list[2].strip()}
                   return addr_dict
