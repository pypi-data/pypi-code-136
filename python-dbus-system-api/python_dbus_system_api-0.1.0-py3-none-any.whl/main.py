from dbus_next.aio.message_bus import MessageBus

import asyncio

from python_dbus_system_api.interfaces.volume import VolumeInterface


async def main_async():
    interfaces = [VolumeInterface()]
    path = "/pysysapi"
    name = "pysysapi.api"
    bus = await MessageBus().connect()
    for interface in interfaces:
        bus.export(path, interface)

    await bus.request_name(name)
    await asyncio.get_event_loop().create_future()


def start_server():
    asyncio.get_event_loop().run_until_complete(main_async())
