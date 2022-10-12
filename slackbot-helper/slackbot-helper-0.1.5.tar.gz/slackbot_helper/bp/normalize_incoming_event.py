#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normmalize an Incoming Slack Event """


from uuid import uuid1

from baseblock import EnvIO
from baseblock import BaseObject

from slackbot_helper.svc import AnalyzeSlackEvent
from slackbot_helper.svc import TransformIncomingEvent
from slackbot_helper.dto import SlackIds
from slackbot_helper.dto import IncomingEvent
from slackbot_helper.dto import NormalizedEvent


class NormalizeIncomingEvent(BaseObject):
    """ Normmalize an Incoming Slack Event """

    def __init__(self,
                 bot_ids: SlackIds):
        """ Change Log

        Created:
            7-Oct-2022
            craigtrim@gmail.com
            *   refactored out of climate-bot

        Args:
            bot_ids (SlackIds): a list of Bot IDs
        """
        BaseObject.__init__(self, __name__)
        self._transform = TransformIncomingEvent().process
        self._analyze = AnalyzeSlackEvent(bot_ids).process

    def process(self,
                d_event: IncomingEvent) -> NormalizedEvent:
        """ Enforce Standardized Event Structure

        Args:
            d_event (dict): the incoming slack event

        Returns:
            dict: a structure containing relevant data for all recipe processing
        """

        d_transformed = self._transform(d_event)
        d_analyzed = self._analyze(d_transformed)

        membership_id = str(uuid1()).replace('-', '_')
        return {  # GRAFFL-342
            'event': d_transformed,
            'analysis': d_analyzed,
            'membership': membership_id
        }
