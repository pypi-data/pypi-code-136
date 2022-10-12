# Socket Server

# Modules
import socket



class SocketServer:

      # Server Chat Script

      def __init__(self, ip_address, port):

            global server
            
            self.ip = ip_address
            self.port = port

            server = socket.socket()
            server.bind((self.ip, self.port))




      def accept(self, clients):

            global conn
            global add

      
            server.listen(clients)
            conn, add = server.accept()

      def get(self, byte):
            return (conn.recv(byte)).decode()

      def send(self, message):
            
            conn.send(message.encode())

      def close(self):
            server.close()



class SocketClient:

      def __init__(self, ip_address, port):

            global sock

            self.ip = ip_address
            self.port = port

            sock = socket.socket()


      def connect(self):

            sock.connect((self.ip, self.port))

      def send(self, message):
            sock.send(message.encode())

      def get(self, byte):
            return (sock.recv(1024)).decode()

      def leave(self):
            sock.close()

def host():
      return socket.gethostbyname(socket.gethostname())

      

              

      




