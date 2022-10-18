
from cloudvision.cvlib.exceptions import InputNotFoundException

try:
    raise InputNotFoundException(["potato"], "asob")
except InputNotFoundException as e:
    print(e)
