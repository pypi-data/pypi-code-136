import os.path
from functools import partial

from lotr_api.utils import get_response


class API:
    """
    LOTR API endpoint handler class

    Automatically generated methods:

    - get_books(**filters)
    - get_book(identifier, **filters)
    - get_book_chapters(identifier, **filters)
    - get_movies(**filters)
    - get_movie(identifier, **filters)
    - get_movie_quotes(identifier, **filters)
    - get_characters(**filters)
    - get_character(identifier, **filters)
    - get_character_quotes(identifier, **filters)
    - get_quotes(**filters)
    - get_quote(identifier, **filters)
    - get_chapters(**filters)
    - get_chapter(identifier, **filters)

    """

    def __init__(self, token):
        self.__token = token

        resources = (
            (
                "book",
                "chapter",
            ),
            (
                "movie",
                "quote",
            ),
            (
                "character",
                "quote",
            ),
            ("quote",),
            ("chapter",),
        )

        for resource_set in resources:
            try:
                resource, nested_resource = resource_set
                setattr(
                    self,
                    f"get_{resource}_{nested_resource}s",
                    partial(self.__get_nested, path=resource, nested=nested_resource),
                )
            except ValueError:
                resource = resource_set[0]
            setattr(self, f"get_{resource}s", partial(self.__get, resource))
            setattr(self, f"get_{resource}", partial(self.__get_by_id, path=resource))

    def __get(self, path, **filters):
        return get_response(path, self.__token, **filters)

    def __get_by_id(self, identifier, path, **filters):
        return self.__get(os.path.join(path, identifier), **filters)

    def __get_nested(self, identifier, path, nested, **filters):
        return self.__get(os.path.join(path, identifier, nested), **filters)
