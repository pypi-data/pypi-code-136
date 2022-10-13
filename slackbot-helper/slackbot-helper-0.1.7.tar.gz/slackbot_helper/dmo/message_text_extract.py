#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract the Message Text from an Incoming Slack Events """


from typing import List
from typing import Optional
from pprint import pformat

from baseblock import Stopwatch
from baseblock import BaseObject

from slackbot_helper.dto import IncomingEvent


class MessageTextExtract(BaseObject):
    """ Extract the Message Text from an Incoming Slack Events """

    def __init__(self) -> None:
        """ Change Log

        Created:
            24-Mar-2022
            craigtrim@gmail.com
            *   refactored out of 'parse-slack-events'
                https://github.com/grafflr/graffl-core/issues/241
        Updated:
            30-Mar-2022
            craigtrim@gmail.com
            *   minor refactoring
                https://github.com/grafflr/graffl-core/issues/246
        Updated:
            6-Oct-2022
            craigtrim@gmail.com
            *   refactored into 'climate-bot'
        Updated:
            7-Oct-2022
            craigtrim@gmail.com
            *   refactored into 'slackbot-helper'
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def _to_string(results: List[str]) -> str:
        message_text = ' '.join(results)
        if '\n' in message_text:
            message_text = message_text.replace('\n', ' ')
        while '  ' in message_text:
            message_text = message_text.replace('  ', ' ')
        return message_text.strip()

    def _process(self,
                 d_event: dict) -> str or None:

        if 'blocks' in d_event:
            
            message = []
            for block in d_event['blocks']:
            
                if 'elements' in block:
                    
                    for element in block['elements']:
                    
                        for inner in element['elements']:
                    
                            if inner['type'] in ['text', 'rich_text_section']:
                                message.append(inner['text'])
                    
                            elif inner['type'] == 'user':
                                message.append(f"@{inner['user_id']}")
                    
                            elif inner['type'] == 'emoji':
                                pass  # GRAFFL-255; can likely just ignore this
                    
                            elif inner['type'] == 'link':
                                pass  # GRAFFL-395; can likely just ignore this
                    
                            else:
                                raise NotImplementedError(inner['type'])

                elif 'accessory' in block:  # formatted blocks like with Giphy
                    message.append(block['accessory']['alt_text'])

            return self._to_string(message)

        elif 'channel' in d_event:
            message_text = d_event['text']
            while '>' in message_text:
                message_text = message_text.split('>')[-1].strip()
            return self._to_string([message_text])

        elif 'choices' in d_event:
            message = []
            for choice in d_event['choices']:
                message.append(choice['text'])
            return self._to_string(message)

        self.logger.error('\n'.join([
            "Event Structure Not Recognized",
            pformat(d_event)]))

        raise NotImplementedError

    def process(self,
                d_event: IncomingEvent) -> Optional[str]:
        """ Extract Message Text

        Args:
            d_event (dict): the message text from the slack event

        Returns:
            str: the message text (sans usernames and IDs)
        """
        sw = Stopwatch()

        message_text = self._process(d_event)

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Message Text Extraction Completed",
                f"\tTotal Time: {str(sw)}",
                f"\tMessage Text: {message_text}"]))

        return message_text
