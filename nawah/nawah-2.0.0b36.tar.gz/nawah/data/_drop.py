from typing import TYPE_CHECKING, Literal

from nawah.config import Config

if TYPE_CHECKING:
    from nawah.types import NawahSession


async def drop(session: "NawahSession", collection_name: str) -> Literal[True]:
    collection = Config.sys.conn[Config.data_name][collection_name]
    await collection.drop()
    return True
