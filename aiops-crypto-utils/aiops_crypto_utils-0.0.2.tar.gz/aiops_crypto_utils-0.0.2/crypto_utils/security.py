import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, source):
    """
    Method to encrypt data
    """
    source = str(source).encode('utf-8')
    # use SHA-256 over our key to get a proper-sized AES key
    key = SHA256.new(key.encode('utf-8')).digest()
    iv = Random.new().read(AES.block_size)  # generate iv
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = iv + encryptor.encrypt(source)  # store the iv at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1")

def decrypt(key, source):
    """
    Method to decrypt data
    """
    source = base64.b64decode(source.encode("latin-1"))
    # use SHA-256 over our key to get a proper-sized AES key
    key = SHA256.new(key.encode('utf-8')).digest()
    iv = source[:AES.block_size]  # extract the iv from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding
