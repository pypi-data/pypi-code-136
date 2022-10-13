from typing import TypeVar, Generic, List
from telus_bulk.pagination.page_meta_dto import PageMetaDto
from fastapi_camelcase import CamelModel

T = TypeVar("T")


class PageDto(CamelModel):
    def __init__(self, data: List[T], pagination_metadata: PageMetaDto):
        super().__init__(data=data, pagination_metadata=pagination_metadata)

    data: List[T]
    pagination_metadata: PageMetaDto
