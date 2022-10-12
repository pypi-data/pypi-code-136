import sys
import threading
import time
from typing import Dict

import zmq
from cachetools import TTLCache, cached

from isyntax_backend.isyntax_reader import IsyntaxSlide


def tprint(msg):
    """like print, but won't get newlines confused with multiple threads"""
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()


class ServerTask(threading.Thread):
    """ServerTask"""

    number_of_workers = 5
    port = 5556

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        tprint(f"starting isyntax backend...")
        context: zmq.Context = zmq.Context()
        frontend: zmq.Socket = context.socket(zmq.ROUTER)
        frontend.bind(f"tcp://*:{self.port}")
        tprint(f"zeromq server binding to *:{self.port}")

        backend: zmq.Socket = context.socket(zmq.DEALER)
        backend.bind("inproc://backend")

        workers = []
        for i in range(self.number_of_workers):
            worker = ServerWorker(context, i)
            worker.start()
            workers.append(worker)
        tprint(f"{len(workers)} workers started.")
        zmq.proxy(frontend, backend)

        frontend.close()
        backend.close()
        context.term()


class ServerWorker(threading.Thread):
    """ServerWorker"""

    def __init__(self, context: zmq.Context, id: int):
        threading.Thread.__init__(self)
        self.context: zmq.Context = context
        self.id = id

    def run(self):
        worker: zmq.Socket = self.context.socket(zmq.DEALER)
        worker.connect("inproc://backend")
        tprint(f"Worker[{self.id}] started")
        while True:
            client_id = worker.recv_string()
            req_msg = worker.recv_json()
            mapped_filepath = "/data" + req_msg["filepath"]
            reader = self.get_reader(mapped_filepath)
            if req_msg["req"] == "verification":
                self.__send_json(
                    worker=worker, client_id=client_id, rep_msg=reader.result
                )
            elif req_msg["req"] == "get_info":
                self.__send_json(
                    worker=worker, client_id=client_id, rep_msg=reader.get_info()
                )
            elif req_msg["req"] == "LABEL":
                self.__send(
                    worker=worker, client_id=client_id, rep_msg=reader.get_label()
                )
            elif req_msg["req"] == "MACRO":
                self.__send(
                    worker=worker, client_id=client_id, rep_msg=reader.get_macro()
                )
            elif req_msg["req"] == "get_region":
                resp, image_array, width, height = reader.get_region(
                    req_msg["level"],
                    req_msg["start_x"],
                    req_msg["start_y"],
                    req_msg["size_x"],
                    req_msg["size_y"],
                )
                self.__send_array_response(
                    worker=worker,
                    client_id=client_id,
                    resp=resp,
                    image_array=image_array,
                    width=width,
                    height=height,
                )
            elif req_msg["req"] == "get_tile":
                resp, image_array, width, height = reader.get_tile(
                    req_msg["level"], req_msg["tile_x"], req_msg["tile_y"]
                )
                self.__send_array_response(
                    worker=worker,
                    client_id=client_id,
                    resp=resp,
                    image_array=image_array,
                    width=width,
                    height=height,
                )
            elif req_msg["req"] == "get_thumbnail":
                resp, image_array, width, height = reader.get_thumbnail(
                    req_msg["max_x"], req_msg["max_y"]
                )
                self.__send_array_response(
                    worker=worker,
                    client_id=client_id,
                    resp=resp,
                    image_array=image_array,
                    width=width,
                    height=height,
                )
            else:
                req = req_msg["req"]
                self.__send_json(
                    worker=worker,
                    client_id=client_id,
                    rep_msg={
                        "rep": "error",
                        "status_code": 422,
                        "detail": f"Invalid request ({req})",
                    },
                )

        worker.close()

    def __send_json(self, worker: zmq.Socket, client_id: str, rep_msg: Dict):
        worker.send_string(client_id, zmq.SNDMORE)
        worker.send_json(rep_msg)

    def __send(self, worker: zmq.Socket, client_id: str, rep_msg):
        worker.send_string(client_id, zmq.SNDMORE)
        worker.send(rep_msg)

    def __send_array_response(
        self, worker: zmq.Socket, client_id: str, resp: Dict, image_array, width, height
    ):
        if resp["rep"] == "success":
            rep_msg = {
                "rep": "success",
                "status_code": 200,
                "detail": f"",
                "width": width,
                "height": height,
            }
            rep_payload = image_array
        else:
            rep_msg = resp
            rep_payload = b""

        worker.send_string(client_id, zmq.SNDMORE)
        worker.send_json(rep_msg, zmq.SNDMORE)
        worker.send(rep_payload)

    @cached(cache=TTLCache(maxsize=100, ttl=600))
    def get_reader(self, mapped_filepath):
        return IsyntaxSlide(mapped_filepath)


if __name__ == "__main__":
    server = ServerTask()
    server.start()
    time.sleep(1)

    server.join()
