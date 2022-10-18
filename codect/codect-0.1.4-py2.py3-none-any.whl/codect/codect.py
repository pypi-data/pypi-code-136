from Crypto.Cipher import AES
import base64
import hashlib
import sys

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def estr(raw_string, secret_key):   # Encrypt string
    try:
        iv = ''
        for char in secret_key:
            iv += str(ord(char))
        if len(iv) < 16:
            iv = iv * 16
        print(iv)
        secret_key = hash_string(secret_key)[::2].encode('utf-8')
        raw_string = pad(base64.b64encode(raw_string.encode('utf-8')).decode('utf-8')).encode('utf-8')
        encoder = AES.new(secret_key, AES.MODE_CBC, iv[:16].encode('utf-8'))
        return base64.b64encode(encoder.encrypt(raw_string)).decode('utf-8')
    except Exception as err:
        print(err)
        sys.exit(0)
 
def dstr(encrypted_string, secret_key):   # Decrypt string
    try:
        iv = ''
        for char in secret_key:
            iv += str(ord(char))
        if len(iv) < 16:
            iv = iv * 16
        secret_key = hash_string(secret_key)[::2].encode('utf-8')
        encrypted_string = base64.b64decode(encrypted_string.encode('utf-8'))
        decoder = AES.new(secret_key, AES.MODE_CBC, iv[:16].encode('utf-8'))
        final = base64.b64decode(unpad(decoder.decrypt(encrypted_string))).decode('utf-8')
        #print(final)
        return final
    except:
        sys.exit(0)