import socket
from server_constants import *

class Connection():
    '''A socket connection class to be used as a server'''
    def __init__(self,IP_ADDR):
        '''Initailzation of the Connection class'''
        self.encoder = 'utf-8'
        self.header_length = 10

        #Create a socket, bind, and listen
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((IP_ADDR, HOST_PORT))
        self.server_socket.listen()