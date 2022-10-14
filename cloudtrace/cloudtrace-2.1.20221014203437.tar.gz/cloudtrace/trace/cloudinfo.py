import json
import os.path
import platform
import subprocess

import requests

def isgoogle():
    # Check if Google
    r = requests.get('http://169.254.169.254/computeMetadata/v1/instance/id', headers={'Metadata-Flavor': 'Google'})
    if r.ok:
        vmid = r.text
        r = requests.get('http://169.254.169.254/computeMetadata/v1/instance/zone', headers={'Metadata-Flavor': 'Google'})
        if r.ok:
            zone = r.text.rpartition('/')[-1]
        return {'cloud': 'gcp', 'vmid': vmid, 'region': zone}
    return False

def isaws():
    r = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document', headers={'Metadata': 'true'})
    if r.ok:
        j = r.json()
        region = j['availabilityZone']
        vmid = j['instanceId']
        return {'cloud': 'aws', 'vmid': vmid, 'region': region}
    return False

def isazure():
    r = requests.get('http://169.254.169.254/metadata/instance?api-version=2021-02-01', headers={'Metadata': 'True'})
    if r.ok:
        j = r.json()
        region = j['compute']['location']
        vmid = j['compute']['vmId']
        # region = j['location']
        # vmid = j['vmId']
        return {'cloud': 'azure', 'vmid': vmid, 'region': region}
    return False

# res = {'cloud': 'cloud', 'vmid': 'vmid', 'region': 'region'}

# if os.path.exists('config.json'):
#     with open('config.json') as f:
#         res = json.load(f)
# else:


def get_cloud_info():
    for func in [isaws, isazure, isgoogle]:
        res = func()
        if res:
            break
    if res:
        hostname = f'{res["cloud"]}_{res["region"]}_{res["vmid"]}'
        print(f'Found cloud metadata: {hostname}')
    else:
        hostname = platform.node()
        print(f'Unable to find any cloud metadata. Using hostname: {hostname}')
    return hostname

