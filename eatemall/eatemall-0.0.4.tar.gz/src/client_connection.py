import json
import socket
from src.constants import SERVER_IP,SERVER_PORT

class Connection():

    def __init__(self,playerName,IP=""):
        self.playerName = playerName

        if(IP != ""):
            self.ip_addr = IP
        else:
            self.ip_addr = SERVER_IP
            
        self.destination_port = SERVER_PORT
        self.socket_address = (self.ip_addr,self.destination_port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Connect to the client
        self.client_socket.connect(self.socket_address)
        self.client_socket.send(self.playerName.encode())
        self.player_id = self.client_socket.recv(8).decode()

    def send_normal(self,message):

        self.client_socket.send(message.encode())
        data = self.client_socket.recv(32768)
        print(type(data))
        return json.loads(data)

    def send_json(self,message):

        self.client_socket.send(json.dumps(message).encode())
        data = self.client_socket.recv(32768)
        return json.loads(data)

