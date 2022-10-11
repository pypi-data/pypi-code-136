import hashlib

def hash(content:str):
    return hashlib.new('md5', content.encode('utf-8')).hexdigest()