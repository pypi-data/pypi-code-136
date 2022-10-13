from Crypto.Cipher import AES
import ast

def encrypt_aes(string,key,mode='GCM'):
  m = ''
  if mode == 'GCM':
    m = AES.MODE_GCM
  elif mode == 'EAX':
    m = AES.MODE_EAX
  elif mode == 'CCM'  :
    m = AES.MODE_CCM
  else: 
    raise Exception(f"no mode {mode}")
  st_utf = string.encode('utf-8')
  k = bytes(key.encode('ascii'))
  cipher = AES.new(k, m)
  ciphertext, tag = cipher.encrypt_and_digest(st_utf)
  z = [x for x in (cipher.nonce, tag, ciphertext)]
  return f"{z}"
  

def decrypt_aes(en,key,mode='GCM'):
  m = ''
  if mode == 'GCM':
    m = AES.MODE_GCM
  elif mode == 'EAX':
    m = AES.MODE_EAX
  elif mode == 'CCM'  :
    m = AES.MODE_CCM
  else: 
    raise Exception(f"no mode {mode}")
  en = ast.literal_eval(en)
  key = bytes(key.encode('ascii'))
  print('\n\n\n !')
  print(en)
  print('\n\n\n !')
  tag, ciphertext = en[1],en[2]
  no = en[0]
  print('\n\n\n !!')
  print(en[0])
  print('\n\n\n !!')
  cipher = AES.new(key, m, no)
  data = cipher.decrypt_and_verify(ciphertext, tag)
  return data.decode('utf-8')
  