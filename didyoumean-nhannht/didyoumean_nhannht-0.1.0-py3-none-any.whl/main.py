#%%
from os.path import expanduser

import requests
import json

# Get key from json file
home = expanduser("~")
with open(f'{home}/org-one/api_key.json') as f:
    api_key = json.load(f)['apilayer_key']


#%%
import click
payload = {}
headers= {
    "apikey": f"{api_key}"
}
@click.command()
@click.option('--q', prompt='Your query', help='The query you want to check.')
def main(q):
    url = f"https://api.apilayer.com/dymt/did_you_mean_this?q={q}"
    response = requests.request("GET", url, headers=headers, data = payload)
    json = response.json()
    if json['is_modified']:
        print(f"Did you mean \"{json['result']}\"?")
    else:
        return



#%%
