#!/usr/bin/env python

import typing
from requests import Session
from json import dumps
import os
from base64 import b64encode

# Internal Utility: hit api on host dbfs
def perform_query(path, headers, url, data={}):
  session = Session()
  resp = session.request('POST', url + path, data=dumps(data), verify=True, headers=headers)
  return resp.json()

# Internal Utility: make directories in dbfs filestore
def mkdirs(path, headers, url):
  _data = {}
  _data['path'] = path
  return perform_query('/dbfs/mkdirs', headers=headers, url=url, data=_data)

# Internal Utility: create or overwrite file
def create(path, overwrite, headers, url):
  _data = {}
  _data['path'] = path
  _data['overwrite'] = overwrite
  return perform_query('/dbfs/create', headers=headers, url=url, data=_data)

# Internal Utility: add dbfs block
def add_block(handle, data, headers, url):
  _data = {}
  _data['handle'] = handle
  _data['data'] = data
  return perform_query('/dbfs/add-block', headers=headers, url=url, data=_data)

# Internal Utility: close dbfs connection
def close(handle, headers, url):
  _data = {}
  _data['handle'] = handle
  return perform_query('/dbfs/close', headers=headers, url=url, data=_data)

# Internal Utility: upload file
def put_file(src_path, dbfs_path, overwrite, headers, url):
  handle = create(dbfs_path, overwrite, headers=headers, url=url)['handle']
  print("Putting file: " + dbfs_path)
  with open(src_path, 'rb') as local_file:
    while True:
      contents = local_file.read(2**20)
      if len(contents) == 0:
        break
      add_block(handle, b64encode(contents).decode(), headers=headers, url=url)
    close(handle, headers=headers, url=url)

# Utility: upload to dbfs filestore
def upload_to_filestore(
  local_source_dir: str,
  dbfs_target_dir : str,
  request_headers : dict,
  host_endpoint   : str,
  ):
  '''Takes source folder path, target dbfs folder path, request header dictionary and api endpoint and executes upload. Returns nothing.'''
  mkdirs(path=dbfs_target_dir, headers=request_headers, url=host_endpoint)
  files = [f for f in os.listdir(local_source_dir) if os.path.isfile(f"{local_source_dir}/{f}")]
  for f in files:
    target_path = dbfs_target_dir + f
    resp = put_file(src_path=f"{local_source_dir}/{f}", dbfs_path=target_path, overwrite=True, headers=request_headers, url=host_endpoint)
    if resp == None:
      print("Success")
    else:
      print(resp)
