import argparse
from src import server_to_play
from src import Client

def run_server():
    parser = argparse.ArgumentParser(
        description="Start the server on a private LAN on port 12345"
    )
    parser.add_argument(
       '-IP', '--IP', type=str,help="IP address to start the server on"
    )
    
    args = parser.parse_args()
    
    server_to_play.start_server(args.IP)

def run_client():
    parser = argparse.ArgumentParser(
        description="Start the server on a private LAN on port 12345"
    )
    parser.add_argument(
       '-IP', '--IP', type=str,help="IP address to start the server on"
    )
    
    args = parser.parse_args()
    
    Client.start_client(args.IP)
