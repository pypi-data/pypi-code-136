import urllib
import json
import json
import os
import os.path
import time

cache_folder = os.getcwd().split('geo')[0] + 'geo/cache'
# 604800 is on week
max_age = 604800

def get_file_path(name):
    return str(cache_folder) + '/' + str(name) + '.json'
        
def check_age(name):
    if (os.path.getmtime(get_file_path(name)) - time.time()) < -max_age:
        print("Updating " + str(name) + " from server.")
        retrieve_and_cache(name)

def check_cache(name):
    return (os.path.exists(name))

def write_cache(data, file_path):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()
        
def load_cache(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return (data)

def retrieve_and_cache(name):
    
    # Load country data from the worldbank
    # We fetch data from the World Bank
    url = "http://api.worldbank.org/v2/countries?format=json&per_page=304"
    response = urllib.request.urlopen(url)
    codec = response.info().get_param('charset', 'utf8')
    data = json.loads(response.read().decode(codec))

    f = get_file_path(name)
    write_cache(data, f)
    print("Files updated from server")

		