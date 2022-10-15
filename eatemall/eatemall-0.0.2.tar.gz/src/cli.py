
import argparse
from src import client
from src import server


def runServer():
    parser = argparse.ArgumentParser(
        description="Start the server on a private LAN on port 12345"
    )
    parser.add_argument(
       '-IP', '--IP', type=str,help="IP address to start the server on"
    )
    
    args = parser.parse_args()
    
    server.run_server(args.IP)

def runClient():
    parser = argparse.ArgumentParser(
        description="Connect your game to an existing server on the LAN! If the server is not started, start the server first!"
    )
    parser.add_argument(
       '-n', '--name', type=str,help="Client Name"
    )
    parser.add_argument(
       '-IP', '--IP', type=str,help="IP address of the server"
    )
    
    args = parser.parse_args()
    
    client.run_client(args.name,args.IP)

