from dataclasses import dataclass

import requests as reqs
import json
from typing import List, Tuple, Union, Optional, Any, Dict
from configparser import RawConfigParser

from dataclasses_json import dataclass_json, Undefined


def remove_nones(dict_: Dict[str, Any]) -> Dict[str, Any]:
    def req(v):
        if type(v) is dict:
            return remove_nones(v)
        elif type(v) is list:
            return list(map(req, v))
        else:
            return v

    return {k: req(v) for (k, v) in dict_.items() if v}


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class InlineKeyboardButton:
    text: str
    url: Optional[str] = None
    callback_data: Optional[str] = None


@dataclass_json
@dataclass
class InlineKeyboardMarkup:
    inline_keyboard: List[List[InlineKeyboardButton]]


@dataclass_json
@dataclass
class KeyboardButton:
    text: str
    request_contact: Optional[bool] = None
    request_location: Optional[bool] = None


@dataclass_json
@dataclass
class ReplyKeyboardMarkup:
    keyboard: List[List[KeyboardButton]]
    resize_keyboard: Optional[bool] = None
    one_time_keyboard: Optional[bool] = None
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None


@dataclass_json
@dataclass
class ReplyKeyboardRemove:
    remove_keyboard: bool = True
    selective: Optional[bool] = None


@dataclass_json
@dataclass
class ForceReply:
    force_reply: bool = True
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None


ReplyMarkup = Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]


class TelegramBot:
    __url = "https://api.telegram.org/bot{token}/{method}"

    def __init__(self, properties_file: Optional[str] = None):
        r"""
        Crate Telegram Bot instance, requires file which at least contains telegramBot.token
        """

        self.__registered = False
        self.__token = None

        if properties_file:
            self.register_bot(properties_file)

    def register_bot(self, properties_file: str):
        config = RawConfigParser()
        config.read(properties_file)

        self.__token = config.get('TelegramBot', 'telegramBot.token')
        self.__registered = True

        if not self.set_webhook(config.get('TelegramBot', 'telegramBot.webhook')):
            print("Unsuccessful to connect bot with webhook")
            self.__registered = False
        else:
            print("Success!")

    def __invoke(self, method_name, data=None) -> Optional[reqs.Response]:
        if not self.__registered:
            print("Current bot haven't been registered yet")
            return None
        return reqs.post(TelegramBot.__url.format(token=self.__token, method=method_name), data=data)

    def get_me(self) -> Optional[reqs.Response]:
        return self.__invoke("getMe")

    def get_updates(self) -> Optional[reqs.Response]:
        return self.__invoke("getUpdates")

    def send_message(self,
                     chat_id: Union[int, str],
                     text: str,
                     parse_mode: str = None,
                     reply_markup: ReplyMarkup = None) -> Optional[reqs.Response]:
        data = \
            {
                'chat_id': chat_id,
                'text': text
            }

        if parse_mode:
            data['parse_mode'] = parse_mode
        if reply_markup:
            data['reply_markup'] = json.dumps(remove_nones(reply_markup.to_dict()))

        return self.__invoke(
            method_name="sendMessage",
            data=data
        )

    def send_poll(self,
                  chat_id: Union[int, str],
                  question: str,
                  options: List[str],
                  is_anonymous: bool = True,
                  poll_type: str = "regular",
                  allows_multiple_answers: bool = False,
                  correct_option_id: int = 0) -> Optional[reqs.Response]:
        return self.__invoke(
            method_name="sendPoll",
            data=
            {
                'chat_id': chat_id,
                'question': question,
                'options': json.dumps(options),
                'is_anonymous': is_anonymous,
                'type': poll_type,
                'allows_multiple_answers': allows_multiple_answers,
                'correct_option_id': correct_option_id
            }
        )

    def send_photo(self,
                   chat_id: Union[int, str],
                   file_path: str) -> Optional[reqs.Response]:
        with open(file_path, 'rb') as payload:
            files = {'photo': (file_path, payload, 'png')}
            return reqs.post(
                url=TelegramBot.__url.format(token=self.__token, method="sendPhoto"),
                data=
                {
                    'chat_id': chat_id
                },
                files=files
            )

    def set_commands(self,
                     cmds: List[Tuple[str, str]]) -> Optional[reqs.Response]:
        return self.__invoke(
            method_name="setMyCommands",
            data=
            {
                'commands': json.dumps(
                    list(
                        map(
                            lambda t:
                            {
                                'command': t[0],
                                'description': t[1]
                            },
                            cmds
                        )
                    )
                )
            }
        )

    def set_webhook(self,
                    url: str) -> bool:
        response = self.__invoke(
            method_name="setWebhook",
            data=
            {
                'url': url
            }
        )
        if response.ok:
            return response.json()['ok']
        return False
