import json
from .httputils import flow360ApiPost

def validateJSON(resourceType, config, meshId=None, solverVersion=None):
    body = {
        "jsonConfig": config,
        "version": solverVersion
    }
    if meshId is not None:
        body['meshId'] = meshId

    try:    
        res = flow360ApiPost(f'validator/{resourceType}/validate', body, verbose=False)
    except:
        return
    
    if 'success' in res and res['success'] == True:
        return res
    elif 'success' in res and res['success'] == False:
        print('JSON Validation failed:', res)
        raise ValueError

