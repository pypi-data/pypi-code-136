"""Provides types used in Nawah data module"""

from typing import TYPE_CHECKING, MutableSequence, Protocol, Union

if TYPE_CHECKING:
    from bson import ObjectId

    from ._types import NawahDoc, NawahSession, ResultsArgs


class DataCreateCallable(Protocol):
    """Provides type-hint for implementation of Data.create to use with IOC classes"""

    # pylint: disable=too-few-public-methods

    async def __call__(
        self,
        *,
        session: "NawahSession",
        collection_name: str,
        doc: "NawahDoc",
    ) -> "ResultsArgs":
        ...


class DataUpdateCallable(Protocol):
    """Provides type-hint for implementation of Data.update to use with IOC classes"""

    # pylint: disable=too-few-public-methods

    async def __call__(
        self,
        *,
        session: "NawahSession",
        collection_name: str,
        docs: MutableSequence[Union[str, "ObjectId"]],
        doc: "NawahDoc",
    ) -> "ResultsArgs":
        ...
