#%%
from os.path import expanduser

import requests
import json

# Get key from json file
home = expanduser("~")
with open(f'{home}/org-one/api_key.json') as f:
    api_key = json.load(f)['apilayer_key']


#%%
payload = {}
headers= {
    "apikey": f"{api_key}"
}
#%%
# parse args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("query", help="query to search")
args = parser.parse_args()
#%%
def main():
    q = args.query
    url = f"https://api.apilayer.com/dymt/did_you_mean_this?q={q}"
    response = requests.request("GET", url, headers=headers, data = payload)
    json = response.json()
    if json['is_modified']:
        print(f"Did you mean \"{json['result']}\"?")
    else:
        return
    #%%
if __name__ == '__main__':
    main()
