from server_constants import *

class Player():
    '''A class to store a connected clients player information'''
    def __init__(self, number):
        """
        This is an initialization function and takes the number of player as input

        Parameters
            ----------
            number : int
                The number of players playing the game, which is in this case limted to 4
        Return
            ----------
            res : number
                returns the number in inputm also the self sets the radius of the player, also since this is an 
                initialization function this will set the scores of player to zero
        """
 
        self.number = number
        self.size = PLAYER_RADIUS
        self.score = 0

        #Assign starting conditions that vary with player number
        # changing the starting coordinates according to circle.
        if self.number == 1:
            self.starting_x = PLAYER_RADIUS
            self.starting_y = PLAYER_RADIUS
            self.p_color = (255, 0, 0)
            self.s_color = (150, 0, 0)
        elif self.number == 2:
            self.starting_x = ROOM_SIZE - PLAYER_RADIUS
            self.starting_y = PLAYER_RADIUS
            self.p_color = (0, 255, 0)
            self.s_color = (0, 150, 0)
        elif self.number == 3:
            self.starting_x = PLAYER_RADIUS
            self.starting_y = ROOM_SIZE - PLAYER_RADIUS
            self.p_color = (0, 0, 255)
            self.s_color = (0, 0, 150)
        elif self.number == 4:
            self.starting_x = ROOM_SIZE - PLAYER_RADIUS
            self.starting_y = ROOM_SIZE - PLAYER_RADIUS
            self.p_color = (255, 255, 0)
            self.s_color = (150, 150, 0)
        else:
            print("Too many players trying to join...")

        #Set the rest of the player attributes
        self.px = self.starting_x
        self.x = self.starting_x
        self.y = self.starting_y
        self.dx = 0
        self.dy = 0
        self.coord = (self.x, self.y, PLAYER_RADIUS, 0)

        self.is_waiting = True
        self.is_ready = False
        self.is_playing = False
        self.status_message = f"Waiting for {TOTAL_PLAYERS} total players"


    def set_player_info(self, player_info):
        """
        This sets the player info of the player initialized

        Parameters
            ----------
            player_info : dict
                The info of players playing the game in form of dictionary
        Return
            ----------
            self : dict
                returns the dictionary with the status set of different states of player
                ie waiting,ready or playing.
                Other than that it also sets up the coodinated of the player in dict
        """
 
        '''Set the player info to the given info from the client (coord and status flags)'''
        self.coord = player_info['coord']
        self.px=player_info['px']  # for px
        self.is_waiting = player_info['is_waiting']
        self.is_ready = player_info['is_ready']
        self.is_playing = player_info['is_playing']


    def reset_player(self):
        '''Reset player values for a new round on the server side'''
        
        self.score = 0