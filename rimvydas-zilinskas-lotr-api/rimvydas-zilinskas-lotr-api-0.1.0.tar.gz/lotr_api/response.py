from dataclasses import dataclass

from lotr_api.exceptions import BadResponseStatus


@dataclass
class Response:
    status: int
    docs: dict
    total: int
    page: int
    limit: int
    offset: int
    pages: int
    path: str
    filters: dict = dict

    def get_next(self):
        if self.status != 200:
            raise BadResponseStatus(
                f"Cannot get next page as previous response returned: {self.status}"
            )

        if self.has_next():
            from lotr_api.utils import get_response

            filters = self.filters
            filters["page"] = self.page + 1
            return get_response(self.path, self.__get_token(), **self.filters)

    def has_next(self):
        return self.page < self.pages

    def set_token(self, token):
        setattr(self, "__token", token)

    def __get_token(self):
        return getattr(self, "__token")
