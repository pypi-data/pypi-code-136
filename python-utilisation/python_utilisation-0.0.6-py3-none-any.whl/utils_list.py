from dataclasses import dataclass


@dataclass
class UtilsList:
    """Class UtilsList."""

    lists: list

    def add_at(self, value, indice:int):
        self.lists.insert(indice, value)
        self.lists.pop(int(indice) + 1)
        
    def remove_at(self, indice):
        self.lists.pop(indice)
