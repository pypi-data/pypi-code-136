"""Provides loops to keep asyncio running, running minutely checks"""

import asyncio
import logging
import sys
import time
from typing import TYPE_CHECKING

import aiohttp.web

import nawah.data as Data
from nawah.config import Config

from ._common_handlers import (_not_allowed_handler, _not_found_handler,
                               _root_handler)
from ._http_handler import _http_handler
from ._utils import _populate_routes

if TYPE_CHECKING:
    from aiohttp.web import Application

logger = logging.getLogger("nawah")


def _create_error_middleware(overrides):
    @aiohttp.web.middleware
    async def error_middleware(request, handler):
        try:
            response = await handler(request)
            override = overrides.get(response.status)
            if override:
                return await override(request)
            return response
        except aiohttp.web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)
            raise

    return error_middleware


async def _web_loop(app: "Application", /):
    # AsnciIOMotor must be created within scope of asyncio.run to be created in same event loop
    # as AIOHTTP loop
    # [TODO] Figure out another callable to call Data.create_conn, after dropping config_app Utility
    Config.sys.conn = Data.create_conn()
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, "0.0.0.0", Config.port)
    await site.start()
    logger.info("Serving on 0.0.0.0:%s", Config.port)
    while True:
        await asyncio.sleep(60)


def _run_app():
    get_routes, post_routes = _populate_routes()

    logger.debug(
        "Loaded modules: %s",
        {module_name: module.attrs for module_name, module in Config.modules.items()},
    )
    logger.debug(
        "Config has attrs: %s",
        {
            k: str(v)
            for k, v in Config.__dict__.items()
            if not isinstance(v, classmethod) and not k.startswith("_")
        },
    )
    logger.debug("Generated get_routes: %s", get_routes)
    logger.debug("Generated post_routes: %s", post_routes)

    app = aiohttp.web.Application()
    app.middlewares.append(
        _create_error_middleware(
            {
                404: _not_found_handler,
                405: _not_allowed_handler,
            }
        )
    )
    app.router.add_route("GET", "/", _root_handler)
    for route in get_routes:
        app.router.add_route("GET", route, _http_handler)
    for route in post_routes:
        app.router.add_route("POST", route, _http_handler)
        app.router.add_route("OPTIONS", route, _http_handler)
    logger.info("Welcome to Nawah")

    try:
        asyncio.run(_web_loop(app))
    except KeyboardInterrupt:
        if time.localtime().tm_hour >= 21 or time.localtime().tm_hour <= 4:
            msg = "night"
        elif time.localtime().tm_hour >= 18:
            msg = "evening"
        elif time.localtime().tm_hour >= 12:
            msg = "afternoon"
        elif time.localtime().tm_hour >= 5:
            msg = "morning"

        logger.info("Have a great %s!", msg)

        sys.exit()
