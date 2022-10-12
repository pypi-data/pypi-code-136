import secrets
from Crypto.Hash import SHA3_256

def create_hmac(msg, pwd):
  m = msg.encode('ascii')
  k = pwd.encode('ascii')
  ti = str(secrets.randbits(256))[:5]
  if len(str(ti)) < 5:
    for _ in range(len(ti)+1):
      ti += "0"
  ti = ti[:5]   
  t = ti.encode('ascii')
  hash = SHA3_256.new()
  hash.update(m + k+t)
  return hash.hexdigest()+ti
  
def verify_hmac(msg, mac, pwd):
  m = msg.encode('ascii')
  k = pwd.encode('ascii')
  ti = mac[-5:]
  hash = SHA3_256.new()
  hash.update(m + k+(ti.encode('ascii')))
  if hash.hexdigest()+ti == mac:
    return 1
  else:
    return 0
