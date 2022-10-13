#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract the User IDs from an Incoming Slack Event """


from pprint import pformat

from typing import List
from typing import Optional

from baseblock import Stopwatch
from baseblock import BaseObject

from slackbot_helper.dto import SlackIds
from slackbot_helper.dto import IncomingEvent


class UserIdExtract(BaseObject):
    """ Extract the User IDs from an Incoming Slack Event """

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

    def _extract_ids(self,
                     message_text: str) -> Optional[List]:
        """ Extract User IDs from Message Text

        Sample Transformation Steps:
            1.  "@blattero hi how are you with @loqi today?"
            2.  ['', 'blattero hi how are you with ', 'loqi today?']
            3.  ['blattero hi how are you with ', 'loqi today?']
            4.  ['blattero', 'loqi']

        Args:
            message_text (str): the incoming message text

        Returns:
            list or None: a list of 0..* user ids
        """

        # GRAFFL-246-1084930282; no other users addressed
        if '@' not in message_text:
            return None

        lines = [x for x in message_text.split('@') if len(x)]
        lines = [x.split(' ')[0] for x in lines]

        return lines

    def _process(self,
                 d_event: IncomingEvent) -> Optional[List]:

        def log_error(message: str) -> None:
            self.logger.error('\n'.join([
                message,
                "\tStart Event Block ---------------------------",
                f"\t{pformat(d_event)}",
                "\t----------------------------- End Event Block"]))

        # typically an event that comes from a user ...
        if 'blocks' in d_event:
            try:

                user_ids = []  # use list to preserve extraction order
                for block in d_event['blocks']:

                    if 'elements' in block:
                        for element in block['elements']:
                            for inner_element in element['elements']:
                                if inner_element['type'] == 'user':
                                    if inner_element['user_id'] not in user_ids:
                                        user_ids.append(
                                            inner_element['user_id'])

                    elif 'accessory' in block:  # this happens with formatted messages, like when giphy images are returned
                        pass  # TODO: can extract, but for now will pass

                if len(user_ids):
                    return user_ids

                # 20220331, GRAFFL-256-1085404768; no user ids is a normal situation
                return None

            except KeyError:
                log_error("Event Structure Parse Error for Blocks")
                raise ValueError

        # typically an event that comes from a bot ...
        if 'channel' in d_event:
            return self._extract_ids(d_event['text'])

        log_error("Event Structure Not Recognized")
        raise NotImplementedError

    @staticmethod
    def _cleanse(user_id: str) -> str:
        if '>' in user_id:
            user_id = user_id.replace('>', '')
        if '<' in user_id:
            user_id = user_id.replace('<', '')
        return user_id.strip()

    def process(self,
                d_event: IncomingEvent) -> SlackIds:
        """ Extract User Name

        Args:
            d_event (dict): the message text from the slack event
            Sample input:
                https://github.com/grafflr/graffl-core/issues/234

        Returns:
            str: the name of the user who asked the question
            Sample Output:
                U038QP8ND9P
        """

        sw = Stopwatch()

        results = self._process(d_event)
        if results:
            results = [self._cleanse(x) for x in results]
            results = [x.strip() for x in results if x and len(x)]

        if self.isEnabledForDebug:

            if results:
                self.logger.debug('\n'.join([
                    "User ID Extraction Completed",
                    f"\tTotal Time: {str(sw)}",
                    f"\tTotal User IDs: {len(results)}"]))
            else:
                self.logger.debug('\n'.join([
                    "User ID Extraction Completed",
                    f"\tTotal Time: {str(sw)}",
                    "\tNo User IDs Found"]))

        return results
