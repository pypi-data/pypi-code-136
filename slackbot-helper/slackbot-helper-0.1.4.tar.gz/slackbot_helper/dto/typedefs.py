#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Define Strict Types for the Project """


from ast import Str
from typing import List
from typing import TypedDict
from typing import NewType


SlackIds = NewType("SlackIds", List[str])


class AnalyzedEvent(TypedDict):
    commands: List[str]
    meta_mode: str
    meta_type: str
    text_1: str
    text_2: str
    user_all: SlackIds
    user_source: str
    user_target: str


class IncomingEvent(TypedDict):
    blocks: List[str]
    channel: str
    team: str
    text: str
    ts: str
    type: str
    user: str


class NormalizedEvent(TypedDict):
    event: IncomingEvent
    analysis: AnalyzedEvent
    membership: str
