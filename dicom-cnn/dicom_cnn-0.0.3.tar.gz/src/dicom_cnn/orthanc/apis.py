import io
import json
import requests
import numpy

class OrthancApis:
    def __init__(self) -> None:
        self.login = ''
        self.password = ''

    def set_orthanc_server(self, url :str) -> None:
        self.host = url
    
    def set_orthanc_port(self, port :int) ->None:
        self.port = port

    def set_orthanc_credential(self, login: str, password: str):
        self.login = login
        self.password = password

    def get_instance_numpy(self, instance_orthanc_id :str) -> numpy.array:
        response_pixel = requests.get(self.host+'/instances/'+instance_orthanc_id+'/numpy?rescale=true', auth=(self.login, self.password))
        pixels = numpy.load(io.BytesIO(response_pixel.content))
        return pixels

    def get_instance_metadata(self, instance_orthanc_id :str) ->dict:
        response = requests.get(self.host+'/instances/'+instance_orthanc_id+'/tags', auth=(self.login, self.password))
        dicom_metadata = json.loads(response.text)
        return dicom_metadata

    def get_series_infos(self, series_orthanc_id: str) -> dict:
        response = requests.get(self.host+'/series/'+series_orthanc_id, auth=(self.login, self.password))
        series_data = json.loads(response.text)
        return series_data
