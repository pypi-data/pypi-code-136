# # ******************************************************************************
# #  Copyright (c) 2020. Tracker wave Pvt Ltd.
# # ******************************************************************************
#

import requests


def get(url, auth, data=None):
    if data:
        response = requests.get(url, headers=auth)
    else:
        response = requests.get(url, headers=auth)
    return response.json()
