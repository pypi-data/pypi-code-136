import os
import requests
import json

def get_access_token(creds):
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth_response = requests.post(os.environ['CODA_AUTH_SERVICE_TOKEN_ENDPOINT_URL'], data=creds,headers=headers)
    return json.loads(auth_response.text)['access_token']

def execute_query(service, action, sites, query, access_token):
    
    headers = {'Authorization': 'Bearer ' + access_token }
    data_response = requests.get(os.environ['CODA_HUB_API_URL'] + 
      '/' + service + '/' + action + '?sites=' + (','.join(sites)), 
                                 json=query,headers=headers)

    data = json.loads(data_response.text)[1][0]['results']

    return data