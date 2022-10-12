import requests
import pandas as pd

# marvel_char_list function creates a dataframe of Marvel characters
# marvel_char_list has pub_key,hash_obj_str,time_stamp_str as arguments in order
# marvel_char_list also has an argument name_start which can be used to extract charcters starting with particular name


class marvel_char:

    def marvel_char_list(self, pub_key=None, hash_obj_str=None, time_stamp_str=None, name_start=None):
        # Function raises an exception if pub_key, hash_obj_str or time_stamnp_str are not passed as arguments
        if (pub_key == None or hash_obj_str == None or time_stamp_str == None):
            raise Exception("Parmeters not specified correctly")

        url = "http://gateway.marvel.com/v1/public/characters"
        df = []
        range_1 = [0, 100, 200, 300, 400, 500, 600, 700,
                   800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]

        for k in range_1:
            params = {"apikey": pub_key, "ts": time_stamp_str, "hash": hash_obj_str,
                      "nameStartsWith": name_start, "limit": 100, "offset": k}
            response = requests.get(url, params)
            if response.raise_for_status():
                print(response.raise_for_status())
            resp_json = response.json()

            for i in resp_json['data']['results']:
                resp = {'char_id': 0, 'char_name': '', 'events': 0,
                        'series': 0, 'stories': 0, 'comics': 0}
                resp['char_id'] = i['id']
                resp['char_name'] = i['name']
                resp['events'] = i['events']['available']
                resp['series'] = i['series']['available']
                resp['stories'] = i['stories']['available']
                resp['comics'] = i['comics']['available']
                df.append(resp)
            dataframe = pd.DataFrame(df)
        return dataframe
# marvel_char_list function returns a dataframe of marvel characters
