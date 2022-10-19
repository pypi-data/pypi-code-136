# type = forsale|rent
import requests
from .common import get_std_headers
import json


def fetch_yad2_nadlan_for_sale_page(page, city, tp):
    payload = {'city': city, 'forceLoad': 'true', 'page': page}

    try:
        with requests.get(f'https://gw.yad2.co.il/feed-search-legacy/realestate/{tp}',
                          params=payload,
                          headers=get_std_headers('https://www.yad2.co.il/')) as r:
            if r.status_code == 200:
                return r.text, r.status_code
            else:
                return r.url, r.status_code
    except:
        return str(payload), -1


def load_estate(args):
    city = args['city']
    page = args['page']
    tp = args['type']
    ret = {}

    payload, status_code = fetch_yad2_nadlan_for_sale_page(page, city, tp)
    ret['status'] = status_code
    ret['page'] = page
    ret['city'] = city
    if status_code == 200:
        raw_data = json.loads(payload)
        total_pages = raw_data['data']['pagination']['last_page']
        ret['total_pages'] = total_pages
        ret['data'] = []
        if 'data' in raw_data.keys():
            data = raw_data['data']
            if 'feed' in data.keys():
                feed = data['feed']
                if 'feed_items' in feed.keys():
                    ret['data'] = feed['feed_items']
    else:
        ret['url'] = payload

    return ret


# https://www.yad2.co.il/api/item/en2h6jnz/contactinfo?id=en2h6jnz
def fetch_yad2_nadlan_additional_info(url, link, query):
    payload = {query: link}

    try:
        with requests.get(url, params=payload, headers=get_std_headers('https://www.yad2.co.il/')) as r:
            if r.status_code == 200:
                return r.text, r.status_code
            else:
                return r.url, r.status_code
    except Exception:
        return f'{url}?{query}={link}', -1


def load_additional_info(is_contact, args):
    params = args['params']
    ret = {'data': []}
    for p in params:
        ad_number = p['ad_number']
        link = p['link']
        if not is_contact:
            url = "https://gw.yad2.co.il/feed-search-legacy/item"
            query = "token"
        else:
            url = f"https://www.yad2.co.il/api/item/{link}/contactinfo"
            query = "id"
        payload, status_code = fetch_yad2_nadlan_additional_info(url, link, query)
        obj = {'ad_number': ad_number, 'link': link, 'payload': payload, 'status': status_code}
        ret['data'].append(obj)
    return ret
