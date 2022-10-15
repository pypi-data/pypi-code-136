import os
from datetime import datetime
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential


class OneDrive:

    def __init__(self, username, password, url_user):
        self.username = username,
        self.password = password,
        self.url_user = url_user

    # CONNECT USER
    def auth(self):

        conn = ClientContext(self.url_user).with_credentials(
            UserCredential(user_name = self.username[0], password = self.password[0])
        )

        return conn



    # GET ALL FOLDERS WITH FROM ROOT OR FOLDER_NAME
    def get_folders_endpoint(self, folder_name : str = ""):

        conn = self.auth()
        
        list_source = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}")
        folders = list_source.folders
        conn.load(folders)
        conn.execute_query()

        return folders



    # GET FILES FROM FOLDER
    def get_files_from_folder(self, folder_name = ""):

        conn = self.auth()
        
        list_source = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}")
        files = list_source.files
        conn.load(files)
        conn.execute_query()

        return files





    # DOWNLOAD FILE BY URL
    def download_file(self, file_url : str):
        
        filename = file_url.split("/")[-1]

        dir_name =  f"{ datetime.now().strftime('%d-%m-%Y') }-datas"

        try:
            os.mkdir(dir_name)

        except FileExistsError:
            pass

        file_path = os.path.abspath( os.path.join(dir_name, filename) )
        conn = self.auth()

        with open(file_path, "wb") as local_file:
            file = conn.web.get_file_by_server_relative_url(file_url)
            file.download(local_file)
            conn.execute_query()

        print(f"Fichier { filename } téléchargé avec succès !")




    # DOWNLOAD FILES FROM FOLDER
    def download_files_from_folder(self, folder_name : str = ""):

        files = self.get_files_from_folder(folder_name)

        for file in files :

            self.download_file(file.serverRelativeUrl)






    # UPLOAD FILE 
    def upload_file_to_onedrive(self, path_file : str, folder_name : str = ""):

            file_name = path_file.split('/')[-1]
            conn = self.auth()

            target_folder = conn.web.get_folder_by_server_relative_url(f"Documents/{folder_name}")

            with open(file_name, 'rb') as content_file:

                file_content = content_file.read()

                target_folder.upload_file(file_name, file_content).execute_query()

            print(f"Le fichier {file_name} chargé avec succès !")






    # UPLOAD FILES ON LOCAL DIRECTORY
    def upload_files_to_onedrive(self, folder_name_local : str = "./", folder_name_onedrive: str = ""):

        folder_name_local = os.listdir(f"{ folder_name_local }")

        # files = [file for file in folder_name_local if (not os.path.isdir(file) and not os.path.ismount(file)) ]

        files = [f for f in folder_name_local if os.path.isfile(folder_name_local+'/'+f)] 

        for file in files:

            self.upload_file_to_onedrive( file, folder_name_onedrive)