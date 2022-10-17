from typing import Optional, Tuple
from stack_bot.src.elements.api_elements import Message, Poll, Update, CallbackQuery
from stack_bot.src.elements.bot_elements import Event
from stack_bot.src.state_base.state import State


class UpdateState(State[Update]):

    def parse_event(self, event: Event) -> Optional[Update]:
        try:
            update = Update.from_json(event.body)
            return update
        except Exception:
            return None

    def description(self) -> str:
        return "Basic update state"


class MessageState(State[Message]):

    def parse_event(self, event: Event) -> Optional[Message]:
        try:
            update = Update.from_json(event.body)
            return update.message
        except Exception:
            return None
    
    def description(self) -> str:
        return "Basic message state"


class PollState(State[Poll]):

    def parse_event(self, event: Event) -> Optional[Poll]:
        try:
            update = Update.from_json(event.body)
            return update.poll
        except Exception:
            return None
    
    def description(self) -> str:
        return "Basic poll state"


class CallBackQueryState(State[CallbackQuery]):

    def parse_event(self, event: Event) -> Optional[CallbackQuery]:
        try:
            update: Update = Update.from_json(event.body)
            return update.callback_query
        except Exception:
            return None

    def description(self) -> str:
        return "Basic callback query state"


commandsState = {}


class CommandMessageState(MessageState):

    def __init__(self, cmd: str) -> None:
        super().__init__()

        commandsState[cmd] = self.__class__

        self.cmd = cmd

    def parse_event(self, event: Event) -> Optional[Message]:
        mb_msg = super().parse_event(event)
        if not mb_msg:
            return None

        text = mb_msg.text
        words = text.split(" ")

        if words and words[0] == f"/{self.cmd}":
            return mb_msg

        return None

    def split_cmd_and_args(self, text: str) -> Tuple[str, str]:
        return self.cmd, text[len(f"/{self.cmd} "):]

