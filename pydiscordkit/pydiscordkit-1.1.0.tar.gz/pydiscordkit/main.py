from webbrowser import open
import pyautogui
import os
from pyautogui import (
    ImageNotFoundException,
    click,
    hotkey,
    locateOnScreen,
    moveTo,
    press,
    size,
    typewrite,
)
import time

WIDTH, HEIGHT = size()

def findtextboxdc() -> None:
    """click on text box"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\attachmentdark.png")
    try:
        moveTo(location[0] + 150, location[1] + 5)
    except Exception:
        location = locateOnScreen(f"{dir_path}\\data\\attachmentlight.png")
        moveTo(location[0] + 200, location[1] + 5)
    click()

def _websingle(receiver: str, message: str) -> None:
    """Opens Discord based on the Receiver"""

    open("https://discord.com/channels/@me/" + receiver)

def _webserver(serverid: str, channelid: str) -> None:
    """Opens Discord based on the Receiver"""

    open("https://discord.com/channels/" + serverid + "/" + channelid)

def send_dm(message: str, channelid:str,timesec:int) -> None:
    """Parses and Sends the Message"""
    try:
        _websingle(receiver=channelid, message=message)
        time.sleep(timesec)
        click(WIDTH / 2, HEIGHT / 2)   
        for char in message:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
        findtextboxdc()
        press("enter")
        print("Message successfully delivered")
    except Exception as e:
        return e

def msg_server(message:str,serverid:str,channelid:str,timesec:int):
        
    try:
        _webserver(serverid=serverid, channelid=channelid)
        time.sleep(timesec)
        click(WIDTH / 2, HEIGHT / 2)   
        for char in message:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
        findtextboxdc()
        press("enter")
        print("Message successfully delivered")
    except Exception as e:
        print(e)

