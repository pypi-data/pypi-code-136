#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Analyze the Message Text into Structured Outcomes """


from typing import List
from typing import Optional

from baseblock import EnvIO
from baseblock import Stopwatch
from baseblock import BaseObject

from slackbot_helper.dto import SlackIds
from slackbot_helper.dto import MessageType


class MessageTypeAnalysis(BaseObject):
    """ Analyze the Message Text into Structured Outcomes """

    __d_known_commands = {

        # GRAFFL-304; both of these commands accomplish the same thing ...
        'test': 'NO_PERSIST',
        'no persist': 'NO_PERSIST',
        'johnbot': 'SearchJohnKao',
        'speech pathology': 'SearchSpeechPathology',
        'speech disorder': 'SearchSpeechDisorder',
    }

    def __init__(self,
                 user_ids: SlackIds,
                 message_text: str,
                 bot_ids: SlackIds):
        """ Change Log

        Created:
            30-Mar-2022
            craigtrim@gmail.com
            *   https://github.com/grafflr/graffl-core/issues/246
        Updated:
            4-May-2022
            craigtrim@gmail.com
            *   permit command extraction
                https://github.com/grafflr/graffl-core/issues/304#issuecomment-1117686873
        Updated:
            8-Jun-2022
            craigtrim@gmail.com
            *   remove 'is-known-model' callable in pursuit of
                https://github.com/grafflr/deepnlu/issues/45
        Updated:
            6-Oct-2022
            craigtrim@gmail.com
            *   refactored into 'climate-bot'
        Updated:
            7-Oct-2022
            craigtrim@gmail.com
            *   refactored into 'slackbot-helper'

        Args:
            user_ids (SlackIds): a list of 0..* user ids extracted from the message text
            message_text (str): the actual message text
            bot_ids (SlackIds): a list of Bot IDs
        """
        BaseObject.__init__(self, __name__)
        self._bot_ids = bot_ids
        self._user_ids = user_ids
        self._message_text = message_text

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Initialized Component",
                f"\tMessage Text: {message_text}",
                f"\tUser IDs: {user_ids}"]))

    def _analyze_type(self) -> MessageType:

        bot_ids = [x for x in self._user_ids
                   if x in self._bot_ids]

        human_ids = [x for x in self._user_ids
                     if x not in self._bot_ids]

        if len(bot_ids) == 0:
            if len(human_ids) == 1:
                return MessageType.H2H_SINGLE
            elif len(human_ids) > 1:
                return MessageType.H2H_SINGLE

        if len(human_ids) == 0:
            if len(bot_ids) == 1:
                return MessageType.H2B_SINGLE
            if len(bot_ids) > 1:
                return MessageType.H2B_MULTI_INIT

        if self.isEnabledForWarning:
            self.logger.warning('\n'.join([
                "Unrecognized Message Type",
                f"\tBot IDs: {bot_ids}",
                f"\tHuman IDs: {human_ids}",
                f"\tMessage Text: {self._message_text}"]))

        return MessageType.OTHER

    def _analyze_text(self,
                      message_type: MessageType) -> str:

        if message_type == MessageType.H2B_MULTI_INIT:
            return self._message_text.split(self._user_ids[-1])[-1].strip()

        message_text = self._message_text
        for user_id in self._user_ids:
            message_text = message_text.replace(f"@{user_id}", "")

        while '  ' in message_text:
            message_text = message_text.replace('  ', ' ').strip()

        return message_text.strip()

    def _extract_command(self,
                         message_text: str) -> List[str]:
        """ Extract a Routing Command from the Text

        This is like an easter egg the user can embed in the text
        The Routing Command can be a command to route the text to a particular model
            or to perform (or deny) a particular course of action

        Args:
            message_text (str): the incoming message text

        Returns:
            str or None: the extracted command (if any)
        """

        commands = []
        # if EnvIO.is_false('PERSIST_EVENTS'):
        #     commands.add('NO_PERSIST')

        if ':' not in message_text:
            return list(commands)

        def find_command(value: str) -> Optional[str]:
            if value in self.__d_known_commands:
                return self.__d_known_commands[value]
            return None

        candidate = message_text.split(':')[0].strip().lower()
        commands.append(find_command(candidate))
        candidates = [find_command(x) for x in candidate.split()]
        candidates = [x for x in candidates if x and len(x)]
        [commands.append(x) for x in candidates]

        commands = [x for x in commands if x and len(x)]
        return sorted(commands)

    def process(self) -> dict:

        sw = Stopwatch()

        message_type = self._analyze_type()
        message_text = self._analyze_text(message_type)

        commands = self._extract_command(message_text)
        if commands and len(commands):
            message_text = message_text.split(':')[-1].strip()

        persist_events = EnvIO.exists_as_true('PERSIST_EVENTS')
        if 'NO_PERSIST' in commands:
            commands = [x for x in commands if x != 'NO_PERSIST']
            persist_events = False

        svcresult = {
            'message_type': message_type,
            'message_text': message_text,
            'commands': commands,
            'persist_events': persist_events
        }

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Message Text Analysis Completed",
                f"\tTotal Time: {str(sw)}",
                f"\tMessage Type: {message_type}",
                f"\tMessage Text: {message_text}"]))

        return svcresult
