# --------------------
## holds references to common values and objects
class VerServices:
    ## the IP address to use for socket comms
    ip_address = '127.0.0.1'
    ## the IP port to use for socket comms
    ip_port = 5002
    ## whether logging is verbose or not
    verbose = True
    ## reference to the logger
    logger = None

    ## holds instance of server
    server = None
    ## holds instance of client
    client = None
