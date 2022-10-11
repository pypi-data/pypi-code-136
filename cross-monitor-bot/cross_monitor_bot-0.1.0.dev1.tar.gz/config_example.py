from datetime import datetime
import os

from cross_monitor_bot.methods import GetMethod, PingMethod
from cross_monitor_bot.messagers import TgMessager
from cross_monitor_bot.config import Task, Chat

TZ = datetime.now().astimezone().tzinfo  # timezone(timedelta(hours=1))
SELF_NAME = "n"
CHATS = [
    Chat(messager=TgMessager(token=os.getenv("TG_TOKEN", "TOKEN"), chatId=int(os.getenv("TG_CHAT_ID", 0))),
         name="tg"),
]

TASKS = [
    Task(
        name="vdsina",
        method=GetMethod(url="http://109.107.176.84", path="/live"),
        checkPeriod="* * * * *",
        messagers=["tg"],
        roundRodinSkip=True
    ),
    Task(
        name="domserver",
        method=PingMethod(host="192.168.100.22"),
        checkPeriod="* * * * *",
        messagers=["tg"]
    ),
]
