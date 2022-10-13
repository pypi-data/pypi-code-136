from .dataloader import DataLoader


class Property(str):
    __slots__ = ("__dataloader", "__key")

    def __new__(
        cls,
        loader: DataLoader,
        country_code: str,
        name: str,
        locale: str = "en",
    ):
        return super().__new__(
            cls,
            cls.__empty_if_none(loader.lookup(country_code, name, locale=locale)),
        )

    def __init__(
        self,
        loader: DataLoader,
        country_code: str,
        name: str,
        locale: str = "en",
    ):
        self.__dataloader = loader
        self.__key = (country_code, name)

    @property
    def key(self) -> str:
        return self.__key

    def to_locale(self, locale: str) -> str:
        """Get the translation of the given `locale`.

        Returns:
            The translation string, None if not found.
        """
        return self.__empty_if_none(self.__dataloader.lookup(*self.key, locale=locale))

    def __deepcopy__(self, memo):
        """Return a copy of the Property object. Since the object is immutable, we just return self."""
        return self  # Property is read-only

    @classmethod
    def __empty_if_none(cls, value):
        return "" if value is None else value
