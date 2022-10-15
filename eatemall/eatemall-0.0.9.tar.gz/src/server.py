import socket
import json
import time
import sys
import math
from src.constants import *
from src.gamestate import GameState
from _thread import *

class ServerConnection():
	"""
	This class creates the socket for the server. It binds the server IP addressed and the port to create the socket.

	"""
	def __init__(self,server_ip=""):
		if server_ip == "":
			self.server_addr = SERVER_IP
		else:
			self.server_addr = server_ip
	
		self.server_port = SERVER_PORT
		self.socket_address = (self.server_addr,self.server_port)
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def create_connection(self):
		try:
			self.server_socket.bind(self.socket_address)
			self.server_socket.listen()
			print(f"Server running at IP: {self.server_addr} and PORT: {self.server_port}")
			print("Server listening now...")
		except socket.error as e:
			print(str(e))
			print("Server could not start due to some error! See Ya!")
			quit()


def resetGameState(gameState):
	"""
	This function resets gameState to reset the game lobby when no clients are connected to the server.

	Parameters
		----------
		 gameState : Dictionary
            This dictionary contains complete information about all the clients connected to the server.

	Return
		----------
		None
	"""
	gameState.food_info=[]
	generate_food(random.randrange(200,250),gameState)
	gameState.running = True
	gameState.cur_time = 0
	gameState.start_time = time.time()

def starting_pos(gameState):
	"""
	This function will calculate the x and y co-ordinate of the position where the client will spawn. The logic ensures that no client spawns inside the radius of an already existing client.

	Parameters
		----------
		gameState : Dictionary
            This dictionary contains complete information about all the clients connected to the server.

	Return
		----------
		tupple(x,y) : int
			The calculated spawning co-ordinates of the client.
	"""
	running = True
	while running:
		running = False
		x = random.randrange(0,WINDOW_WIDTH)
		y = random.randrange(0,WINDOW_HEIGHT)
		for key,value in gameState.connectedClients.items():
			center_distance = math.sqrt((value["x"]-x)**2 + (value["y"]-y)**2)
			if center_distance <= gameState.player_radius + value["radius"]:
				running = True
	return (x,y)

def generate_food(food_points,gameState):
	"""
	This function will generate the circles/food on the screen. The logic guarantees that each generated circle will not spawn inside any connected client.

	Parameters
		----------
		food_points : int
			The number of circles that have to be generated.

		gameState : Dictionary
            This dictionary contains complete information about all the clients connected to the server.

	Return
		----------
		None
	"""
	for i in range(food_points):
		running = True
		while running:
			running = False
			food_x = random.randrange(0,WINDOW_WIDTH)
			food_y = random.randrange(0,WINDOW_HEIGHT)
			for key,value in gameState.connectedClients.items():
				center_distance = math.sqrt((food_x - value["x"])**2 + (food_y-value["y"])**2)
				if center_distance <= gameState.food_radius + value["radius"]:
					running = True
		gameState.food_info.append([food_x,food_y, random.choice(COLOR)])

def reduce_radius(gameState):
	"""
	This function will reduce the radius of all the clients by 0.05%

	Parameters
		----------
		gameState : Dictionary
            This dictionary contains complete information about all the clients connected to the server.

	Return
		----------
		None
	"""
	for key,value in gameState.connectedClients.items():
		if value["radius"] > 10:
			value["radius"] = math.floor(value["radius"]*0.95)

def player_eats_food(gameState):
	"""
	This function will check for collision between any client and the generated food point. If a collision is found then the particular food item will be removed and the collided player's radius will increase.

	Parameters
		----------
		gameState : Dictionary
            This dictionary contains complete information about all the clients connected to the server.

	Return
		----------
		None
	"""
	for key,value in gameState.connectedClients.items():
		player_x = value["x"]
		player_y = value["y"]
		for food_item in gameState.food_info:
			center_distance = math.sqrt((player_x - food_item[0])**2 + (player_y-food_item[1])**2)
			if center_distance <= gameState.food_radius + value["radius"]:
				value["radius"] = value["radius"] + 0.5
				gameState.food_info.remove(food_item)


