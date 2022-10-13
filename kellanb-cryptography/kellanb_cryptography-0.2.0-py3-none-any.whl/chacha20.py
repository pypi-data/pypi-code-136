import ast,json
from base64 import b64decode,b64encode
from Crypto.Cipher import ChaCha20


def encrypt_chacha_20(plaintext,key):
  t = plaintext.encode('utf-8')
  key = key.encode('ascii')

  chacha = ChaCha20.new(key=key)
  ciphertext = chacha.encrypt(t)
  nonce = b64encode(chacha.nonce).decode('utf-8')
  ct = b64encode(ciphertext).decode('utf-8')
  r = json.dumps({'nonce':nonce, 'ciphertext':ct})
  return f"{r}"

def decrypt_chacha_20(entxt,key):
  d = ast.literal_eval(entxt)
  key = key.encode('ascii')
  nonce = b64decode(d['nonce'])
  ciphertext = b64decode(d['ciphertext'])
  cipher = ChaCha20.new(key=key, nonce=nonce)
  plaintext = cipher.decrypt(ciphertext)
  return plaintext.decode('utf-8')
k = '12345678901234567890123456789012'
a = encrypt_chacha_20('kellan',k)
print(decrypt_chacha_20(a,k))