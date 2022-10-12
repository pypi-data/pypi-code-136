import secrets,string
from base64 import b64encode
from Crypto.Protocol.KDF import PBKDF2 
from Crypto.Hash import SHA256

def gen_random_key(size=256):
  l = (string. ascii_letters+string.punctuation+string.digits)
  a= ""
  for i in range(int(size/8)):
    a += secrets.choice(l)
  return a

def gen_key_from_password(pwd,len_=256):
  bytelen = len_/8
  p = pwd.encode('ascii')
  key =PBKDF2(p,int(bytelen) , count=1, hmac_hash_module=SHA256)
  i = (b64encode(key).decode("utf-8"))
  if len(str(i))<bytelen:
    key2 = PBKDF2(p,i[0],int(bytelen) , count=1, hmac_hash_module=SHA256)
  k3 = (key+key2)
  return (b64encode(k3).decode("utf-8"))[0:int(bytelen)]

