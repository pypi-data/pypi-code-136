from collections import OrderedDict
import json
import os


class BrazilLocations:
    def __init__(self):
        this_dir, this_filename = os.path.split(__file__)
        json_path = os.path.join(this_dir, "states_and_cities_10_22.json")
        self._locations = OrderedDict()
        self._locations = json.load(open(json_path))

    @property
    def list_states(self):
        return sorted([self._locations[s]['abbr'] for s in self._locations])

    @property
    def list_all_cities(self):
        cities = []

        for state in self._locations:
            for city in self._locations[state]['cities']:
                cities.append(city['name'])
        
        return cities

    @property
    def dict_states(self):
        d = {}
        for s in self._locations:
            d[self._locations[s]['abbr']] = {'code': self._locations[s]['code'], 'name': self._locations[s]['name'] }
        return d

    def list_cities(self, abbr=None, code=None):
        if code is None and abbr is None:
            return

        cities = 'Not found'

        states_codes = {self._locations[s]['code']: s for s in self._locations.keys()}
        
        if code != None:
            if code in states_codes:
                cities = [c['name'] for c in self._locations[states_codes[code]]['cities']]

        if abbr != None:
            if abbr.upper() in self._locations.keys():
                cities = [c['name'] for c in self._locations[abbr.upper()]['cities']]

        return cities

    def get_city(self, name=None):
        if name is None:
            return

        for state in self._locations:
            for city in self._locations[state]['cities']:
                if city['name'].upper() == name.upper():
                    return city

    def _get_state_by_abbr(self, abbr):
        state = None
        for u in self._locations:
            if self._locations[u]['abbr'] == abbr:
                state = self._locations[u]
                break
        return state


br_locale_info = BrazilLocations()
