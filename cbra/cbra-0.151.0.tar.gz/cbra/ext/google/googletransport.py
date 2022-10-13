# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""Declares :class:`GoogleTransport`."""
import aorta


class GoogleTransport(aorta.transport.GoogleTransport):
    command_topic: str
    events_topic: str

    def __init__(self, project: str, command_topic: str, events_topic: str):
        super().__init__(project=project, topic_path=None)
        self.command_topic = command_topic
        self.events_topic = events_topic

    def get_topics(self, message: aorta.models.Message):
        topics = [self.events_topic, f'{self.events_topic}.{message.kind}']
        if message.is_command():
            topics = [self.command_topic]
        return [self.client.topic_path(self.project, x) for x in topics]
