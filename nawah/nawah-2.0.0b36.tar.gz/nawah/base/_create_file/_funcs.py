"""Provides short-hand functions for 'CreateFile', 'SetFile' IOC classes with runtime config"""

import logging
from typing import TYPE_CHECKING

import nawah.data as Data
from nawah.config import Config

from ._classes import CreateFile, SetFile

if TYPE_CHECKING:
    from nawah.types import NawahDoc, NawahSession, Results

logger = logging.getLogger("nawah")


async def create_file(
    *,
    module_name: str,
    session: "NawahSession",
    doc: "NawahDoc",
) -> "Results":
    """Creates file doc for a module"""

    # This is short-hand wrapper around CreateFile class which injects Config.modules, Data.create

    create_file_implementation = CreateFile(
        modules=Config.modules,
        data_create_callable=Data.create,
        set_file_callable=set_file,
    )

    return await create_file_implementation(
        module_name=module_name, session=session, doc=doc
    )


async def set_file(
    *,
    module_name: str,
    session: "NawahSession",
    doc: "NawahDoc",
    raise_no_success: bool,
) -> "Results":
    """Sets doc value of file created using 'create_file'"""

    # This is short-hand wrapper around SetFile class which injects Config.modules, Data.update

    update_file_implementation = SetFile(
        modules=Config.modules, data_update_callable=Data.update
    )

    return await update_file_implementation(
        module_name=module_name,
        session=session,
        doc=doc,
        raise_no_success=raise_no_success,
    )
