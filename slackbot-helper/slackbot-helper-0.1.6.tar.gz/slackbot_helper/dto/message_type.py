#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Classify Message Types """


from enum import Enum


class MessageType(Enum):
    """ Classify Message Types """

    # Human-to-Human
    # @Jane Hi!
    H2H_SINGLE = 10

    # Human-to-Multiple-Humans
    # @Bob @Jane Hi!
    H2H_MULTI = 11

    # Human-to-Bot
    # @Chatbot Hi!
    H2B_SINGLE = 20

    # Human-to-Multiple-Bots
    # @Chatbot are you and @Bigbot happy to be here?
    H2B_BROADCAST = 21

    # Human-to-Multiple-Bots; Initialize a Conversation between two bots
    # @Chatbot please tell @Bigbot to take a short hike off a long bridge
    H2B_MULTI_INIT = 22

    # Bot-to-Human Response (no UserIDs)
    # a bot-to-human response that contains no user ids
    B2H_RESPONSE = 30

    # All Other Message types ...
    OTHER = 99
