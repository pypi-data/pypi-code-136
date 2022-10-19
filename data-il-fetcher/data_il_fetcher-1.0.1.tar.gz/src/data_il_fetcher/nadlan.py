import json

import requests


def load_page_from_nadlan_impl(label, city_id, page):
    payload = {
        "MoreAssestsType": 0,
        "FillterRoomNum": 0,
        "GridDisplayType": 0,
        "ResultLable": label,
        "ResultType": 1,
        "ObjectID": str(city_id),
        "ObjectIDType": "text",
        "ObjectKey": "UNIQ_ID",
        "DescLayerID": "SETL_MID_POINT",
        "Alert": None,

        "Gush": "",
        "Parcel": "",
        "showLotParcel": True,
        "showLotAddress": True,
        "OriginalSearchString": label,
        "MutipuleResults": False,
        "ResultsOptions": None,
        "CurrentLavel": 2,
        "Navs": [
            {

            }
        ],
        "QueryMapParams": {
            "QueryToRun": None,
            "QueryObjectID": str(city_id),
            "QueryObjectType": "number",
            "QueryObjectKey": "SETL_CODE",
            "QueryDescLayerID": "KSHTANN_SETL_AREA",
            "SpacialWhereClause": None
        },
        "isHistorical": True,
        "PageNo": page,
        "OrderByFilled": "DEALDATETIME",
        "OrderByDescending": True,
        "Distance": 0
    }

    headers = {'Connection': 'keep-alive',
               'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
               'Accept': 'application/json, text/plain, */*',
               'mainsite_version_commit': '3376126e2fad3570e3a7cd8102badd16e5644759',
               'mobile-app': 'false',
               'sec-ch-ua-mobile': '?0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',
               'sec-ch-ua-platform': '"Linux"',
               'Origin': 'https://www.nadlan.gov.il',
               'Sec-Fetch-Site': 'same-site',
               'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Dest': 'empty',
               'Referer': 'https://www.nadlan.gov.il/',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'en-US,en;q=0.9'}

    with requests.post("https://www.nadlan.gov.il//Nadlan.REST/Main/GetAssestAndDeals", json=payload,
                       headers=headers) as r:
        return r.text, r.status_code


def load_page_from_nadlan(args):
    label = args['label']
    city_id = int(args['city_id'])
    page = int(args['page'])
    res = {}
    try:
        text, code = load_page_from_nadlan_impl(label, city_id, page)
        res['code'] = code
        if code == 200:
            res['data'] = json.loads(text)
        else:
            res['data'] = None
    except:
        res['code'] = -1
        res['data'] = None
    return res
