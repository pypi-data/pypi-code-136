from typing import Dict, Optional, Union
from stack_bot.src.elements.bot_elements import Event
from stack_bot.src.state_base.impl import UpdateState
from stack_bot.src.state_base.state import StateLine
from stack_bot.src.state_base.telegrambot import TelegramBot


class StateBot(TelegramBot):

    default_pipeline_id: int = -1
    
    def __init__(self, properties_file: Optional[str] = None):
        super().__init__(properties_file)

        self.pipelines: Dict[Union[int, str], StateLine] = {StateBot.default_pipeline_id: StateLine()}
        self.curr_pipeline: StateLine = self.default_pipeline()
        self.curr_pipeline_id: int = StateBot.default_pipeline_id

        self.__repeat_handling = False
    
    def handle(self, event: Event):

        while True:
            self.__repeat_handling = False
            self.curr_pipeline = self.default_pipeline()
            self.curr_pipeline_id = StateBot.default_pipeline_id

            maybe_update = UpdateState().parse_event(event)

            if maybe_update and maybe_update.get_from_id():

                chat_id = maybe_update.get_from_id()
                curr_username = None

                if maybe_update.get_chat():
                    curr_username = maybe_update.get_chat().username

                if curr_username:
                    if curr_username in self.pipelines:
                        if chat_id in self.pipelines:
                            states = self.pipelines.pop(curr_username).pipeline
                            reversed(states)
                            for state in states:
                                self.pipelines[chat_id] << state
                        else:
                            self.pipelines[chat_id] = self.pipelines.pop(curr_username)

                if chat_id in self.pipelines:
                    self.curr_pipeline_id = chat_id
                    self.curr_pipeline = self.pipeline(chat_id)

            self.curr_pipeline.run(event)

            if not self.curr_pipeline.pipeline:
                self.pipelines.pop(self.curr_pipeline_id)

            if not self.__repeat_handling:
                break

    def default_pipeline(self) -> StateLine:
        return self.pipelines[StateBot.default_pipeline_id]
    
    def pipeline(self, id: Union[int, str]) -> StateLine:
        return self.pipelines[id]

    def set_pipeline_for(self, id: Union[int, str]) -> bool:
        if id in self.pipelines:
            return False
        else:
            self.pipelines[id] = StateLine()
            return True

    def repeat_handling(self):
        self.__repeat_handling = True


        