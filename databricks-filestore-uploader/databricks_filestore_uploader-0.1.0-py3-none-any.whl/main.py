#!/usr/bin/env python
#===================================
# <company> | <team>
# Databricks FileStore Uploader
#
#   - Isaac Yep
#===================================
mainDocString = '''
This is a convenience/efficiency tool for uploading local files to filestore while specifying folder structure quickly.
Each local source folder can be enumerated and given it's own FileStore destination path.'''

#---Dependencies---------------
# stdlib
from sys import argv, exit, getsizeof
from typing import List
from subprocess import run
# custom modules
from toolchain.option_utils import usageMessage, checkListOverlap, verifyOption, getOptionVal, stripOptionVals
from toolchain.filestore_utils import upload_to_filestore
# 3rd party
try:
  from yaml import safe_load, YAMLError
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)

#---Parameters-----------------
userArgs = argv[1:]
minArgs  = 0
maxArgs  = 2
options  = {
  'help' : ['-h', '--help'],
}

#---Entry----------------------
def main():
  ## Invalid number of args
  if len(userArgs) < (minArgs) or len(userArgs) > (maxArgs):
    usageMessage(f"Invalid number of options in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Invalid option
  if (len(userArgs) != 0) and not (verifyOption(userArgs, options)):
    usageMessage(f"Invalid option(s) entered in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Help option
  if checkListOverlap(userArgs, options['help']):
    print(mainDocString, end='')
    usageMessage()
    exit(0)
  else:
    with open(f"input.yml", 'r') as rawInput:
      inputDict      = safe_load(rawInput)
      databricksHost = inputDict['host']
      accessToken    = inputDict['token']
      payloadDict    = inputDict['payloads']
      for k,v in payloadDict.items():
        upload_to_filestore(
          k,
          f"dbfs:/FileStore/{v}/",
          {'Authorization': f"Bearer {accessToken}"},
          f"{databricksHost}/api/2.0"
        )
    exit(1)


#---Exec-----------------------
if __name__ == "__main__":
    main()
