""" A Named Entity representing system/SIMOS/NamedEntity"""
from .entity import Entity

class NamedEntity(Entity):
    """ A Named Entity representing system/SIMOS/NamedEntity"""

    def __init__(self,name=None, description="", **kwargs) -> None:
        super().__init__(description,**kwargs)
        self.name = name

    @property
    def name(self) -> str:
        """Get name"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)
