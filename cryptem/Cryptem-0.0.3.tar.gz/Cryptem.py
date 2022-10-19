"""
Cryptographic applications library based on elliptic curve cryptography.
Can be used for asymmetric and symmetric cryptography, signature verification,
and supports password-secured cryptography.
Built on the eciespy, coincurve and hashlib modules.
"""

import hashlib
import os
import traceback
from ecies.utils import generate_key
from ecies import encrypt, decrypt
from coincurve import PrivateKey, PublicKey, verify_signature
from cryptography.fernet import Fernet


class Crypt:
    """Encryption/decryption engine for bytearrays.
    Can be used for single-session public-key/private-key cryptography
    as well as for password secured multi-session public-key/private-key or private-key-only cryptography.
    * Single-session means the keys are used only as long as the Crypt instance exists,
    * so when the program is restarted different keys are used.
    * Multi-session means that the same keys can be reused after restarting the program,
    * a simplified form of the private key must be memorised by the useras a password.
    Usage:
        - As Single-Session Asymetric Encryption System (public-key and private-key):
            # Communication Receiver:
            codec = Crypt()
            public_key = codec.public_key

            ## give public_key to Sender

            # Communication Sender:
            codec2 = Encryptor(public_key)
            cipher = codec2.Encrypt("Hello there!".encode('utf-8'))

            ## transmit cipher to Receiver

            # Communication Receiver:
            plaintext = codec.Decrypt(cipher).decode('utf-8')

        - As Multi-Session Asymetric Encryption System (public-key and private-key):
            # Communication Receiver:
            codec = Crypt("mypassword")   # KEEP PASSWORD PRIVATE AND SAFE
            public_key = codec.public_key

            ## give public_key to Sender

            # Communication Sender:
            codec2 = Encryptor(public_key)
            cipher = codec2.Encrypt("Hello there!".encode('utf-8'))

            ## transmit cipher to Receiver

            # Communication Receiver:
            plaintext = codec.Decrypt(cipher).decode('utf-8')


        - As Multisession Symetric Enryption System (private-key only):
            codec = Crypt("my_password")   # KEEP PASSWORD PRIVATE AND SAFE
            cipher = codec.Encrypt("Hello there!".encode('utf-8'))

            ## transmit cipher to other person

            codec2 = Crypt("my_password")
            plaintext = codec2.Decrypt(cipher).decode('utf-8')
    """

    public_key = ""
    __private_key = ""

    def __init__(self, password=None):
        if password == None:
            key = generate_key()    # generate new random key
        else:
            # creating a cryptographic hash from the password, to create a larger encryption key from it
            hashGen = hashlib.sha256()
            hashGen.update(password.encode())
            hash = hashGen.hexdigest()

            key = PrivateKey.from_hex(hash)

        self.__private_key = key
        self.public_key = key.public_key.format(False).hex()

    def Encrypt(self, data_to_encrypt: bytearray):
        return Encrypt(data_to_encrypt, self.public_key)

    def Decrypt(self, encrypted_data: bytearray):
        try:
            if(type(encrypted_data) == bytearray):
                encrypted_data = bytes(encrypted_data)
            decrypted_data = decrypt(
                self.__private_key.to_hex(), encrypted_data)
            return decrypted_data
        except Exception as e:
            print("Failed at decryption.")
            print(e)
            print("----------------------------------------------------")
            traceback.print_exc()  # printing stack trace
            print("----------------------------------------------------")
            print("")
            # print(encrypted_data)
            return None

    def EncryptFile(self, plain_file, encrypted_file):
        return EncryptFile(plain_file, encrypted_file, self.public_key)

    def DecryptFile(self, encrypted_file, decrypted_file):

        with open(encrypted_file, 'rb') as file:
            encrypted_data = file.read()
        key = encrypted_data[:141]   # extract encrypted key from file
        encrypted_data = encrypted_data[141:]    # remove encrypted key from file

        # decrypt encrypted key and create file-decrypting Fernet object from it
        f = Fernet(self.Decrypt(key))

        decrypted_data = f.decrypt(encrypted_data)  # decrypt file

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted_data)

    def Sign(self, data: bytes):
        return self.__private_key.sign(data)

    def SignSmall(self, data: bytearray):
        hashGen = hashlib.sha256()
        hashGen.update(self.Sign(data))
        return hashGen.hexdigest()


class Encryptor:
    def __init__(self, public_key):
        self.public_key = public_key

    def Encrypt(self, data):
        return Encrypt(data, self.public_key)

    def EncryptFile(self, plain_file, encrypted_file):
        return EncryptFile(plain_file, encrypted_file, self.public_key)

    def VerifySignature(self, data, signature):
        pk = PublicKey(self.public_key)
        return pk.verify(signature, data)
        return verify_signature(signature, data, self.public_key)


def Encrypt(data_to_encrypt: bytearray, public_key):
    """Encryption-only engine for bytearrays, based on public-key.
    Usage:
        # Communication Receiver:
        codec = Crypt()
        public_key = codec.public_key

        ## give public_key to Sender

        # Communication Sender:
        cipher = Encrypt("Hello there!".encode('utf-8'), public_key)

        ## transmit cipher to Receiver

        # Communication Receiver:
        plaintext = codec.Decrypt(cipher).decode('utf-8')
    """
    try:
        if type(data_to_encrypt) == str:
            print("data to encrypt must be of type bytearray")
        if type(public_key) == bytearray:
            public_key = public_key.hex()
        encrypted_data = encrypt(public_key, data_to_encrypt)
        return encrypted_data
    except Exception as e:
        print("Failed at encryption.")
        print(e)
        print("----------------------------------------------------")
        traceback.print_exc()  # printing stack trace
        print("----------------------------------------------------")
        print("")
        print("public key: " + public_key)
        print("")
        return None


def EncryptFile(plain_file, encrypted_file, public_key):
    """
    Encrypt a file.
    Parameters:
        plain_file: the path of the file to encrypt
        encrypted_file: where the encrypted file should be saved
    """
    key = Fernet.generate_key()
    f = Fernet(key)

    with open(plain_file, 'rb') as file:
        plain_data = file.read()
    encrypted_data = f.encrypt(plain_data)

    key_encrypted = Encrypt(key, public_key)

    encrypted_data = key_encrypted + encrypted_data
    with open(encrypted_file, 'wb') as file:
        file.write(encrypted_data)


def VerifySignature(data: bytes, public_key: bytes, signature: bytes):
    if isinstance(public_key, str):
        public_key = bytes(bytearray.fromhex(public_key))
    return verify_signature(signature, data, public_key)
