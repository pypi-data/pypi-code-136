########################################################
# this module meant to provide crypto handling actions #
########################################################

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad


# will encrypt a data block
def encrypt(data, key, iv, mode=AES.MODE_CBC, padding_size=AES.block_size):
    encryption_cipher = AES.new(key, mode, iv)
    return encryption_cipher.encrypt(pad(data, padding_size))


# will decrypt a data block
def decrypt(data, key, iv, mode=AES.MODE_CBC, padding_size=AES.block_size):
    cipher = AES.new(key, mode, iv)
    # ans = cipher.decrypt(pad(data, padding_size)) # if, for some reason, you'll have a problem with decryption, uncheck this! and remove the other one
    pt = unpad(cipher.decrypt(data), padding_size)
    return pt
