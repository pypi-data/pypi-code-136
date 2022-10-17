import logging
import socket
from typing import Optional, Union

# TODO: Integration tests with socket server mimicking UR controller.


class URSocketClient:
    """Socket client for communication with UR robots.

    Parameters
    ----------
    ur_hostname
        IP or hostname for robot controller.
    ur_port
        One of 30001, 30002 or 30003. See `Remote Control Via TCP/IP
        <https://www.universal-robots.com/articles/ur/interface-communication/remote-control-via-tcpip/>`_
    recv_socket_hostname
        The address the robot controller is to use to send data back to the
        client. This needs to be an IP that the controller can reach the client
        (your computer) with or a hostname that resolves correctly for the robot
        controller.
    recv_socket_port
        Any free port on the client (your computer). It's generally advisable to
        use not use one the reserved ports (1-1024). Arbitrarily defaults to
        40000.
    send_socket_timeout
        Timeout for the send operations on the send port. I.e. how long to wait
        for UR controller to accept message.

    Usage
    -----
    >>> import math
    >>> import move_to_conf from ur_py_ctl
    >>> move_cmd = move_to_conf([radians(j) for j in [0, 0, 30, 0, 30]])
    "movej([0, 0, 30, 0, 30])"
    >>> script = "def program()\n" + move_cmd + "\nend\n\nprogram()"
    "def program
    movej([0, 0, 30, 0, 30])
    end

    program()"
    >>> with URClient("robot.local", recv_socket_hostname="laptop.local") as client:
    ...     client.send_script(script)
    """

    def __init__(
        self,
        ur_hostname: str,
        ur_port=30002,
        recv_socket_hostname: str = None,
        recv_socket_port: int = 40000,
        send_socket_timeout: int = 2,
    ):
        self.send_addr = (ur_hostname, ur_port)
        self.recv_addr = (recv_socket_hostname, recv_socket_port)

        self.send_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.send_sock.settimeout(send_socket_timeout)

        # SO_REUSEADDR might be causing comm problems..
        # self.send_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.recv_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        self.recv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __enter__(self):
        self._connect_send_sock()
        if self._has_recv_addr():
            self._bind_recv_sock()
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback) -> bool:
        self.send_sock.close()
        self.recv_sock.close()

        return True

    def send_script(
        self, script: Union[str, bytes], await_response=False
    ) -> Optional[str]:
        if isinstance(script, str):
            script = script.encode(encoding="utf-8")

        self.send_sock.send(script)

        if await_response:
            if not self._has_recv_addr():
                raise RuntimeError("Missing address for receiving socket!")

            # Listen for incoming connections
            self.recv_sock.listen(1)

            logging.debug("Waiting for accept")

            conn, client_address = self.recv_sock.accept()

            logging.debug(f"Received accept from: {client_address}")

            return conn.recv(1024).decode(encoding="utf-8")

        return None

    def _connect_send_sock(self) -> None:
        self.send_sock.connect(self.send_addr)

    def _bind_recv_sock(self) -> None:
        self.recv_sock.bind(self.recv_addr)

    def _has_recv_addr(self) -> bool:
        return self.recv_addr[0] is not None and self.recv_addr[1] is not None
