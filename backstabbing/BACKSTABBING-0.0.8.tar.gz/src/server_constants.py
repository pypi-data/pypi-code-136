import socket

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

#Define pygame constants to be used and ALTERED
ROOM_SIZE = 600
PLAYER_RADIUS = 25
ROUND_TIME = 120
FPS = 30
TOTAL_PLAYERS = 2


#Maximum number of players allowed is 4!
if TOTAL_PLAYERS > 4:
    TOTAL_PLAYERS = 4