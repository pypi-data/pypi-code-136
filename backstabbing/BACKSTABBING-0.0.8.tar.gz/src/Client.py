#online multiplayer game client
import pygame
import socket, threading, json


def fetch_data(player_socket,header_length,encoder):
        packet_size = player_socket.recv(header_length).decode(encoder)
        player_info_json = player_socket.recv(int(packet_size))
        player_info = json.loads(player_info_json)
        return player_info    
    
class Player():

    def __init__(self,WINDOW_WIDTH,display_surface,player_socket,header_length,encoder) :
        self.player_socket= player_socket
        self.header_length= header_length
        self.encoder = encoder

        player_info= fetch_data(self.player_socket,self.header_length,self.encoder)
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.display_surface = display_surface

        self.number = player_info['number']
        self.size = player_info['size']  # this size is equal to radius

        self.starting_x = player_info['starting_x'] # centre
        self.starting_y = player_info['starting_y'] # centre
        
        self.p_color = player_info['p_color']
        self.s_color = player_info['s_color']

        self.px = player_info['px']
        self.x = player_info['x']
        self.y = player_info['y']

        self.dx = player_info['dx']
        self.dy = player_info['dy']
        self.coord = player_info['coord']

        self.is_waiting = player_info['is_waiting']
        self.is_ready = player_info['is_ready']
        self.is_playing = player_info['is_playing']
        self.status_message = player_info['status_message']

    def set_player_info(self,player_info):
        self.is_waiting = player_info['is_waiting']
        self.is_ready = player_info['is_ready']
        self.is_playing = player_info['is_playing']


    def update(self,display_surface,WINDOW_WIDTH):
        keys= pygame.key.get_pressed()

        #creating circles
        player_circle = pygame.draw.circle(display_surface, self.p_color, [self.coord[0],self.coord[1]], self.coord[2], self.coord[3] )

        if self.is_playing :
            if keys[pygame.K_UP] and player_circle.top >0 :
                self.dx=0
                self.dy = -2*self.size
            elif keys[pygame.K_DOWN] and player_circle.bottom <WINDOW_WIDTH:
                self.dx=0
                self.dy = 2*self.size
            elif keys[pygame.K_LEFT] and player_circle.left >0 :
                self.dx = -2*self.size
                self.dy =0
            elif keys[pygame.K_RIGHT] and player_circle.right < WINDOW_WIDTH:
                self.dx = 2*self.size
                self.dy = 0
            else :
                self.dx =0
                self.dy =0
            
            self.px= self.x
            self.x += self.dx
            self.y +=self.dy
            self.coord = (self.x,self.y, self.size,0) # radius is self.size and the width is '0' inorder to fll the circle completely
            

    def reset_player(self):
        self.px=self.starting_x
        self.x = self.starting_x
        self.y = self.starting_y
        self.coord = (self.x , self.y,self.size, 0)

        

        self.is_waiting = False
        self.is_ready = True
        self.is_playing = False
        self.status_message = "Ready...waiting for the other players"
        
