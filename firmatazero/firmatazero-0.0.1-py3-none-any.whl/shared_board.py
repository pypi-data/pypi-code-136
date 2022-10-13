import atexit
import contextlib
from threading import RLock

import pyfirmata2
import serial
from serial.tools import list_ports


def detect_port():
    """Detect Arduino port

    If multiple can be found, it returns the first one.
    If no Arduinos found, raise RuntimeError.
    """

    serial_comports = []
    comports = list_ports.comports()
    for comport in comports:
        # Skip if cannot be Arduino
        if comport.pid is None or comport.device is None:
            continue

        # Try opening serial connection, skip if fails
        try:
            ser = serial.Serial(
                comport.device,
                9600,
                timeout=1,
                writeTimeout=0,
            )
            ser.close()
        except serial.SerialException:
            continue

        # Serial did not fail, return if 'arduino' in description
        if "arduino" in comport.description.lower():
            return comport.device
        else:
            serial_comports.append(comport.device)

    # Return the first with serial, if no 'arduino' in descriptions
    if len(serial_comports) > 0:
        return serial_comports[0]

    # Raise error if no potential Arduinos detected
    raise RuntimeError("Arduino port not found (DOCS LINK)")


class SharedBoard:
    _board = None
    _port = ""  # allow setting to PyFirmata2.AUTODETECT == None
    _board_access_lock = RLock()

    @staticmethod
    def _get_board():
        if SharedBoard._board is None:
            if SharedBoard._port == "":
                port = detect_port()
            else:
                port = SharedBoard._port

            SharedBoard._board = pyfirmata2.Arduino(port)

        return SharedBoard._board

    @staticmethod
    def exit_handler():
        if SharedBoard._board is not None:
            SharedBoard._board.exit()


atexit.register(SharedBoard.exit_handler)


def set_port(port):
    if SharedBoard._board is not None:
        raise RuntimeError(
            "Board has already been initialized. Set port earlier."
        )

    SharedBoard._port = port


def set_board(board):
    if SharedBoard._board is not None:
        raise RuntimeError(
            "Board has already been initialized. Set board earlier."
        )

    SharedBoard._board = board


def get_board():
    return SharedBoard._get_board()


@contextlib.contextmanager
def shared_board():
    with SharedBoard._board_access_lock:
        try:
            yield SharedBoard._get_board()
        finally:
            pass


def shared_lock():
    return SharedBoard._board_access_lock
