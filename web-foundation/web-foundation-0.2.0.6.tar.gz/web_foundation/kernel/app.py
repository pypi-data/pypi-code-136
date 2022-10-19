from __future__ import annotations

from functools import partial
from typing import Type, Generic, Callable

import orjson
from sanic import Sanic

from web_foundation.config import AppConf
from web_foundation.extentions.error_handler import ExtendedErrorHandler
from web_foundation.extentions.realtime.rt_broadcaster import RtBroadcaster
from web_foundation.extentions.realtime.rt_connection import RtEventCallback
from web_foundation.extentions.router import ExtRouter
from web_foundation.extentions.sanic_ext_worker import ExtWorker
from web_foundation.kernel.channel import IChannel, IMessage, GenericIMessage
from web_foundation.kernel.container import GenericDependencyContainer
from web_foundation.kernel.dispatcher import IDispatcher, IDispatcherIsolate
from web_foundation.kernel.isolate import Isolate


class App(Generic[GenericDependencyContainer]):
    name: str
    container: GenericDependencyContainer
    sanic: Sanic
    config: AppConf
    dispatcher: IDispatcher
    # listeners: Dict[str, List[AppListener]]
    _rt_listeners = list[tuple[list[Type[IMessage] | str], RtEventCallback, bool]]

    def __init__(self, dependency_container: GenericDependencyContainer,
                 dispatcher: IDispatcher = None, with_addons=False):
        self.name = dependency_container.app_config().app_name
        self.container = dependency_container
        self.sanic = Sanic(self.name, loads=orjson.loads, dumps=orjson.dumps,
                           error_handler=ExtendedErrorHandler())
        self.dispatcher = dispatcher if dispatcher else IDispatcher()
        self._rt_listeners = []
        self.add_isolate("Dispatcher", IDispatcherIsolate, dispatcher=self.dispatcher, add_channel=False, daemon=False)

    def add_isolate(self, name: str, isolate_cls: Type[Isolate], daemon=True, add_channel: bool = True, **kwargs):
        """
        Add process to execute with worker manager
        """
        instance = isolate_cls(name, **kwargs)
        if add_channel:
            self.dispatcher.register_isolate(instance)

        def add_nondaemon(s_app: Sanic):
            nonlocal instance

            def override_manage(ident, func, kwargs, transient=False, daemon=True):
                nonlocal s_app
                container = s_app.manager.transient if transient else s_app.manager.durable
                container.append(
                    ExtWorker(ident, func, kwargs, s_app.manager.context, s_app.manager.worker_state, daemon=daemon))

            s_app.manager.manage = override_manage
            s_app.manager.manage(name, instance.run_forked, {}, daemon=daemon)

        if daemon:
            self.sanic.main_process_ready(
                lambda s_app: s_app.manager.manage(name, instance.run_forked, {}))
        else:
            self.sanic.main_process_ready(lambda s_app: add_nondaemon(s_app))

    def subscribe_worker(self, event_type: list[GenericIMessage | str] | GenericIMessage | str,
                         resolve_callback: RtEventCallback, use_nested_classes: bool = False):
        """
        Subscribe all sanic workers to event[s]
        :param use_nested_classes:
        :param event_type: Name or Class event
        :param resolve_callback: Resolve function
        """
        self._rt_listeners.append((event_type, resolve_callback, use_nested_classes))

    def add_custom_router(self, router: ExtRouter):
        router.ctx.app = self.sanic
        self.sanic.router = router
        self.sanic.router.apply_routes(self.sanic, self.container)

    def _set_sanic_confs(self):
        self.sanic.config.SWAGGER_UI_CONFIGURATION = {
            "docExpansion": 'none'
        }

    def _configure_sanic_main(self):
        async def on_start(s_app: Sanic):
            for i in range(s_app.state.workers):
                channel = IChannel(f"Channel_{i}")
                setattr(s_app.shared_ctx, f"Channel_{i}", channel)
                self.dispatcher.channels.update({f"Channel_{i}": channel})
                # noinspection PyAsyncCall
                self.sanic.add_task(channel.listen_produce(self.dispatcher.on_channel_sent))

        self.sanic.main_process_ready(on_start)

    def _configure_sanic_worker(self):
        async def set_worker_ctx(s_app: Sanic):

            # set channel to ctx
            worker_num = int(s_app.m.name.split('-')[-2])
            s_app.ctx.channel = getattr(s_app.shared_ctx, f"Channel_{worker_num}")
            s_app.ctx.container = self.container
            for service, name in s_app.ctx.container.services():
                service.channel = s_app.ctx.channel
            # add addon loader

            # add broadcaster
            s_app.ctx.rt_broadcaster = RtBroadcaster()
            for event, resolver, use_nested_classes in self._rt_listeners:
                s_app.ctx.channel.add_event_listener(
                    event_type=event,
                    callback=partial(s_app.ctx.rt_broadcaster.broadcast, resolve_callback=resolver),
                    use_nested_classes=use_nested_classes)
            await self.container.init_resources(s_app.ctx.channel)

        self.sanic.before_server_start(set_worker_ctx)

        async def listen_channel(s_app: Sanic):
            # noinspection PyAsyncCall
            s_app.add_task(s_app.ctx.channel.listen_consume())

        self.sanic.after_server_start(listen_channel)

        async def on_stop(s_app: Sanic):
            await self.container.shutdown_resources()

        self.sanic.before_server_stop(on_stop)

    # def _add_listener(self, scope: str, listener: AppListener):
    #     if not self.listeners.get(scope):
    #         self.listeners[scope] = []
    #     self.listeners[scope].append(listener)
    #
    # def before_resources_init(self, listener: AppListener):
    #     self._add_listener("before_resource", listener)
    #
    # def before_app_start(self):
    #     pass

    def run(self, *args, **kwargs):
        self._set_sanic_confs()
        self._configure_sanic_main()
        self._configure_sanic_worker()
        self.sanic.run(*args, **kwargs)


AppListener = Callable[[App], None]
