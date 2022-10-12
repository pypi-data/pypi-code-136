import asyncio
import pulsectl_asyncio
from typing import Dict
from dbus_next.service import ServiceInterface, method, signal
from dbus_next.signature import Variant


class VolumeInterface(ServiceInterface):
    INAME = "pysysapi.Volume"

    def __init__(self):
        super().__init__(VolumeInterface.INAME)
        self.pulse = pulsectl_asyncio.PulseAsync("pysysapi")
        asyncio.create_task(self._listen_for_events())

    async def _listen_for_events(self):
        await self.pulse.connect()
        async for event in self.pulse.subscribe_events("all"):
            self.event(event.t._value, event.facility._value, event.index)

    @method()
    async def get_sinks(self) -> "aa{sv}":  # type: ignore
        "index name mute"
        " description sample_spec owner_module latency driver"
        " monitor_source monitor_source_name flags configured_latency card"

        def get_sink_dict(sink) -> Dict:
            return {
                "index": Variant("u", sink.index),
                "name": Variant("s", sink.name),
                "mute": Variant("u", sink.mute),
                "description": Variant("s", sink.description),
                "volume_all_chans": Variant("d", sink.volume.value_flat),
                # TODO: "sample_spec": Variant("?", sink.sample_spec),
                "owner_module": Variant("u", sink.owner_module),
                "latency": Variant("u", sink.latency),
                "driver": Variant("s", sink.driver),
                "monitor_source": Variant("u", sink.monitor_source),
                "monitor_source_name": Variant("s", sink.monitor_source_name),
                "flags": Variant("u", sink.flags),
                "configured_latency": Variant("u", sink.configured_latency),
                "card": Variant("u", sink.card),
            }

        return list(map(get_sink_dict, await self.pulse.sink_list()))

    @method()
    async def volume_get_all_chans(self, sink_name: "s") -> "d":  # type: ignore
        sink = await self.pulse.get_sink_by_name(sink_name)
        return await self.pulse.volume_get_all_chans(sink)

    @signal()
    def event(self, type: str, facility: str, index: int) -> "(ssi)":  # type: ignore
        return [type, facility, index]
