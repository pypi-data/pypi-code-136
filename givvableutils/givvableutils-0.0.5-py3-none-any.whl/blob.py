import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings


def initialize_storage_account(storage_account_name, storage_account_key):
    try:  
        global service_client
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
    
    except Exception as e:
        print(e)
        
def list_directory_contents(container, directory):
    try:
        
        file_system_client = service_client.get_file_system_client(file_system=container)

        paths = file_system_client.get_paths(path=directory)

        for path in paths:
            print(path.name)

    except Exception as e:
        print(e)
        
def create_file_system(container):
    try:
        global file_system_client

        file_system_client = service_client.create_file_system(file_system=container)
    
    except Exception as e:
        print(e)
        
        
def create_directory(container, directory):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container)
        file_system_client.create_directory(directory)
    
    except Exception as e:
        print(e)

        
def rename_directory(container, old_directory_name, new_directory_name):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container)
        directory_client = file_system_client.get_directory_client(old_directory_name)

        directory_client.rename_directory(new_name=directory_client.file_system_name + '/' + new_directory_name)
    except Exception as e:
        print(e)
        

def delete_directory(container, directory):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container)
        directory_client = file_system_client.get_directory_client(directory)

        directory_client.delete_directory()
    except Exception as e:
        print(e)
    
    
def upload_file_to_directory(container, directory, online_file_name, local_file_path):
    try:

        file_system_client = service_client.get_file_system_client(file_system=container)

        directory_client = file_system_client.get_directory_client(directory)
        
        file_client = directory_client.create_file(online_file_name)
        local_file = open(local_file_path,'r')

        file_contents = local_file.read()

        file_client.append_data(data=file_contents, offset=0, length=len(file_contents))

        file_client.flush_data(len(file_contents))

    except Exception as e:
        print(e)
        

'''For uploading large files'''
def upload_file_to_directory_bulk(container, directory, online_file_name, local_file_path, encoding='utf-8', overwrite=True):
    try:

        file_system_client = service_client.get_file_system_client(file_system=container)

        directory_client = file_system_client.get_directory_client(directory)
        
        file_client = directory_client.get_file_client(online_file_name)

        local_file = open(local_file_path, 'r', encoding=encoding)

        file_contents = local_file.read()

        file_client.upload_data(file_contents, overwrite=overwrite)

    except Exception as e:
        print(e)


def download_file_from_directory(container, directory, online_file_name, local_file_path):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container)

        directory_client = file_system_client.get_directory_client(directory)
        
        local_file = open(local_file_path,'wb')

        file_client = directory_client.get_file_client(online_file_name)

        download = file_client.download_file()

        downloaded_bytes = download.readall()

        local_file.write(downloaded_bytes)

        local_file.close()

    except Exception as e:
        print(e)


'''For uploading large files'''
def upload_file_buffer_to_directory_bulk(container, directory, online_file_name, file_buffer, overwrite=True):
    try:

        file_system_client = service_client.get_file_system_client(
            file_system=container)

        directory_client = file_system_client.get_directory_client(directory)

        file_client = directory_client.get_file_client(online_file_name)

        file_client.upload_data(file_buffer, overwrite=overwrite)

    except Exception as e:
        print(e)
