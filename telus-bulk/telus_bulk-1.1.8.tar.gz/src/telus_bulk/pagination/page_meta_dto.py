from fastapi_camelcase import CamelModel
import math

from pydantic import Field


class PageMetaDto(CamelModel):
    def __init__(self, page: int, limit: int, item_count: int):
        page_count = math.ceil(item_count / limit)
        super().__init__(
            page=page,
            page_size=limit,
            item_count=item_count,
            page_count=page_count,
            has_previous_page=page > 1,
            has_next_page=page < page_count,
        )

    page: int = Field(..., ge=1)
    page_size: int
    item_count: int
    page_count: int
    has_previous_page: bool
    has_next_page: bool
