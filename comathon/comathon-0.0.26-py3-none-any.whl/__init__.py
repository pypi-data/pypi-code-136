# import requests

# from .cmt_test_obsolete import *
from .cmt_exchange import *
from .cmt_quotation import *
import socket

print("Comathon Module Imported, GAZUA")

## Check if the code is being run from the server of from the personal computer

## Create API upbit instances here? Then how can we check if someone cut out the connection or added a one?

# def code_status():
    
#     is_server = False

#     my_IP = socket.gethostbyname(socket.gethostname())
#     print("my IP address : ", my_IP)

#     server_IP = '121.137.95.97'
#     dev_IP = '175.207.155.229'
#     dev_IP_laptop = '192.168.213.94'

#     if my_IP == server_IP or my_IP == dev_IP_laptop:
#         print("The code is being run by the server or Jeong's computer")
#         is_server = True
    
#     else:
#         print("The code is being run on a personal computer")
#         print("is_server variable : ", is_server)

#     return is_server

# code_status()


