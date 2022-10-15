import pygame
from src.client_connection import Connection
from src.button import Button
from src.constants import *
import sys
import os
import pathlib


def process_time(time):
    """
    This function will convert the time in integer to it's formatted string

    Parameters
        ----------
        time : int
            The current round time counter - Maintained by the server and passed through Game State
    Return
        ----------
        convertedTime : string
            returns the converted time of the current round time counter(Maintained by the server and passed through Game State) into formatted string that is to be displayed on the UI
    """
    minutes = str(time//60)
    seconds = str(time%60)
    if(int(seconds)<10):
        seconds = "0"+seconds
    convertedTime = minutes+":"+seconds
    return convertedTime

def HUD(gameState,player_id,display_window):
    """
    This function will render the information (which is extracted from the GameState) about a client on the pygame display_window

    Parameters
        ----------
        gameState : Dictionary
            This dictionary is received from the server and contains complete information about all the clients connected to the server.
    
        player_id : integer
            The ID of the client whose information is to be fetched from the gameState dictionary. 

        display_window : class<obj>, pygame
            The window that will render all the objects on the screen

    Return
        ----------
        None
    """
    DIR = pathlib.Path().resolve()
    LEADERBOARD_FONT = pygame.font.Font(f".{DIR}\\assets\Facon.ttf",20)
    ROUND_TIME_FONT = pygame.font.Font(f".{DIR}\\assets\Facon.ttf",30)
    SCORE_FONT = pygame.font.Font(f".{DIR}\\assets\Facon.ttf",26)
    
    sorted_by_radius = sorted(gameState["connectedClients"], key=lambda x: gameState["connectedClients"][x]["radius"])
    rev_sorted_players = list(reversed(sorted_by_radius))

    display_window.fill((255,255,255)) 
    
    for food_item in gameState["food_info"]:
        pygame.draw.circle(display_window, food_item[2], (food_item[0], food_item[1]), gameState["food_radius"])
    
    text = ROUND_TIME_FONT.render("Round Time: " + process_time(gameState["cur_time"]), 1, (0,0,0))
    display_window.blit(text,(10,10))

    # draw score
    text = ROUND_TIME_FONT.render("Score: " + str(round(gameState["connectedClients"][player_id]["radius"])),1,(0,0,0))
    display_window.blit(text,(10,15 + text.get_height()))

    title_text = ROUND_TIME_FONT.render("Leaderboard", True, (0,0,0))
    start_y = 50
    x = WINDOW_WIDTH - title_text.get_width() - 10
    display_window.blit(title_text, (x, 5))
    
    for player_id in sorted_by_radius:
        value = gameState["connectedClients"][player_id]
        pygame.draw.circle(display_window, value["color"], (value["x"], value["y"]), gameState["player_radius"] + round(value["radius"]))
        render_text = LEADERBOARD_FONT.render(value["name"], True, (0,0,0))
        display_window.blit(render_text , (value["x"] - text.get_width()/2 + 15, value["y"] - render_text.get_height()/2))

    run = min(len(gameState["connectedClients"]), 3)
    for count, i in enumerate(rev_sorted_players[:run]):
        text = SCORE_FONT.render(str(count+1) + ". " + str(gameState["connectedClients"][i]["name"]) + "  " + str(round(gameState["connectedClients"][i]["radius"])), True, (0,0,0))
        display_window.blit(text, (x, start_y + count * 40))


def quitGame(gameState,display_window):
    """
    This function will select the client/player with the highest score among all the clients. This will run once the round is over and render the winner on all the client's screen.

    Parameters
        ----------
        gameState : Dictionary
            This dictionary is received from the server and contains complete information about all the clients connected to the server.

        display_window : class<obj>, pygame
            The window that will render all the objects on the screen

    Return
        ----------
        None
    """
    DIR = pathlib.Path().resolve()
    sorted_by_radius = sorted(gameState["connectedClients"], key=lambda x: gameState["connectedClients"][x]["radius"])

    winner = sorted_by_radius[len(sorted_by_radius) - 1]
    winnerName = gameState["connectedClients"][winner]["name"]

    TIME_FONT = pygame.font.Font(f".{DIR}\\assets\Facon.ttf",60)
    
    text = TIME_FONT.render(f"Player {winnerName} has won the game!", 1, (0,0,0))
    display_window.blit(text,(100,WINDOW_HEIGHT//2 - 200))
    QUIT_BUTTON = Button(image=pygame.image.load(f".{DIR}\\assets\quit.png"), pos=(750, 450), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    MOUSE_POS = pygame.mouse.get_pos()
    QUIT_BUTTON.changeColor(MOUSE_POS)
    QUIT_BUTTON.update(display_window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if QUIT_BUTTON.checkForInput(MOUSE_POS):
                pygame.quit()
                sys.exit()
    
def update_pos(gameState,player_id):
    """
    This function will capture the key presses made by a client to change it's position and update the gameState to incorporate these changes for a client.

    Parameters
        ----------
        gameState : Dictionary
            This dictionary is received from the server and contains complete information about all the clients connected to the server.
    
        player_id : integer
            The ID of the client whose information is to be fetched from the gameState dictionary. 

    Return
        ----------
        data : string
            This string is sent to the server along with the updated positions of the client.
    """
    data = ""
    keys = pygame.key.get_pressed()
    speed = gameState["player_speed"] - round(gameState["connectedClients"][player_id]["radius"]/14)
    speed = max(1,speed)

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if gameState["connectedClients"][player_id]["y"] - speed - gameState["player_radius"] - gameState["connectedClients"][player_id]["radius"] >= 0:
            gameState["connectedClients"][player_id]["y"] = gameState["connectedClients"][player_id]["y"] - speed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if gameState["connectedClients"][player_id]["y"] + speed + gameState["player_radius"] + gameState["connectedClients"][player_id]["radius"] <= WINDOW_HEIGHT:
            gameState["connectedClients"][player_id]["y"] = gameState["connectedClients"][player_id]["y"] + speed

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if gameState["connectedClients"][player_id]["x"] - speed - gameState["player_radius"] - gameState["connectedClients"][player_id]["radius"] >= 0:
            gameState["connectedClients"][player_id]["x"] = gameState["connectedClients"][player_id]["x"] - speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if gameState["connectedClients"][player_id]["x"] + speed + gameState["player_radius"] + gameState["connectedClients"][player_id]["radius"] <= WINDOW_WIDTH:
            gameState["connectedClients"][player_id]["x"] = gameState["connectedClients"][player_id]["x"] + speed


    data = "changepos " + str(gameState["connectedClients"][player_id]["x"]) + " " + str(gameState["connectedClients"][player_id]["y"])

    return data

def game(client_socket,display_window):
    
    """
    This function runs the main game loop, sending client updates to the server and fetching the updated state from the server. It calls the HUD to draw the updates on the screen. It also calls quitGame once the round is over.

    Parameters
        ----------
        client_socket  : class<obj>, socket
            Socket which stores the connection with the server. Used to send/retrieve game state to/from the server.

        display_window : class<obj>, pygame
            The window that will render all the objects on the screen

    Return
        ----------
        None
    """
    DIR = pathlib.Path().resolve()
    player_id = client_socket.player_id
    gameState = client_socket.send_normal("gameState")

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)

        data = update_pos(gameState,player_id)
        gameState = client_socket.send_normal(data)
        
        HUD(gameState,player_id,display_window)
        
        if gameState["total_time"] == gameState["cur_time"]:
            quitGame(gameState,display_window)

        pygame.display.update()

    client_socket.client_socket.close()
    pygame.quit()
    quit()

def get_font(size): 
    DIR = pathlib.Path().resolve()
    return pygame.font.Font(f".{DIR}\\assets\menu.ttf", size)

def main_menu(player_name,display_window,IP_addr):
    """
    This function renders the landing screen for the game. It initiates the connection with the server. The client/player can chose to start/quit the game from this landing screen.

    Parameters
        ----------
        player_name : String
            The name of the client that will be displayed on the screen.
    
        display_window : class<obj>, pygame
            The window that will render all the objects on the screen 

        IP_addr : String
            The IP address of the server to which the client connects.

    Return
        ----------
        NONE
    """
    DIR = pathlib.Path(__file__).parent.resolve()
    DIR2 = pathlib.Path.joinpath(DIR, "\\assets\Background.png")
    print("DIR IS ")
    print(DIR)
    print(DIR2)
    try:
        client_socket = Connection(player_name,IP_addr)
    except:
        print("QUTTING!!! Invalid IP ADDRESS entered or the server is down!")
        sys.exit()
    # print(DIR + r'\assets\Background.png')
    # print(DIR + r'\\assets\Background.png')
    BG = pygame.image.load(DIR2)
    while True:
        display_window.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(750, 100))
        WELCOME_FONT = pygame.font.Font(f".{DIR}\\assets\Facon.ttf",60)
    
        text = WELCOME_FONT.render(f"Welcome {player_name}!", 1, (255,255,255))
        display_window.blit(text,(400,250))
        PLAY_BUTTON = Button(image=pygame.image.load(f".{DIR}\\assets\play.png"), pos=(750, 400), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(f".{DIR}\\assets\quit.png"), pos=(750, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        display_window.blit(MENU_TEXT, MENU_RECT)
        
        buttons = [PLAY_BUTTON, QUIT_BUTTON]

        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(display_window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game(client_socket,display_window)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def run_client(player_name="",IP_addr=""):
    """
    This function is responsible for starting the client. The name of the client and the server IP address to which the client wants to connect is provided.

    Parameters
        ----------
        player_name : String
            The name of the client that will be displayed on the screen.
    
        IP_addr : String
            The IP address of the server to which the client connects.

    Return
        ----------
        NONE
    """
    pygame.font.init()

    display_window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Eat em ALL!")
    
    if(player_name == ""):
        print("Client name not provided, quitting the client!")
        pygame.quit()
        sys.exit()

    if(IP_addr == ""):
        print("IP Address not provided, quitting the client!")
        pygame.quit()
        sys.exit()

    main_menu(player_name,display_window,IP_addr)