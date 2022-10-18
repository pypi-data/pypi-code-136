import requests     # to make API calls
import configparser # to parse .loniAPIConfig for email and password
import os           # to get and construct absolute paths
import pandas       # to save file list and file metadata

class LoniApi:
    def __init__(self):
        """
        Initializes global variables
        """
        self._set_null_instance_variables()

    def _set_null_instance_variables(self):
        self._auth_key = None
        self.group_id = None
        self.loni_files = None

    def _get_credentials(self, group_id):
        """
        parse email and password from .loniApiConfig file in home directory
        Args:
            group_id (str): group id provided by LONI/IDA
        Returns:
            dict: credentials
        """
        _config = configparser.ConfigParser()
        _config.read(os.path.join(os.path.expanduser('~'), '.loniApiConfig'))
        return dict([('email', _config.get(group_id, 'email')), ('password', _config.get(group_id, 'password'))])

    def login(self, group_id):
        """
        Use the 'requests' library to make the API call for logging in
        Print whether log-in attempt was successful
    
        Args:
            group_id (str): group id provided by LONI/IDA
    
        Returns:
            dict: credentials
        """
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
        """
        Log out by setting all credential variables to None
        """
        self._set_null_instance_variables()

    def get_LONI_files(self):
        """
        Return a pandas dataframe containing information (id, name, 
        description, version, isLatest) about all files 
        associated with the group_id. 
        """
        if self._auth_key is None:
            raise Exception("To download file, please log-in first")
        if self.loni_files is None:
            url = "https://downloads.loni.usc.edu/download/data/{}?get=list".format(self.group_id)
            resp = requests.get(url).json()
            self._create_LONI_files_dataframe(resp)
        return self.loni_files

    def _create_LONI_files_dataframe(self, jsonResponse):
        """
        Store file information returned by the IDA file API in
        a pandas dataframe
    
        Args:
            jsonResponse (str): list of json blobs returned by the IDA file API
            where each blob contains information about a file
        """
        json_list = list(jsonResponse)
        self.loni_files = pandas.DataFrame(
            columns = ['id', 'name', 'description', 'version', 'isLatest']
        )
        for blob in json_list:                
            row =   [blob['id'], blob['name'], blob['description'], 
                    blob['version'], blob['isLatest']]
            self.loni_files.loc[len(self.loni_files.index)] = row


    def download_LONI_file(self, file_id, downloadLocation = os.getcwd(), version = None):
        """
        Download a file from LONI IDA
    
        Args:
            file_id (str): file id as assigned by LONI/IDA

            downloadLocation(str): Directory where to download the file. 
            Defaults to the current directory.

            version(str): file version. If a specific version is not provided,
            will download the latest version of the file
    
        Returns:
            string: path of newly downloaded file
        """
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

    # # NOTE: The function below aims to provide additional functionality
    # # on top of the current LONI API. It is commented out for now because 
    # # there are still many outstanding questions that we need to ask LONI
    
    # # return the name of the file that loni will download given id
    # def get_LONI_file_name(self, file_id, version = None):
    #     if self._auth_key is None:
    #         raise Exception("To download file, please log-in first")
    #     headers = {"Authorization" :"Bearer {}".format(self._auth_key)}
    #     file_info = {'id': file_id}
    #     if (version is not None):
    #         file_info['version'] = version
    #     resp = requests.post("https://downloads.loni.usc.edu/download/data/ampad?", headers = headers, params = file_info)
    #     file_url = resp.url
    #     file_name = file_url[(file_url.rindex('/') + 1):]
    #     return file_name

    # Future functions that may be useful for users

    # TODO: get whether file with name is latest. This depends on the accuracy
    # of loni's 'isLatest' field

    # get version

    # get a more possible recent version of this file