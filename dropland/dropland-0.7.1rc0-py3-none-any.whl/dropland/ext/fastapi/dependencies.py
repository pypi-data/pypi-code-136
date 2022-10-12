from typing import Optional

from fastapi import Cookie, Query

from dropland.data.context import get_context


async def query_locale(locale: Optional[str] = Query(None)) -> Optional[str]:
    if locale:
        get_context().data['lang'] = locale
    return locale


async def cookie_locale(locale: Optional[str] = Cookie(None)) -> Optional[str]:
    if locale:
        get_context().data['lang'] = locale
    return locale