def player_eats_player(gameState):
	"""
	This function will check for collision between any two pair of clients. If a collision is detected then the client with higher radius/score absorbs the client with lower radius and it's radius increases. The client with lower radius/score is respawned with starting radius.

	Parameters
		----------
		gameState : Dictionary
            This dictionary contains complete information about all the clients connected to the server.

	Return
		----------
		None
	"""
	sorted_players = sorted(gameState.connectedClients, key=lambda x: gameState.connectedClients[x]["radius"])
	for x, player_1 in enumerate(sorted_players):
		for player_2 in sorted_players[x+1:]:
			player_1_x = gameState.connectedClients[player_1]["x"]
			player_1_y = gameState.connectedClients[player_1]["y"]

			player_2_x = gameState.connectedClients[player_2]["x"]
			player_2_y = gameState.connectedClients[player_2]["y"]

			center_distance = math.sqrt((player_1_x - player_2_x)**2 + (player_1_y-player_2_y)**2)
			if center_distance < gameState.connectedClients[player_2]["radius"] - gameState.connectedClients[player_1]["radius"]*0.85:
				gameState.connectedClients[player_2]["radius"] = math.sqrt(gameState.connectedClients[player_2]["radius"]**2 + gameState.connectedClients[player_1]["radius"]**2) 
				gameState.connectedClients[player_1]["radius"] = 0
				gameState.connectedClients[player_1]["x"], gameState.connectedClients[player_1]["y"] = starting_pos(gameState)

def connect_client(client_socket, player_id,client_address,gameState):
	"""
	This function runs in a new thread on the server. It adds a new client to the gameState and continously retrieves the updates of the clients. It also sends the updated gameState to the client. This function also closes the connection with the client once the client disconnects from the server.

	Parameters
		----------
		client_socket  : class<obj>, socket
            Socket which stores the connection of the client with the server. Used to send/retrieve game state to/from the server.

		played_id : integer
			The ID assigned to the connected client.

		client_address : tupple(string,int)
			Tupple containing the IP Address and the port of the connected client.

		gameState : Dictionary
            This dictionary contains complete information about all the clients connected to the server.

	Return
		----------
		None
	"""
	player_name = client_socket.recv(20).decode()
	print(f"Client {player_name} with IP: {client_address[0]} has joined the game!")
	pos = starting_pos(gameState)
	client_socket.send(str(player_id).encode())

	new_player_attributes = {
		"color" : random.choice(COLOR),
		"x" : pos[0],
		"y" : pos[1],
		"name" : player_name,
		"radius" : 0
	}
	gameState.connectedClients[int(player_id)] = new_player_attributes
	
	while True:
		if gameState.running:
			gameState.cur_time = round(time.time()-gameState.start_time)

			if gameState.cur_time >= gameState.total_time:
				gameState.running = False
			else:
				if gameState.cur_time // gameState.radius_loss_time == gameState.next_loss:
					reduce_radius(gameState)
					gameState.next_loss+=1  
		try:
			client_data = client_socket.recv(40)

			client_data = client_data.decode()
			splitted_data = client_data.split(" ")

			if splitted_data[0] == "gameState":
				send_data = json.dumps(gameState.__dict__)

			else:
				player_x = int(splitted_data[1])
				player_y = int(splitted_data[2])
				#Update the game state
				gameState.connectedClients[player_id]["x"] = player_x
				gameState.connectedClients[player_id]["y"] = player_y

				if gameState.running:
					player_eats_food(gameState)
					player_eats_player(gameState)

				if len(gameState.food_info) < 150:
					generate_food(random.randrange(100,150),gameState)

				send_data = json.dumps(gameState.__dict__)

			# send data back to clients
			encoded_data = send_data.encode()
			client_socket.send(encoded_data)

		except Exception as e:
			print(e)
			break

		time.sleep(0.005) 

	print(f"Client {player_name} with IP: {client_address[0]} has DISCONNECTED!!")
	del gameState.connectedClients[player_id]
	if(len(gameState.connectedClients)==0):
		gameState.running = False
	client_socket.close() 

def run_server(server_ip = ""):
	"""
	This function is responsible for starting the server on the provided IP address.

	Parameters
		----------
		server_ip : string
			The IP address of the host machine on which to start the server.

	Return
		----------
		None
	"""

	if(server_ip==""):
		print("Server IP not provided, couldn't start the server! ")
		sys.exit()  

	server = ServerConnection(server_ip)
	try:
		server.create_connection()
	except:
		print("Invalid IP entered for running the server! Please check your private IP and enter the correct one!")
		sys.exit()

	server_socket = server.server_socket
	gameState = GameState()

	generate_food(random.randrange(200,250),gameState)

	print("Waiting for players to connect!")

	while True:
		client_socket,client_address = server_socket.accept()

		if gameState.running == False:
			resetGameState(gameState)
		
		gameState.client_id+=1
		start_new_thread(connect_client,(client_socket,gameState.client_id,client_address,gameState))