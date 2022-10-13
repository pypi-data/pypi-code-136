import hashlib
def hash_params(ts,priv_key,pub_key):
    temp=f'{ts}{priv_key}{pub_key}'
    hash_md5 = hashlib.md5()
    hash_md5.update(temp.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params