class Game():

    def __init__(self, player, total_players, ROUND_TIME,player_socket,header_length,encoder,display_surface,WINDOW_WIDTH):

        self.player_socket= player_socket
        self.header_length= header_length
        self.encoder = encoder
        self.display_surface= display_surface
        self.WINDOW_WIDTH= WINDOW_WIDTH
       
        self.player = player
        self.total_players = total_players
        self.is_active = False


        self.player_count = self.player.number - 1

        self.game_state = []

        self.round_time = ROUND_TIME
        self.high_score = 0
        self.winning_player = 0

        waiting_thread = threading.Thread(target=self.recieve_pregame_state)
        waiting_thread.start()

    def ready_game(self):
        self.player.is_waiting = False
        self.player.is_ready = True
        self.player.status_message = "Ready...Waiting for other players"

        self.send_player_info(self.player_socket,self.encoder,self.header_length)

        #Monitor for start of game 
        start_thread = threading.Thread(target=self.start_game)
        start_thread.start()

    def start_game(self):
        """
        It will start the game and wait tp receive info from server that game has begun


        Parameters
            ----------
            self : instance of class Game
     
        """
        while True:
            #wait tp receive info from server that game has begun
            self.recieve_player_info()
            if self.player.is_playing:
                self.is_active = True
                self.player.is_ready = False
                self.player.status_message = "Play!"
                break

   
   
    def reset_game(self,ROUND_TIME):
        """
        It will reset the game and the player

        Parameters
            ----------
            self : instance of class Game
     
        """
        #game
        self.round_time = ROUND_TIME
        self.winning_player = 0
        self.high_score = 0 

        #reset the player
        self.player.reset_player()


        self.send_player_info()
   
        start_thread = threading.Thread(target=self.start_game)
        start_thread.start()



    def send_player_info(self,player_socket,encoder,header_length):
        """
        It will send the player details in the instance of dictionary called self.player,
        it sets the player status whether in waiting,ready or playing, sets the coords and px.

        Parameters
            ----------
            self : instance of class Game
     
        """
        player_info ={
            'coord' : self.player.coord,
            'px' : self.player.px,  #for px
            'is_waiting': self.player.is_waiting,
            'is_ready' : self.player.is_ready,
            'is_playing': self.player.is_playing,
        }

        player_info_json = json.dumps(player_info)
        header = str(len(player_info_json))
        while len(header) < header_length:
            header += " "

        player_socket.send(header.encode(encoder))
        player_socket.send (player_info_json.encode(encoder))

    def recieve_player_info(self):
       
        """
        It will receive the player details in the instance of Game class player_info,
        it sets the updated flag for player.

        Parameters
            ----------
            self : instance of class Game
     
        """
        
        

        player_info = fetch_data(self.player_socket,self.header_length,self.encoder)

        #Set the updated flags for player
        self.player.set_player_info(player_info)
  
  
    def recieve_pregame_state(self):
        global player_socket,header_length,encoder
        """
        It will receive the program details in the instance of dictionary called self.player,
        it sets the player count.

        Parameters
            ----------
            self : instance of class Game
     
        """
        while self.player_count < self.total_players:
            self.game_state = fetch_data(self.player_socket,self.header_length,self.encoder)

            self.player_count += 1
        

        self.player.status_message = "Press Enter to play!"

    def recieve_game_state(self,header_length,player_socket,encoder):
        """
        It will receive the game details in the instance of dictionary called self.game_state,
        it sets the packet size ,and round time
        Parameters
            ----------
            self : instance of class Game
     
        """
        
        self.game_state = fetch_data(self.player_socket,self.header_length,self.encoder)

        packet_size = player_socket.recv(header_length).decode(encoder)
        self.round_time = player_socket.recv(int(packet_size)).decode(encoder)

        self.process_game_state()


    def process_game_state(self):
        """
        It will fill the player details in the instance of dictionary called self.player,
        it sets the coordinates ,resets the score and initial conditions.

        Parameters
            ----------
            self : instance of class Game
     
        """
        current_score =[]

        for player in self.game_state:
            player = json.loads(player)
            if player['number'] == self.player.number:
                self.player.coord = player['coord']
                self.player.px=self.player.px
                self.player.x = self.player.coord[0]
                self.player.y = self.player.coord[1]

            if player['score'] > self.high_score :
                self.winning_player = player['number']
                self.high_score = player['score']
            
            current_score.append(player['score'])
        
        count =0
        for score in current_score:
            if score == self.high_score:
                count+=1

            if count >1 :
                self.winning_player = 0



    def update(self,FLAG=False):
        # if FLAG== True :
        #     self.reset_game()
        # .......
        

        if self.player.is_playing :
            self.player.update(self.display_surface,self.WINDOW_WIDTH)

            if int(self.round_time) == 0 :
                self.player.is_playing = False
                self.player.is_ready = False
                self.player.is_waiting = True
                self.player.status_message = "Game over! Enter to play again"


            self.send_player_info(self.player_socket,self.encoder,self.header_length)
            self.recieve_game_state(self.header_length,self.player_socket,self.encoder)

    def draw(self,display_surface, WHITE,MAGENTA,font,WINDOW_WIDTH,WINDOW_HEIGHT):
        """
        It will fill the display to the secondary color of the current winning player

        Parameters
            ----------
            self : instance of class Game
     
        """
        
        for player in self.game_state:
            player = json.loads(player)
            if player['number'] == self.winning_player :
                display_surface.fill(player['s_color'])

        
        current_scores = []

        
        for player in self.game_state :
            player = json.loads(player)

            score ="p" + str(player['number']) + ": " + str(player['score'])
            score_text = font.render(score,True, WHITE)
            score_rect = score_text.get_rect()
            if player['number'] == 1:
                score_rect.topleft = (player['starting_x'], player['starting_y'])
            elif player['number']== 2:
                score_rect.topright = (player['starting_x'], player['starting_y'])

            elif player['number'] == 3:
                score_rect.bottomleft = (player['starting_x'], player['starting_y'])
            else :
                score_rect.bottomright = (player['starting_x'], player['starting_y'])
            current_scores.append((score_text, score_rect))


            pygame.draw.circle(display_surface, player['p_color'], [player['coord'][0],player['coord'][1]], player['coord'][2], player['coord'][3] )
            pygame.draw.circle(display_surface, MAGENTA, [player['coord'][0],player['coord'][1]], player['coord'][2], player['coord'][3], int( player['coord'][2]/10) )


        pygame.draw.circle(display_surface, self.player.p_color, [self.player.coord[0],self.player.coord[1]], self.player.coord[2], self.player.coord[3] )
        pygame.draw.circle(display_surface, MAGENTA , [self.player.coord[0],self.player.coord[1]], self.player.coord[2], self.player.coord[3], int(self.player.size/10))
        render_text = font.render('p', True,WHITE)
        render_rect = render_text.get_rect()
        render_rect.topleft = (self.player.coord[0]-1,self.player.coord[1]-2)
        display_surface.blit(render_text,render_rect)
        
	    
        

        for score in current_scores :
            display_surface.blit(score[0],score[1])

        

        time_text = font.render("Round Time: "+ str(self.round_time),True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.center = (WINDOW_WIDTH//2,15)
        display_surface.blit(time_text, time_rect)

        status_text = font.render(self.player.status_message, True, WHITE)
        status_rect = status_text.get_rect()
        status_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
        display_surface.blit(status_text, status_rect)



#create a connection and get game window information from the server
def start_client(IP_ADDR):

        #define socket constants to be used and altered
    #DEST_IP should be of the form '192.168.1.* or other addresses

    DEST_IP = str(input("Enter SERVER'S IP ADDRESS:"))
    DEST_PORT = 12345
    encoder = 'utf-8'
    header_length = 10
    player_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    player_socket.connect((IP_ADDR, DEST_PORT))


    packet_size = player_socket.recv(header_length).decode(encoder)
    room_size = int(player_socket.recv(int(packet_size)).decode(encoder))

    packet_size = player_socket.recv(header_length).decode(encoder)
    round_time = int(player_socket.recv(int(packet_size)).decode(encoder))

    packet_size = player_socket.recv(header_length).decode(encoder)
    fps= int(player_socket.recv(int(packet_size)).decode(encoder))

    packet_size = player_socket.recv(header_length).decode(encoder)
    total_players = int(player_socket.recv(int(packet_size)).decode(encoder))
    #initialize pygame
    pygame.init()

    #set game constraints
    WINDOW_WIDTH = room_size
    WINDOW_HEIGHT = room_size
    ROUND_TIME = round_time
    BLACK =(0,0,0)
    WHITE =(255,255,255)
    MAGENTA =(155,0,155)
    FPS = fps
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('gabriola',28)

    #Create a game window
    display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    pygame.display.set_caption("BACKSTABBING~~")

    #Create player and game objects
    my_player = Player(WINDOW_WIDTH,display_surface,player_socket,header_length,encoder)
    my_game = Game(my_player,total_players,ROUND_TIME,player_socket,header_length,encoder,display_surface,WINDOW_WIDTH)

    #   The main game loop
    running = True
    while running:

        #check to see if the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            # my_game.update(True)  
            # to update the game window
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    if my_player.is_waiting and my_game.player_count == my_game.total_players :
                        my_game.ready_game()

                    if my_player.is_waiting and my_game.is_active:
                        my_game.reset_game()
                    



        #fill the surface
        display_surface.fill(BLACK)

        #Update and draw classes
    # my_player.update()
        my_game.update()
        my_game.draw(display_surface,WHITE,MAGENTA,font,WINDOW_WIDTH,WINDOW_HEIGHT)

        #update the display and tick the clock
        pygame.display.update()
        clock.tick(FPS)
start_client('192.168.1.12')