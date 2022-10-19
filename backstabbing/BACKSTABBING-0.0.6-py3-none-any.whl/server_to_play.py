#Online Multiplayer Game Server

from src.server_connection import *
from src.server_player import *
from src.server_game import *
import sys

def start_server(IP_ADDR=''):
    if(IP_ADDR == ""):
        print("IP Address not provided, quitting the SERVER!")
        sys.exit()
#Start the server
    my_connection = Connection(IP_ADDR)
    my_game = Game(my_connection)

    #Listen for incomming connections
    print("Server is listening for incomming connections...\n")
    my_game.connect_players()

start_server('192.168.1.12')