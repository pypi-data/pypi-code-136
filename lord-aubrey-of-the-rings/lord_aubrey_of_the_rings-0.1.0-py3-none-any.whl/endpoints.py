from lord_of_the_rings.client import TheOneAPIBase


class LordOfTheRings(TheOneAPIBase):
    """
    TheOneAPI Wrapper Class
    """
    def get_books(self, identifier: str = None, *args, **kwargs):
        """
        Retrieves book(s) from
        :param identifier: ID of a book
        :param args: Additional path(s) added to the resource
        :param kwargs: Query params for pagination, sorting and filtering the result
        :return: json response
        """
        resource = '/book'
        if identifier:
            resource += f'/{identifier}'

            if 'chapter' in args:
                resource += '/chapter'

        return self._make_request(
            'GET',
            self._build_url(resource),
            params=kwargs,
        )

    def get_movies(self, identifier: str = None, *args, **kwargs):
        """
        Retrieves movie(s) from API
        :param identifier: ID of a movie
        :param args: Additional path(s) added to the resource
        :param kwargs: Query params for pagination, sorting and filtering the result
        :return: json response
        """
        resource = '/movie'
        if identifier:
            resource += f'/{identifier}'

            if 'quote' in args:
                resource += '/quote'

        return self._make_request(
            'GET',
            self._build_url(resource),
            params=kwargs,
        )

    def get_characters(self, identifier: str = None, *args, **kwargs):
        """
        Retrieves character(s) from API
        :param identifier: ID of a character
        :param args: Additional path(s) added to the resource
        :param kwargs: Query params for pagination, sorting and filtering the result
        :return: json response
        """
        resource = '/character'
        if identifier:
            resource += f'/{identifier}'

            if 'quote' in args:
                resource += '/quote'

        return self._make_request(
            'GET',
            self._build_url(resource),
            params=kwargs,
        )

    def get_quotes(self, identifier: str = None, **kwargs):
        """
        Retrieves quote(s) from API
        :param identifier: ID of a quote
        :param kwargs: Query params for pagination, sorting and filtering the result
        :return: json response
        """
        resource = '/quote'
        if identifier:
            resource += f'/{identifier}'

        return self._make_request(
            'GET',
            self._build_url(resource),
            params=kwargs,
        )

    def get_chapters(self, identifier: str = None, **kwargs):
        """
        Retrieves chapter(s) from API
        :param identifier: ID of a chapter
        :param kwargs: Query params for pagination, sorting and filtering the result
        :return: json response
        """
        resource = '/chapter'
        if identifier:
            resource += f'/{identifier}'

        return self._make_request(
            'GET',
            self._build_url(resource),
            params=kwargs,
        )
