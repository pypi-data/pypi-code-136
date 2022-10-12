import base64

def encrypt(text:str):
    ret = base64.b64encode(bytes(text, encoding='UTF-8'))
    return str(ret, 'UTF-8')

def decrypt(text:str):
    ret = base64.b64decode(bytes(text, encoding='UTF-8'))
    return str(ret, 'UTF-8')