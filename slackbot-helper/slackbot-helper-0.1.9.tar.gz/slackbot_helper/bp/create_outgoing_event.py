#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Format a Response into a "Slack Blocks" object """


from pprint import pformat

from baseblock import BaseObject


class CreateOutgoingEvent(BaseObject):
    """ Format a Response into a "Slack Blocks" object """

    def __init__(self):
        """ Change Log

        Created:
            8-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/grafflr/slackbot/issues/8
        Updated:
            17-Aug-2022
            craigtrim@gmail.com
            *   fix blank-text defect
                https://github.com/grafflr/slackbot/issues/99
        Updated:
            14-Sept-2022
            craigtrim@gmail.com
            *   change 'parse' attribute
                per https://api.slack.com/methods/chat.postMessage#formatting:
                -   By default, URLs will be hyperlinked.
                -   Set parse to none to remove the hyperlinks.
                -   The behavior of parse is different for text formatted with mrkdwn.
                -   By default, or when parse is set to none, mrkdwn formatting is implemented.
                -   To ignore mrkdwn formatting, set parse to full.
        Updated:
            7-Oct-2022
            craigtrim@gmail.com
            *   refactored out of slackbot and renamed from 'format-slack-response'
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_event_incoming: dict,
                output_text: str) -> dict:
        """ Create and Format Outgoing Slack Events

        Args:
            d_event_incoming (dict): the incoming slack event
            output_text (str): the outgoing slack message

        Returns:
            dict: the outgoing slack event
        """

        if not output_text or not len(output_text):
            return None
        
        if not d_event_incoming or type(d_event_incoming) != dict:
            return None

        def get_channel() -> str:
            return d_event_incoming['channel']

        def get_blocks() -> list:

            if 'https:' not in output_text:
                return [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",  # 20220914; use 'mrkdwn' to properly format <@UserId> statements
                            "text": output_text
                        }
                    }
                ]

            tokens = output_text.split('https:')
            url = f"https:{tokens[1].strip().replace(' ', '')}"

            text = tokens[0].strip()
            if not len(text):
                text = ' '  # COR-99; can't have blank text

            return [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": text
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": url,
                        "alt_text": d_event_incoming['text']
                    }
                }
            ]

        def get_thread_ts() -> str or None:
            if 'thread_ts' in d_event_incoming:
                return d_event_incoming['thread_ts']

        d_event_outgoing = {
            'channel': get_channel(),
            'blocks': get_blocks(),
            'thread_ts': get_thread_ts(),
        }

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Constructed Outgoing Event",
                f"\tOutgoing Event:\n{pformat(d_event_outgoing)}"]))

        return d_event_outgoing
