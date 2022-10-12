from Crypto.Hash import SHA256,SHA512,SHA3_256,SHA3_512


def sha256(str):
  return SHA256.new(data=str.encode('ascii')).hexdigest()

def sha512(str):
  return SHA512.new(data=str.encode('ascii')).hexdigest()
def sha3_256(str):
  return SHA3_256.new(data=str.encode('ascii')).hexdigest()

def sha3_512(str):
  return SHA3_512.new(data=str.encode('ascii')).hexdigest()
