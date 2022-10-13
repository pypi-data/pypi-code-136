import requests


def get_character_data(data, timestamp, api_key, hash=None, characters=[]):
    ''' This function is taking all the characters as parameter. Then it is looping 
        through each character and adding the data to the dictionary'''

    try:
        for letter in characters:
            for offset in range(3):
                params = {'ts': timestamp, 'apikey': api_key,
                          'hash': hash, 'limit': 100, 'offset': offset*100}
                res = requests.get('https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=' +
                                   letter, params=params)
                results = res.json()

                for i in results['data']['results']:
                    data['character_name'].append(i['name'])
                    data['event_appearances'].append(i['events']['available'])
                    data['series_appearances'].append(i['series']['available'])
                    data['stories_appearances'].append(
                        i['stories']['available'])
                    data['comics_appearances'].append(i['comics']['available'])
                    data['character_id'].append(i['id'])

        return data
    except:
        print('API or Hash keys are missing')
