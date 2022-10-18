def acl(wiz):
    ip = wiz.request.ip()
    
    # uncomment this after set your environment
    # if ip not in ['127.0.0.1', '220.82.71.65']:
    #     wiz.response.abort(401)
