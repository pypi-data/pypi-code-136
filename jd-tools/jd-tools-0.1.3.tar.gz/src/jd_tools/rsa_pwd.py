# -*- coding:utf-8 -*-
# 文件:  rsa_pwd.py
# 日期:  2021/10/27 15:45
# 描述:  生成RSA 公钥、私钥， 使用 RSA 解密密码
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization    # , hashes
import binascii
from .tools import singleton


__version__ = '3.2'

__all__ = [
    'remove_rsa_public_header', 'remove_rsa_private_header',
    'jd_decrypt', 'JdRsa'
]


@singleton
class JdRsa(object):

    def __init__(self):
        self.pub_file = ''
        self.pri_file = ''

    def set_file(self, public, private):
        self.pub_file = public
        self.pri_file = private

    def generate_rsa_key(self):
        # 生成 RSA 公钥 和 私钥

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend())
        public_key = private_key.public_key()

        # store private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(self.pri_file, "wb") as f:
            f.write(private_pem)

        # store public key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(self.pub_file, "wb") as f:
            f.write(public_pem)

    def get_rsa_public_key(self):
        # 从文件获取 RSA 公钥
        with open(self.pub_file) as f:
            pub_key_ = f.read()
            # pub_key_ = remove_rsa_public_header(pub_key_)
        return pub_key_

    def encrypt(self, msg):
        # 加密（encrypt）
        with open(self.pub_file, 'rb') as f:
            key = f.read()
            public_key = serialization.load_pem_public_key(
                key,
                backend=default_backend()
            )

        encrypted = public_key.encrypt(
            msg.encode('utf-8'),
            padding.PKCS1v15()
            # padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()), algorithm=hashes.SHA1(), label=None)
        )
        cipher_text = base64.b64encode(encrypted).decode('utf-8')

        return cipher_text

    def decrypt(self, encrypt_text):
        # 解密（decrypt）

        with open(self.pri_file, 'rb') as f:
            key = f.read()
            private_key = serialization.load_pem_private_key(
                key,
                password=None,
                backend=default_backend()
            )

        encrypted = base64.b64decode(encrypt_text)
        original_message = private_key.decrypt(
            encrypted,
            padding.PKCS1v15()
            # padding.OAEP(mgf=padding.MGF1(algorithm=padding.PKCS1v15()), algorithm=hashes.SHA1(), label=None)
        )

        text = original_message.decode('utf-8')
        return text


def remove_rsa_private_header(rsa_private_key):
    if isinstance(rsa_private_key, bytes):
        rsa_private_key = rsa_private_key.decode('utf-8')
    rsa_private_key = rsa_private_key.replace("-----BEGIN RSA PRIVATE KEY-----", '')\
        .replace("-----END RSA PRIVATE KEY-----", '').replace('\n', '')
    return rsa_private_key


def remove_rsa_public_header(rsa_private_key):
    if isinstance(rsa_private_key, bytes):
        rsa_private_key = rsa_private_key.decode('utf-8')
    rsa_private_key = rsa_private_key.replace("-----BEGIN PUBLIC KEY-----", '')\
        .replace("-----END PUBLIC KEY-----", '').replace("\n", '')
    return rsa_private_key


def jd_decrypt(pwd):    # RSA解密，捕获异常
    try:
        jd_rsa = JdRsa()
        password = jd_rsa.decrypt(pwd)
    except (TypeError, ValueError, binascii.Error):
        return False, ''    # 解密错误
    return True, password
