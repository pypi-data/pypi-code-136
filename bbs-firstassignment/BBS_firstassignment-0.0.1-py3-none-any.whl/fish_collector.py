import requests


def getSpeciesList():
    fish_list = []
    api_url = "https://www.fishwatch.gov/api/species"
    response = requests.get(api_url, timeout=5)
    for elem in response.json():
        elemDict = {}
        elemDict["name"] = elem["Species Name"]
        elemDict["path"] = elem["Path"][10:]
        fish_list.append(elemDict)
    return fish_list

def getInformSelectSpecies(name):
    api_url = "https://www.fishwatch.gov/api/species/"+name
    response = requests.get(api_url, timeout=5)
    return response.json()
