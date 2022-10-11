class EnergiumField:
    code = None

    def as_energium(self):
        return f'^{self.code}{str(self)}'  # noqa

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_energium

    @classmethod
    def validate_energium(cls, v):
        if not cls.code:
            raise TypeError('attribute "code" is required')
        return cls(v)  # noqa

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"
