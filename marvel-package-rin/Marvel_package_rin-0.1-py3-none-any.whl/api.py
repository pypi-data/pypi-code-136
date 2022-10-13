import requests

def api_call(namestartWith, web_url, hash_val="None", publicKey="None", ts="None"):
    if hash_val=='None':
        raise Exception('Hash value not provided')
    if publicKey=='None':
        raise Exception('Public Key not provided')
    else:
        parameters = {
                    'ts' : 2,
                    'apikey': publicKey,
                    'hash' : hash_val,
                    'nameStartsWith': namestartWith,
                    'limit' : 100
            }
        headers = {'Content-Type': 'application/json'}
        response = requests.get(web_url, headers=headers, params=parameters, verify=False)
        response.raise_for_status()
        results = response.json()

        return results