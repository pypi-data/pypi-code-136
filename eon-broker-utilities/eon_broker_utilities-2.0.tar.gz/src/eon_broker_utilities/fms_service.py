from dataclasses import replace
import os
from typing import Any
import requests
import json

class ManageFiles():
    def __init__(self, fms_config_variables):
        # Getting FMS API host ip address
        self.fms_host = fms_config_variables['FMS_HOST']
        # Getting FMS API PORT
        self.fms_port = fms_config_variables['FMS_PORT'] 
        # Setting FMS API endpoint
        self.fms_url  = f"{self.fms_host}:{self.fms_port}"
    
    # This function is used to download file from FMS API
    # it takes file key which will be used to get the file from the FMS API
    # and the location where the file will be stored in
    def download_file(self, file_key, base_path):
        url = f"http://{self.fms_url}/{file_key}"
        try:
            # Setting the url for the file by combining FMS API base url and the file key
            
            # Sending get request to FMS API 
            with requests.get(url, stream=True) as response:
                # Retrun error if happened during HTTP request
                
                # for i in response.iter_lines():
                #         download_response += str(i)
                response.raise_for_status()
                
                # Getting file extension from request headers
                file_extention = response.headers['x-ext'].replace('.','')
                # Setting file storage location using file key as the name of the saved file
                file_location = os.path.join(base_path,f"{file_key}.{file_extention}")
                # Writing recieved chuncks from the get request
                with open(file_location, 'wb') as file:
                    # Itterating through the recieved chuncks to be writtien to the created file
                    for chunk in response.iter_content(chunk_size=1024): 
                        file.write(chunk)
                # Closing get request after finishing download
                
                response.close()
                
                
            # Return success message
            return 'File Downloaded Successfully', file_key, file_extention, True
        except Exception as err:
            response = b''
            for response_bytes in requests.get(url).iter_lines():
                        response += response_bytes
            response = json.loads(response.decode('utf8').replace("'", '"'))
            response = response["message"]
            return response, 'Error', 'Error', False

    # This function is used to upload files to FMS API 
    # it takes file key(to be sent to FMS API), name(to be upload from the hosting machine)
    # extension of the targeted file, base path which will be the location of the target file,
    # file group and the name creater of the file
    def upload_file(self, file_key, file_name, file_extention, base_path, group = None, created_by = None):
        response = ''
        try:
            # Setting the url for the file by combining FMS API base url and the file key
            url = f"http://{self.fms_url}/{file_key}"
            # Setting the location of the file to be uploaded
            file_location = os.path.join(base_path,f"{file_name}.{file_extention}")
            # Setting the header of the post request, file extension must be sent in the headers as same as the original extesion of the file
            headers = {'content-type': 'application/octet-stream',
                        'x-ext': file_extention, 'x-group': group, 'x-createdby': created_by}
            # Sending post request request to start upload the file
            file_request = requests.Session()
            # Opening the file to send chuncks of the targeted file
            with open(file_location, 'rb') as file:
            # Sending the file using post request, parametrs: file (opened targeted file) ,
            # headers: preset headers, stream = True for stream upload
                
                with requests.post(url, file, headers=headers, stream=True) as req:
                    for i in req.iter_lines():
                        response += str(i)

            
            # Closing post request after finishing upload
            file_request.close()
            # Return success message
            return "File Uploaded Successfully", True
        except Exception as err:
            response = err
            return response, False
        
    # This function is to delete the file locally, not from the FMS API (only for cleaning the storage\)
    def delete_file(self, file_key, ext, base_path): 
        # Removing the file using os remove and sending the bath of the targeted file
        os.remove(os.path.join(base_path,f"{file_key}.{ext}"))
        # Return success message
        return f"File Deleted Successfully {file_key}.{ext}"


 