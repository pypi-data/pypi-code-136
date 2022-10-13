__Author__ = "Pranav Chandran"
__Date__ = 12 - 10 - 2022

import json
import datetime

"""
A helper function to get the secrets from the json file (Encrypted) and
 return the decrypted secrets
 
Data_template:
{'data': 
    [{'Category': 'Database', 
    'Server': 'xxxxxxx', 
    'UserName': 'xxxxx', 
    'Password': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*SHPGJ+58GYuA2cz5zmAzYg==', 
    'Key': 'xxxxxxxx'}]}
    
Encrypted data:
    We using 'Key' to encrypt the data
    
"""


def encrypt_data(*args) -> str:
    """
    Encrypt the data using the key
    """
    _secret_key = ''
    if args:
        data = args[0]
        print(f"Data to be encrypted: {data}")
        #     if data is int, float, None, bool then print the data is not supported
        if isinstance(data, int) or isinstance(data, float) or \
                isinstance(data, bool) or isinstance(data, str):
            print("Data type not supported")
            return None
        #     if data have ['data'][0]['Key'] and it is string then encrypt the data
        elif isinstance(data, dict) and data['data'][0]['Key'] and isinstance(data['data'][0]['Key'], str):
            print("Data is supported")
            # Todays date only as a string
            secret_key = data['data'][0]['Key']
            today = datetime.datetime.now().strftime("%d")
            print(f"Today's date: {today}")
            for i in range(0, len(secret_key)):
                _secret_key = _secret_key + chr(ord(secret_key[i]) + int(today))
            # print(f"Secret key: {_secret_key}")
            return _secret_key
    else:
        print("No data to encrypt")
        return None


# testing the function
# test_data = ["Test", json_data]
# for data in test_data:
#     encrypt_data(data)
