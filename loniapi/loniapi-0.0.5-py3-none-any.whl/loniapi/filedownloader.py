import requests     # to make API calls
import configparser # to parse .loniAPIConfig for email and password
import os           # to get and construct absolute paths
import pandas       # to save file list and file metadata

class LoniApi:
    def __init__(self):
        self._set_null_instance_variables()

    def _set_null_instance_variables(self):
        self._auth_key = None
        self.group_id = None
        self.loni_files = None

    # parse email and password from .loniApiConfig file in home directory
    # and return credentials in a dictionary
    def _get_credentials(self, group_id):
        _config = configparser.ConfigParser()
        _config.read(os.path.join(os.path.expanduser('~'), '.loniApiConfig'))
        return dict([('email', _config.get(group_id, 'email')), ('password', _config.get(group_id, 'password'))])

    # Use the 'requests' library to make API call and 
    # return the result string containing the auth key
    def login(self, group_id):
        if self._auth_key is None:
            credentials = self._get_credentials(group_id)   #get credentials from .loniApiConfig
            headers = {"Content-Type" :"text/plain"}
            payload = {'get': 'authorize', 'email': credentials['email']}
            data = credentials['password']
            output = requests.post("https://downloads.loni.usc.edu/download/data/ampad?", headers = headers, params = payload, data = data)
            login_result = output.json()[0]
            if (login_result['status'] == "OK"):
                self._auth_key = login_result["authorization key"]
                self.group_id = group_id
                print("Log-in successful")
            else:
                print(login_result["status"]) #BAD_PASSWORD, ACCESS_DENIED, or UNKNOWN_USER
    
    def logout(self):
        self._set_null_instance_variables()

    def get_LONI_files(self):
        if self._auth_key is None:
            raise Exception("To download file, please log-in first")
        if self.loni_files is None:
            url = "https://downloads.loni.usc.edu/download/data/{}?get=list".format(self.group_id)
            resp = requests.get(url).json()
            self._create_LONI_files_dataframe(resp)
        return self.loni_files

    def _create_LONI_files_dataframe(self, jsonResponse):
        json_list = list(jsonResponse)
        self.loni_files = pandas.DataFrame(
            columns = ['id', 'name', 'description', 'version', 'isLatest']
        )
        for blob in json_list:                
            row =   [blob['id'], blob['name'], blob['description'], 
                    blob['version'], blob['isLatest']]
            self.loni_files.loc[len(self.loni_files.index)] = row


    def download_LONI_file(self, file_id, downloadLocation = os.getcwd(), version = None):
        if self._auth_key is None:
            raise Exception("To download file, please log-in first")

        # Make HTTP request
        headers = {"Authorization" :"Bearer {}".format(self._auth_key)}
        file_info = {'id': file_id}
        if (version is not None):
            file_info['version'] = version
        resp =  requests.post(
                "https://downloads.loni.usc.edu/download/data/ampad?", 
                headers = headers, 
                params = file_info)

        # Save file content as a file in the designated di
        file_url = resp.url
        file_name = file_url[(file_url.rindex('/') + 1):]
        file_path = os.path.join(downloadLocation, file_name)
        with open(file_path, 'wb') as f: 
            f.write(resp.content)
        return file_path

    # return the name of the file that loni will download given id
    def get_LONI_file_name(self, file_id, version = None):
        if self._auth_key is None:
            raise Exception("To download file, please log-in first")
        headers = {"Authorization" :"Bearer {}".format(self._auth_key)}
        file_info = {'id': file_id}
        if (version is not None):
            file_info['version'] = version
        resp = requests.post("https://downloads.loni.usc.edu/download/data/ampad?", headers = headers, params = file_info)
        file_url = resp.url
        file_name = file_url[(file_url.rindex('/') + 1):]
        return file_name

    # Future functions that may be useful for users

    # TODO: get whether file with name is latest. This depends on the accuracy
    # of loni's 'isLatest' field

    # get version

    # get a more possible recent version of this file