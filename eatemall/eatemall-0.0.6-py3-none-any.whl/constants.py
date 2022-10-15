import random

def populate_colors(n):
    colors = []
    for i in range(n):
        colors.append([random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)])
    return colors

FPS = 30
SERVER_IP = "192.168.1.2"
SERVER_PORT = 12345
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800
COLOR = populate_colors(10)




