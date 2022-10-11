import os
import argparse
import json

def type_secret(dct):
	if 'type' in dct:
		if dct['type']=='secret_file':
			with open(dct['path']) as f:
				t_secret=json.load(f)
			return type_secret
	return dct

def get_config():
  parser=argparse.ArgumentParser(description='PVZ script')
  parser.add_argument('-c',help='config file in JSON')
  parser.add_argument('-s',help='config string in JSON')
  args=parser.parse_args()
  settings={}
  settings_string=''
  if args.c == None:
    settings_file='./config/default.json'
  else:
    settings_file = args.c
  if args.s != None:
    settings_string = args.s
  
  with open(settings_file) as f:
    settings=json.load(f,object_hook=type_secret)
  if settings_string !='':
    settings.update(json.loads(settings_string))
  return settings