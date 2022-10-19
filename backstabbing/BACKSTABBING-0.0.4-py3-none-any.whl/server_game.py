import math
import threading
import json
import time
from server_constants import *
from server_player import *

class Game():
    '''A class to handle all operations of gameplay'''
    def __init__(self, connection):
        """
        This is the Initialzation of the Game class

        Parameters
            ----------
            conncection : dict
                gives the connection in the form of dictionaty
                
        Return
            ----------
            player_details : dict
                returns the connection status and sets it to the Game's connection.
        """
 
        self.connection = connection
        self.player_count = 0
        self.player_objects = []
        self.player_sockets = []
        self.round_time = ROUND_TIME


    def connect_players(self):
        """
        This function will connect any incoming player
        Only accept players if the player count is less than total players
        Accept incoming player socket connections
        Send the current game configuration values over to the client
        Create a new Player object for the connected client
        Send the new player object to the connected client
        Create a thread to monitor the ready status of THIS player

        Parameters
            ----------
            self : instance of Game Class 
        Return
            ----------
            print : print total number of player in game
        """
        #Only accept players if the player count is less than total players
        #i = self.player_count
        while self.player_count<TOTAL_PLAYERS:
            #Accept incoming player socket connections
            player_socket, player_address = self.connection.server_socket.accept()

            #Send the current game configuration values over to the client
            header = str(len(str(ROOM_SIZE)))
            while len(header) < self.connection.header_length:
                header += " "  
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(ROOM_SIZE).encode(self.connection.encoder))

            header = str(len(str(ROUND_TIME)))
            while len(header) < self.connection.header_length:
                header += " "  
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(ROUND_TIME).encode(self.connection.encoder))

            header = str(len(str(FPS)))
            while len(header) < self.connection.header_length:
                header += " "  
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(FPS).encode(self.connection.encoder))

            header = str(len(str(TOTAL_PLAYERS)))
            while len(header) < self.connection.header_length:
                header += " "  
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(TOTAL_PLAYERS).encode(self.connection.encoder))

            #Create a new Player object for the connected client
            self.player_count += 1
            player = Player(self.player_count)
            self.player_objects.append(player)
            self.player_sockets.append(player_socket)
            print(f"New player joining from {player_address}...Total players: {self.player_count}")

            #Send the new player object to the connected client
            player_info_json = json.dumps(player.__dict__)
            header = str(len(player_info_json))
            while len(header) < self.connection.header_length:
                header += " "
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(player_info_json.encode(self.connection.encoder))

            #Alert ALL players of new player joining the game
            self.broadcast()

            #Create a thread to monitor the ready status of THIS player
            ready_thread = threading.Thread(target=self.ready_game, args=(player, player_socket,))
            ready_thread.start()

        #Maximum number of players reached.  No longer accepting new players
        print(f"{TOTAL_PLAYERS} players in game.  No longer accepting new players...")


    def broadcast(self):
        
        """
        This function will broadcast message to all connected player
        Turn each player object into a dict, then into a string with json
        Now that someone else has joined the game, send the game state to ALL players

        Parameters
            ----------
            self : instance of Game class
        Return
            ----------
            conncection : send the json encoded connection details
        """
  
        game_state = []

        #Turn each player object into a dict, then into a string with json
        for player_object in self.player_objects:
            player_json = json.dumps(player_object.__dict__)
            game_state.append(player_json)

        #Now that someone else has joined the game, send the game state to ALL players
        game_state_json = json.dumps(game_state)
        header = str(len(game_state_json))
        while len(header) < self.connection.header_length:
            header += " "
        for player_socket in self.player_sockets:
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(game_state_json.encode(self.connection.encoder))

            
    def ready_game(self, player, player_socket):
       
        """
        This function Ready the game to be played for a SPECIFIC player
        Check if ALL players are ready
        If ALL current players are ready to play the game
        Send updated player flags back to THIS player
        Now that THIS player has started, create a thread to recieve game information

        Parameters
            ----------
            player : dict
                The payer is a dict containing the current state of player whether it is
                ready or waitinf or playing
            player_socket : non negative fd(file descriptor) of accepted socket

        """
  
        #Wait till the given player has sent info signaling they are ready to play
        self.recieve_pregame_player_info(player, player_socket)

        #Reset the game
        self.reset_game(player)

        #If THIS player is ready to play
        if player.is_ready:
            while True:
                #Check if ALL players are ready
                game_start = True
                for player_object in self.player_objects:
                    if player_object.is_ready == False:
                        game_start = False
                    
                #If ALL current players are ready to play the game
                if game_start:
                    player.is_playing = True
                    
                    #Start a clock on the server
                    self.start_time = time.time()
                    break
            
            #Send updated player flags back to THIS player
            self.send_player_info(player, player_socket)

            #Now that THIS player has started, create a thread to recieve game information
            recieve_thread = threading.Thread(target=self.recieve_game_player_info, args=(player, player_socket,))
            recieve_thread.start()
                     

    def reset_game(self, player):
        
        """
        This function will Restart the game and wipe information for a SPECIFIC player

        Parameters
            ----------
            player : dict
                The payer is a dict containing the current state of player whether it is
                ready or waitinf or playing.

        """
  
        #Reset the game
        self.round_time = ROUND_TIME

        #Reset the player
        player.reset_player()


    def send_player_info(self, player, player_socket):
        
        """
        This function will Send specific information about THIS player to the given client
        This will Create a dictionary with the status flags for THIS player
        and Send the player info over to THIS player


        Parameters
            ----------
            player : dict
                The payer is a dict containing the current state of player whether it is
                ready or waitinf or playing.

            player_socket : non negative fd(file descriptor) of accepted socket
     
        """
        #Create a dictionary with the status flags for THIS player
        player_info = {
            'is_waiting': player.is_waiting,
            'is_ready': player.is_ready,
            'is_playing': player.is_playing,
        }

        #Send the player info over to THIS player
        player_info_json = json.dumps(player_info)
        header = str(len(player_info_json))
        while len(header) < self.connection.header_length:
            header += " "
        player_socket.send(header.encode(self.connection.encoder))
        player_socket.send(player_info_json.encode(self.connection.encoder))
        

    def recieve_pregame_player_info(self, player, player_socket):
       
        """
        This function will Recieve specific info about THIS player pregame
        Set the updated values for THIS player

        Parameters
            ----------
            player : dict
                The payer is a dict containing the current state of player whether it is
                ready or waitinf or playing.

            player_socket : non negative fd(file descriptor) of accepted socket
     
        """
        packet_size = player_socket.recv(self.connection.header_length).decode(self.connection.encoder)
        player_info_json = player_socket.recv(int(packet_size))
        player_info = json.loads(player_info_json)

        #Set the updated values for THIS player
        player.set_player_info(player_info)


    def recieve_game_player_info(self, player, player_socket):
        
        """
        This Recieve specific info about THIS player during the game
        this also Set the updated values for the given player
        and Process the new game state to see if a player scored points
        when Game have finished, monitor for the restart of the game.

        Parameters
            ----------
            player : dict
                The payer is a dict containing the current state of player whether it is
                ready or waitinf or playing.

            player_socket : non negative fd(file descriptor) of accepted socket
     
        """
        while player.is_playing:
            packet_size = player_socket.recv(self.connection.header_length).decode(self.connection.encoder)
            player_info_json = player_socket.recv(int(packet_size))
            player_info = json.loads(player_info_json)

            #Set the updated values for the given player
            player.set_player_info(player_info)

            #Process the new game state to see if a player scored points
            self.process_game_state(player, player_socket)

        #Game have finished, monitor for the restart of the game.
        ready_thread = threading.Thread(target=self.ready_game, args=(player, player_socket))
        ready_thread.start()


    def process_game_state(self, player, player_socket):
        
        """
        This Process the given player info and update the games state
        this Update the server clock and Process collisions for current player
        and Send the updated game state back to THIS player




        Parameters
            ----------
            player : dict
                The payer is a dict containing the current state of player whether it is
                ready or waitinf or playing.

            player_socket : non negative fd(file descriptor) of accepted socket
     
        """
        
        self.current_time = time.time()
        self.round_time = ROUND_TIME - int(self.current_time - self.start_time)

        #Process collisions for this player
        for player_object in self.player_objects:
            #Dont collide with yourself!
            if player != player_object:
                if player.coord[1] == player_object.coord[1]:
                    if math.sqrt((player_object.coord[0]-player.coord[0])**2+(player_object.coord[1]-player.coord[1])**2 ) < (2*player.size):
                        if player.px < player_object.px:
                            player.score += 1
                            player.px = player.starting_x
                            player.x = player.starting_x
                            player.y = player.starting_y
                            player.coord = (player.x, player.y, player.size, player.size)

        #Send the updated game state back to THIS player
        
        self.send_game_state(player_socket)


    def send_game_state(self, player_socket):
        
        """
        This Send the current game state of ALL players to THIS given player
        and Sends the server time 
        also Turn each connected player ojbect into a dict, then a string
        Parameters
            ----------
            player_socket : non negative fd(file descriptor) of accepted socket
     
        """
        game_state = []

        #Turn each connected player ojbect into a dict, then a string
        for player_object in self.player_objects:
            player_json = json.dumps(player_object.__dict__)
            game_state.append(player_json)

        #Send the whole game state back to THIS player
        game_state_json = json.dumps(game_state)
        header = str(len(game_state_json))
        while len(header) < self.connection.header_length:
            header += " "
        player_socket.send(header.encode(self.connection.encoder))
        player_socket.send(game_state_json.encode(self.connection.encoder))

        #Send the server time
        header = str(len(str(self.round_time)))
        while len(header) < self.connection.header_length:
            header += " "
        player_socket.send(header.encode(self.connection.encoder))
        player_socket.send(str(self.round_time).encode(self.connection.encoder))