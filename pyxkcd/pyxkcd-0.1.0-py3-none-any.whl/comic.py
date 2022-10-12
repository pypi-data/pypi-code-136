import datetime


class Image:
    """
    Represents an image from the xkcd API.

    Attributes
    ----------
    url: str
        The URL of the image.
    alt: str
        The alt text of the image.
    """

    def __init__(self, url: str, alt: str):
        self.__url = url
        self.__alt = alt

    @property
    def url(self):
        return self.__url

    @property
    def alt(self):
        return self.__alt

    def __repr__(self):
        return f"Image(url={self.__url!r}, alt={self.__alt!r})"


class Comic:
    """
    Represents a xkcd comic.

    Attributes
    ----------
    released: datetime.datetime
        The date the comic was released.
    title: str
        The title of the comic.
    num: int
        The number of the comic.
    transcript: str
        The transcript of the comic.
    image: Image
        The image of the comic.
    """

    def __init__(self, response: dict):
        self.__response = response
        self.__released = datetime.datetime(
            int(response["year"]), int(response["month"]), int(response["day"])
        )
        self.__title = response["title"]
        self.__num = response["num"]
        self.__transcript = response["transcript"]
        self.__image = Image(response["img"], response["alt"])

    @property
    def response(self) -> dict:
        return self.__response

    @property
    def released(self) -> datetime.datetime:
        return self.__released

    @property
    def title(self) -> str:
        return self.__title

    @property
    def num(self) -> int:
        return self.__num

    @property
    def image(self) -> Image:
        return self.__image

    @property
    def transcript(self):
        return self.__transcript

    def __eq__(self, __o):
        return self.response == __o.response

    def __dict__(self):
        return self.__response

    def __str__(self):
        return f"{self.num}: {self.title}"

    def __repr__(self):
        return f"<Response({self.__response})>"
