from typing import TypeVar, Generic, List
from telus_bulk.pagination.page_meta_dto import PageMetaDto
from fastapi_camelcase import CamelModel

T = TypeVar("T")


class PageDto(CamelModel):
    def __init__(self, data: List[T], meta: PageMetaDto):
        super().__init__(data=data, meta=meta)

    data: List[T]
    meta: PageMetaDto
