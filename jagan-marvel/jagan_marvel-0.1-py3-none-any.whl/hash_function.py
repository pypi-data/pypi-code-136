
import hashlib


def hash_params(timestamp, pub_key, priv_key):
    ''' This function is taking the timestamp and keys as parameter 
        and returs a hash value'''

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params
