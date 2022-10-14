from bs4 import BeautifulSoup as bs
from rats.core.RATS_CONFIG import packagepath, topopath


def extractscale(datasheet_identifier, edblist):
    edbs = [i for i in edblist]
    import os

    # for filename in os.listdir(str(packagepath / topopath)):
        # if 'topology' in filename.lower() and 'xml' in filename:
        #     topofile = filename

    # print(str(packagepath / topopath / topofile))
    # with open(str(packagepath / topopath / topofile), 'r') as f:
    #     content = f.readlines()
    #     content = "".join(content)
    #     soup = bs(content, 'lxml')

    # device = soup.find('de:device', {'instancename': instanceName})
    description = {}
    units = {}
    minimum = {}
    maximum = {}

    with open(str(packagepath / topopath / f'DeviceEndpoint_{datasheet_identifier}.xml'), 'r') as f:
    # with open(r'C:\Users\uksayr\Downloads\DeviceEndpoint_4-2-3.xml', 'r') as f:
        content = f.readlines()
        content = "".join(content)
        soup = bs(content, 'lxml')

    for edb in edbs:
        addr42 = soup.find('is:interface', {'name': 'RATS'})
        data = addr42.find('is:readback', {'id': edb})
        description[edb] = data['description']
        units[edb] = data['unit']
        minimum[edb] = int(data['minvalue'])
        maximum[edb] = int(data['maxvalue'])

    scalingfactors = dict(descriptions=description, units=units, minimum=minimum, maximum=maximum)
    print('scaling factors determined')

    return scalingfactors


def arbfunc(netid, e):
    output = extractscale(netid, e)
    return output

