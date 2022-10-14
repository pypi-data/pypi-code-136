# from addrPatterns import addrpattern1, addrpattern2
from patternFactory import addrpatternfactory
from patternStore import addrStore

def preprocess_addr(address):
    addr = addrpatternfactory(address)
    # print(addrFact.get_addr().show_addr())
    addr = addrStore(addr)
    # addr.show_addr()
    return addr.fix_addr()

