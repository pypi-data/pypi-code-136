# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from cbra.conf import settings
from cbra.ext.google import GoogleTransport
from cbra.ext import ioc
from cbra.ext.ioc.provider import _default # type: ignore
from cbra.ext.ioc.models import DependencyList

from molano.runtime.ioc import GLOBAL_DEPENDENCIES


async def init():
    """Loads the preconfigured dependencies in the default provider."""
    await _default.load_many(DependencyList(items=GLOBAL_DEPENDENCIES)) # type: ignore
    if settings.DEPLOYMENT_ENV != 'local':
        ioc.provide(
            name='MessageTransport',
            value=GoogleTransport(
                project=settings.GOOGLE_HOST_PROJECT,
                command_topic=settings.AORTA_COMMAND_TOPIC,
                command_project=settings.AORTA_COMMAND_PROJECT,
                events_topic=settings.AORTA_EVENT_TOPIC,
                events_project=settings.AORTA_EVENT_PROJECT
            ),
            force=True
        )