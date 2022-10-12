#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Create an Image-only Blocks Response """


from pprint import pformat

from baseblock import BaseObject


class CreateImageBlock(BaseObject):
    """ Create an Image-only Blocks Response 

    Reference:
        https://github.com/craigtrim/climate-bot/issues/6#issuecomment-1276597202
    """

    def __init__(self):
        """ Change Log

        Created:
            12-Oct-2022
            craigtrim@gmail.com
            *   in response to
                https://github.com/craigtrim/climate-bot/issues/6
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_event_incoming: dict,
                image_url: str) -> dict:
        """ Create and Format Outgoing Slack Events

        Args:
            d_event_incoming (dict): the incoming slack event
            image_url (str): a public URL for a slack image

        Returns:
            dict: the outgoing slack event
        """

        if not image_url or not len(image_url):
            return None

        def get_blocks() -> list:
            return [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": image_url
                    }
                }
            ]

        def get_thread_ts() -> str or None:
            if 'thread_ts' in d_event_incoming:
                return d_event_incoming['thread_ts']

        d_event_outgoing = {
            'channel': d_event_incoming['channel'],
            'blocks': get_blocks(),
            'thread_ts': get_thread_ts(),
        }

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Constructed Image Block",
                f"\tOutgoing Event:\n{pformat(d_event_outgoing)}"]))

        return d_event_outgoing
