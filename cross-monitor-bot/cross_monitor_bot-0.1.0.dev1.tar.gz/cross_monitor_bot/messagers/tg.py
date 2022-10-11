import asyncio
from datetime import datetime
import logging
from typing import Optional

from aiogram import Bot

from .abc import ABCMessager


class TgMessager(ABCMessager):
    def __init__(self, token: str, chatId: int) -> None:
        self.bot = Bot(token=token)
        self.chatId = chatId
        self._loop = asyncio.get_event_loop()
        logger = logging.getLogger("cmb")
        if logger:
            self.logger = logger
        else:
            self.logger = logging.Logger("cmb", logging.WARNING)

    def report(self, checker: str, target: str, status: bool, start: datetime, end: Optional[datetime] = None):
        if end:
            message = (
                f"{target} is now reachable by {checker}"
                f"\nstart: {start.isoformat(timespec='seconds')}"
                f"\nend:   {end.isoformat(timespec='seconds')}"
                f"\ntotal: {int((end - start).total_seconds())} seconds"
            )
        else:
            message = (
                f"{target} is unreachable by {checker}"
                f"\nstart: {start.isoformat(timespec='seconds')}"
            )
        try:
            self._loop.run_until_complete(self.bot.send_message(self.chatId, message))
        except Exception as e:
            self.logger.error(f"{e} {self.chatId}, {message}")
            return False
        return True
