# -*- coding:utf-8 -*-
# 文件:  aes.py
# 日期:  2022/9/8 9:37
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
import base64
import binascii
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


__version__ = "1.2"
__all__ = [
    "aes_gcm_encrypt", "aes_gcm_decrypt",
    "aes_cbc_encrypt",
    "aes_ecb_encrypt", "aes_ecb_decrypt"
]


def aes_gcm_encrypt(key, data, nonce, associated_data=None):
    """
    AES-GCM加密
    :param key: 密钥。16, 24 or 32字符长度的字符串
    :param data: 待加密字符串
    :param associated_data: 附加数据，一般为None
    :param nonce: 随机值，和MD5的“加盐”有些类似，目的是防止同样的明文块，始终加密成同样的密文块
    """
    key = key.encode("utf-8")
    data = data.encode("utf-8")
    nonce = nonce.encode("utf-8") if nonce else "12345678".encode("utf-8")
    associated_data = associated_data.encode("utf-8") if associated_data else None

    # 生成加密器
    cipher = AESGCM(key)
    # 加密数据
    crypt_bytes = cipher.encrypt(nonce, data, associated_data)
    return base64.b64encode(crypt_bytes).decode()


def aes_gcm_decrypt(key, cipher_data, nonce, associated_data=None):
    """
    AES-GCM解密
    :param key: 密钥。16, 24 or 32字符长度的字符串
    :param cipher_data: encrypt_aes_gcm 方法返回的数据
    :param nonce: 随机值，和MD5的“加盐”有些类似，目的是防止同样的明文块，始终加密成同样的密文块
    :param associated_data: 附加数据，一般为None
    :return:
    """
    key = key.encode("utf-8")
    nonce = nonce.encode("utf-8") if nonce else "12345678".encode("utf-8")
    associated_data = associated_data.encode("utf-8") if associated_data else None
    cipher_data = base64.b64decode(cipher_data)  # 进行base64解码
    cipher = AESGCM(key)
    # 解密数据
    try:
        plaintext = cipher.decrypt(nonce, cipher_data, associated_data).decode("utf-8")
    except InvalidTag:
        plaintext = None
    return plaintext


block_size = 128


def aes_ecb_encrypt(secret_key, data):
    """AES_ECB加密数据
    :param secret_key: 加密秘钥
    :param data: 需要加密数据
    """
    # 将数据转换为byte类型
    data = data.encode("utf-8")
    secret_key = secret_key.encode("utf-8")

    # 填充数据采用 pkcs7
    pad = padding.PKCS7(block_size).padder()
    pad_data = pad.update(data) + pad.finalize()

    # 创建密码器
    cipher = Cipher(algorithms.AES(secret_key), mode=modes.ECB(), backend=default_backend())
    # 加密数据
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(pad_data)
    return base64.b64encode(encrypted_data).decode()


def aes_ecb_decrypt(secret_key, data):
    """AES_ECB解密数据"""
    secret_key = secret_key.encode("utf-8")
    data = base64.b64decode(data)

    # 创建密码器
    cipher = Cipher(algorithms.AES(secret_key), mode=modes.ECB(), backend=default_backend())
    decrypter = cipher.decryptor()
    decrypt_data = decrypter.update(data)
    un_pad = padding.PKCS7(block_size).unpadder()
    un_pad_decrypt_data = un_pad.update(decrypt_data) + un_pad.finalize()
    return un_pad_decrypt_data.decode("utf-8")


def _zero_pad(s):
    # Zero Padding
    if isinstance(s, bytes):
        s = s.decode("utf-8")
    return (s + (16 - len(s) % 16) * '\0').encode('utf-8')


def aes_cbc_encrypt(data, key, iv, encode=1):
    """
    use AES CBC to encrypt message, using key and init vector， padding: ZeroPadding
    :param data: 待加密的数据
    :param key:  加密所用的key
    :param iv:   加密所有的初始化向量 Init Vector
    :param encode:  加密后密文的编码方式， 1-base64, 2-binascii.hexlify(转为16进制,1byte->2字符)
    :return:
    """
    padded_data = _zero_pad(data)   # bytes
    key = key.encode('utf8')
    iv = iv[:16].encode('utf8')
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    enc_content = encryptor.update(padded_data) + encryptor.finalize()
    if encode == 1:  # base64编码
        enc_data = base64.b64encode(enc_content).decode('utf8')
    else:   # encode == 2  # 1byte 转 16进制2个字符,
        enc_data = binascii.hexlify(enc_content).decode('utf-8')
    return enc_data


if __name__ == '__main__':
    my_key = "JP67DD47BSO8B2C43JEZ7UA0ZHV60SB2"
    my_iv = "1234567812345678"
    my_data = '{"lang":"zh-CN","pageNumber":1,"pageSize":10,"cycleId":"1522973936269266945"}'

    print("原始数据：%s" % my_data)
    r = aes_ecb_encrypt(my_key, my_data)
    print("加密数据 [aes_ecb_encrypt]：%s" % r)
    r = aes_ecb_decrypt(my_key, r)
    print("解密数据：%s" % r)

    ret = aes_cbc_encrypt(my_data, my_key, my_iv, encode=1)
    print(f"加密后 [aes_cbc_encrypt]：{ret}")
