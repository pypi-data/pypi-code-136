from StevenTricks.netGEN import randomheader
from os.path import isdir
from CPL import warehousedircheck

whsename = 'warehouse'

if isdir(whsename) is False:
    warehousedircheck(whsename)