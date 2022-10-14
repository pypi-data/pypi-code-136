'''
Author: Guo Wei
'''

def hexstring_to_string(hex_string):
    '''
    param: hex_string,
    '''
    if hex_string.startswith('0x'):
        hex_string = hex_string[2::]
    return bytes.fromhex(hex_string).decode('utf-8')

def string_to_hexstring(string,length=0):
    _ = "{:#0" + str(length) + "X}"  # {:#066X}
    return _.format(int(string.encode('ascii').hex(), 16)).lower()

print(hexstring_to_string('784249424C780000000000000000000000000000'))
print(string_to_hexstring('xBIBLx'))