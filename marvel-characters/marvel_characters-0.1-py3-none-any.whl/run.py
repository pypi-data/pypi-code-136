import os
from dotenv import load_dotenv
from pathlib import Path
from functions import create_character_df, filter_characters
import hashlib

# getting keys from .env 
path = Path('.')/'.env'
load_dotenv()
private_key = os.getenv('private_key')
public_key = os.getenv('public_key')

#asking user if they want to input their own private key or want to use the fetched env variable private_key
flag_private_key = input("If you want to enter private key manually, enter True. To use the key saved in local file, press Enter.\n")
if flag_private_key=='True':
    privateKey = input("Enter private key\n")
else:
    privateKey = private_key

#setting perameters necessary for calling the API
publicKey = public_key
ts = 1
hash = hashlib.md5((str(ts)+privateKey+publicKey).encode()).hexdigest()

#asking user for starting letter to call the API and creating character dataframe
nameStartWith = input("Input the starting letter of names of characters you want\n")
char_df = create_character_df(input_apikey=publicKey, input_hash=hash, nameStartWith=nameStartWith)
print(char_df)

#asking user for filtering parameters and printing filtered dataframe
col = input("enter the column name that you want to filter with\n")
condition = input("enter the filter condition - for text column, enter starts_with.\
    for integer columns, enter equal_to, less_than or greater_than\n")
value = input("enter the filter value\n")
filtered_df = filter_characters(df=char_df, column_name=col, filter_condition=condition, filter_value=value)
print(filtered_df)
