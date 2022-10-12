#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Analyze an Incoming Slack Event """


from pprint import pformat
from typing import Any
from typing import Dict

from baseblock import Stopwatch
from baseblock import BaseObject

from slackbot_helper.dmo import UserIdExtract
from slackbot_helper.dmo import MessageTextExtract
from slackbot_helper.dmo import MessageTypeAnalysis
from slackbot_helper.dto import SlackIds
from slackbot_helper.dto import MessageType
from slackbot_helper.dto import IncomingEvent
from slackbot_helper.dto import AnalyzedEvent


class AnalyzeSlackEvent(BaseObject):
    """ Analyze an Incoming Slack Event """

    def __init__(self,
                 bot_ids: SlackIds):
        """ Change Log

        Created:
            1-Apr-2022
            craigtrim@gmail.com
            *   refactored out of 'parse-slack-events'
                https://github.com/grafflr/graffl-core/issues/258#issuecomment-1086258290
        Updated:
            9-Apr-2022
            craigtrim@gmail.com
            *   structural refactoring
                https://github.com/grafflr/graffl-core/issues/277#issuecomment-1094149722
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
            bot_ids (SlackIds): a list of Bot IDs
        """
        BaseObject.__init__(self, __name__)
        self._bot_ids = bot_ids
        self._extract_user_ids = UserIdExtract().process
        self._extract_message_text = MessageTextExtract().process

    @staticmethod
    def _mode_of_address(d_message_type: Dict[str, Any]) -> str:

        if d_message_type['message_type'] in [
            MessageType.H2B_BROADCAST,
            MessageType.H2B_SINGLE,
            MessageType.H2B_MULTI_INIT,
        ]:
            return 'human2bot'

        elif d_message_type['message_type'] in [
            MessageType.B2H_RESPONSE,
        ]:
            return "bot2human"

        return 'bot2bot'

    def _process(self,
                 d_event: IncomingEvent) -> AnalyzedEvent:

        def get_source_user_id() -> str:
            if 'user' in d_event:
                return d_event['user']
            return d_event['bot_id']

        source_user_id = get_source_user_id()
        user_ids = self._extract_user_ids(d_event)
        message_text = self._extract_message_text(d_event)

        d_message_type = MessageTypeAnalysis(
            user_ids=user_ids,
            bot_ids=self._bot_ids,
            message_text=message_text).process()

        mode_of_address = self._mode_of_address(d_message_type)

        return {
            "text_1": message_text,
            "text_2": d_message_type['message_text'],
            "commands": d_message_type['commands'],
            'meta_mode': mode_of_address,
            'meta_type': d_message_type['message_type'].name,
            'user_source': source_user_id,
            'user_target': user_ids[0],
            'user_all': user_ids
        }

    def process(self,
                d_event: IncomingEvent) -> AnalyzedEvent:
        """ Purpose:
            Parses a list of events coming from the Slack RTM API to find bot commands.
        :return dict:
            return the command (str) and channel (str).
        """

        sw = Stopwatch()

        d_analyzed = self._process(d_event)

        if d_event and self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Retrieved Slack Event",
                f"\tTotal Time: {str(sw)}",
                pformat(d_analyzed)]))

        return d_analyzed
