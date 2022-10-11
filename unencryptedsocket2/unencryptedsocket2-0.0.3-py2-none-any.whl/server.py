from .utils import recv_all, utf8d
import traceback
import threading
import socket
import struct
import pickle
import json


class SS:
    def __init__(
            self, functions,
            host = "127.199.71.10", port = 39291,
            silent = False, backlog = 5
    ):
        self.terminate = False
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__s.bind((host, int(port)))
        self.__s.listen(backlog)
        self.functions = functions or {}

    def handler(self, conn, addr):
        uid = "{}:{}".format(*addr)
        try:
            while True:
                request = recv_all(conn)
                if not request:
                    break
                try:
                    request = json.loads(utf8d(request))
                except:
                    request = pickle.loads(request)
                try:
                    if request["command"] in self.functions:
                        response = self.functions[request["command"]](*request["data"][0], **request["data"][1])
                    else:
                        raise Exception("request command '{}' is not in socket functions".format(request["command"]))
                except:
                    response = traceback.format_exc()
                try:
                    response = json.dumps(response).encode()
                except TypeError:
                    response = pickle.dumps(response)
                conn.sendall(struct.pack('>I', len(response))+response)
        except:
            traceback.print_exc()
        finally:
            conn.close()

    def start(self):
        try:
            while not self.terminate:
                conn, addr = self.__s.accept()
                threading.Thread(target=self.handler, args=(conn, addr)).start()
        except Exception as e:
            if not self.terminate:
                raise e

    def stop(self):
        self.terminate = True
        self.__s.close()
        return True

