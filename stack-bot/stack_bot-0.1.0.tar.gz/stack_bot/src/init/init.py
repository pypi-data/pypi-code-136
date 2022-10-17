from typing import Dict, Type

from stack_bot.src.database_base.table import Table, tablesState
from stack_bot.src.state_base.impl import CommandMessageState, commandsState
from stack_bot.src.state_base.state_bot import StateBot

botState = {}


def register_bot(properties_file: str):
    bot().register_bot(properties_file)


def bot() -> StateBot:
    if "bot" not in botState:
        botState["bot"] = StateBot()
    return botState["bot"]


def commands() -> Dict[str, Type[CommandMessageState]]:
    return commandsState


def tables() -> Dict[type, Table]:
    return tablesState
