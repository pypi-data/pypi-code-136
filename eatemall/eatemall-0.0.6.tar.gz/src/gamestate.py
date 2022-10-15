
class GameState():
    """
	This class maintains the state of the game. 

     Parameters
        ----------
        connectedClients : Dictionary
            This stores all the connected clients' information as <client_id, information>
        client_id : integer
            Starting counter of the ID to be assigned to the clients connecting to the server.
        food_info : list[list[int,int,tupple(int,int,int)]]
            Contains a list of the circles/food generated on the grid.
        running : bool
            Maintains the current status of game lobby.
        cur_time : integer
            Counter to track the time elapsed since the game lobby started.
        total_time : integer
            Total time the game lobby will last for.
        start_time : integer 
            Time when the first client connected to the lobby
        food_radius : integer
            Radius of the circles rendered on the grid as food.
        player_radius : integer
            Initial radius of the player
        radius_loss_time : integer
            Decrease mass once every radius_loss_time seconds
        player_speed : integer
            Initial player speed

        


	"""
    def __init__(self):
        self.connectedClients={}
        self.client_id = 0
        self.food_info=[]
        self.running = False
        self.start_time = 0
        self.total_time = 120
        self.cur_time = 0
        self.food_radius = 5
        self.player_radius = 10
        self.radius_loss_time = 6
        self.next_loss = 1
        self.player_speed = 8
        