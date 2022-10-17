# import asyncio
# import os
#
# from loguru import logger
# from sanic import Sanic, Request, json
#
# from web_foundation import settings
# from web_foundation.environment.events.settings import SettingsChange
# from web_foundation.kernel.messaging.channel import IChannel
# from web_foundation.kernel.messaging.dispatcher import IDispatcher
#
# settings.DEBUG = True
# settings.METRICS_ENABLE = True
# settings.EVENTS_METRIC_ENABLE = True
#
# app = Sanic("name")
# app.shared_ctx.disp = IDispatcher()
#
#
# async def call_event(event):
#     logger.warning(f"new event {os.getpid()} {event}")
#
#
# def listen_disp(disp: IDispatcher):
#     async def listen(disp):
#         await asyncio.gather(*disp.perform())
#
#     try:
#         asyncio.run(listen(disp))
#     except KeyboardInterrupt:
#         print("done")
#
#
# @app.before_server_start
# async def find_channel(s_app: Sanic):
#     worker_num = int(s_app.m.name.split('-')[-2])
#     channel = getattr(s_app.shared_ctx, f"Channel_{worker_num}")
#     s_app.ctx.channel = channel
#     s_app.ctx.channel.add_event_listener(SettingsChange, call_event)
#
#
# @app.after_server_start
# async def listen(s_app: Sanic):
#     await s_app.ctx.channel.listen_consume()
#
#
# @app.main_process_start
# async def start(s_app: Sanic):
#     for i in range(s_app.state.workers):
#         channel = IChannel(f"Channel_{i}")
#         setattr(s_app.shared_ctx, f"Channel_{i}", channel)
#         s_app.shared_ctx.disp.channels.update({f"Channel_{i}": channel})
#
#
# #
# @app.main_process_ready
# async def ready(s_app: Sanic):
#     s_app.manager.manage("IDispatcher", listen_disp, {"disp": s_app.shared_ctx.disp})  # TODO KeyboardInterrupt signal
#
#
# @app.get("/test")
# async def test(r: Request):
#     logger.warning(f"{os.getpid()}")
#     # logger.warning(r.app.shared_ctx)
#     data = SettingsChange("DEBUG", settings.DEBUG)
#     logger.warning(r.app.m.name)
#     # logger.warning(r.app.ctx.channel.produce_pipe.queue.put(data))
#     await r.app.ctx.channel.produce(data)
#     # r.app.shared_ctx.q: Queue
#     # r.app.shared_ctx.q.put(1, block=False)
#     return json({"ok": "ok"})
#
#
# if __name__ == '__main__':
#     app.run("0.0.0.0", fast=True,dev=True)
#
# """
#  ctx:
#     Channel
#     AddonLoader
#     DepContainer:
#         RTManager
#         AddonService
#         MetricService
#         *Services
#         *Resource
# """
from enum import Enum
from pathlib import Path

if __name__ == '__main__':
    print(Path("../applied_files").joinpath(Path("config")).joinpath(Path("")))
