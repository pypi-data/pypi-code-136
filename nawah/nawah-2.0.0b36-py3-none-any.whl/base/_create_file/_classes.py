"""Provides IOC-style classes for 'create_file' Base Function callable, 'set_file' Utility"""

import datetime
import logging
from typing import TYPE_CHECKING, MutableMapping, Protocol

from nawah.classes import Attr
from nawah.enums import AttrType
from nawah.exceptions import InvalidAttrTypeException
from nawah.utils import extract_attr, validate_doc

from .._shared import FILE_ATTRS
from ..exceptions import NoDocUpdatedException, UtilityModuleDataCallException

if TYPE_CHECKING:
    from nawah.classes import Module
    from nawah.types import (DataCreateCallable, DataUpdateCallable, NawahDoc,
                             NawahSession, Results)

logger = logging.getLogger("nawah")


class SetFileCallable(Protocol):
    """Provides type-hint for 'set_file_callable' of 'CreateFile'"""

    # pylint: disable=too-few-public-methods

    async def __call__(
        self,
        *,
        module_name: str,
        session: "NawahSession",
        doc: "NawahDoc",
        raise_no_success: bool,
    ) -> "Results":
        ...


class CreateFile:
    """IOC-style implementation for 'create_file' Base Function"""

    # pylint: disable=too-few-public-methods

    __modules: MutableMapping[str, "Module"]
    __data_create_callable: "DataCreateCallable"
    __set_file_callable: "SetFileCallable"

    def __init__(
        self,
        modules: MutableMapping[str, "Module"],
        data_create_callable: "DataCreateCallable",
        set_file_callable: "SetFileCallable",
    ):
        self.__modules = modules
        self.__data_create_callable = data_create_callable
        self.__set_file_callable = set_file_callable

    async def __call__(
        self,
        *,
        module_name: str,
        session: "NawahSession",
        doc: "NawahDoc",
    ) -> "Results":
        module = self.__modules[module_name]

        if not module.collection:
            raise UtilityModuleDataCallException(
                module_name=module_name, func_name="create_file"
            )

        if "_id" in doc:
            return await self.__set_file_callable(
                module_name=module_name,
                session=session,
                doc=doc,
                raise_no_success=True,
            )

        file_attr = extract_attr(attrs=module.attrs, path=doc["attr"])

        # For list of files, assert call points to LIST attr, and it contains a FILE attr
        if file_attr.type == AttrType.LIST:
            if file_attr.args["list"][0].type != AttrType.FILE:
                raise InvalidAttrTypeException(
                    attr_type=file_attr.type,
                )

            file_attr = file_attr.args["list"][0]

        # If it is still not a FILE attr raise InvalidAttrTypeException
        if file_attr.type != AttrType.FILE:
            raise InvalidAttrTypeException(attr_type=file_attr.type)

        types_pattern = None
        if file_attr.args["types"]:
            types_pattern = "|".join(file_attr.args["types"])
            # Replace astrisks (*) with dot-astrisks to mark it as valid RegExp pattern
            types_pattern = types_pattern.replace("*", ".*")

        file_doc_attrs = {
            **FILE_ATTRS,
            "file": Attr.TYPED_DICT(
                dict={
                    "name": Attr.STR(),
                    "lastModified": Attr.INT(),
                    "type": Attr.STR(pattern=types_pattern),
                    "size": Attr.INT(),
                    "content": Attr(
                        desc="__sys_attr",
                        type=AttrType.BYTES,
                        args={},
                    ),
                }
            ),
        }

        file_doc = {
            "user": session["user"]["_id"],
            "doc": "000000000000000000000000",
            "attr": doc["attr"],
            "file": {
                "name": doc["name"],
                "lastModified": doc["lastModified"],
                "type": doc["type"],
                "size": len(doc["content"]),
                "content": doc["content"],
            },
            "create_time": datetime.datetime.utcnow().isoformat(),
        }

        validate_doc(mode="create", attrs=file_doc_attrs, doc=file_doc)

        # Execute Data driver create
        results = await self.__data_create_callable(
            session=session, collection_name=f"{module.collection}__file", doc=file_doc
        )

        return {
            "status": 200,
            "msg": f'Created {results["count"]} files',
            "args": results,
        }


class SetFile:
    """IOC-style implementation for 'set_file' Utility"""

    # pylint: disable=too-few-public-methods

    __modules: MutableMapping[str, "Module"]
    __data_update_callable: "DataUpdateCallable"

    def __init__(
        self,
        modules: MutableMapping[str, "Module"],
        data_update_callable: "DataUpdateCallable",
    ):
        self.__modules = modules
        self.__data_update_callable = data_update_callable

    async def __call__(
        self,
        *,
        module_name: str,
        session: "NawahSession",
        doc: "NawahDoc",
        raise_no_success: bool,
    ) -> "Results":
        module = self.__modules[module_name]

        update_results = await self.__data_update_callable(
            session=session,
            collection_name=f"{module.collection}__file",
            docs=[doc["_id"]],
            doc={"doc": doc["doc"]},
        )

        if raise_no_success is True and update_results["count"] == 0:
            raise NoDocUpdatedException(module_name=module_name)

        return {
            "status": 200,
            "msg": f"Updated {update_results['count']} docs",
            "args": update_results,
        }
