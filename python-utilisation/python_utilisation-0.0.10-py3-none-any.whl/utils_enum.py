
from dataclasses import dataclass
from enum import Enum

from python_utilisation.read import read_int


@dataclass
class UtilsEnum:
    """Class Utils Enum."""

    enum:Enum

    @property
    def len(self):
        return len(self.enum)

    def enum_list_key_value(self)-> list:
        """enum list key value."""
        return [(int(key), value.value) for key, value in enumerate(self.enum, 1)]

    def enum_dict_key_value(self)->dict:
        """enum dict key value"""
        return [{"id":int(key), "name": vue.value} for key, vue in enumerate(self.enum, 1)]

    def enum_format(self, texte: str = None):
        """
            enum format
            
            print Enum as (id, name)
        """
        texte = f"Choisir un id correspond dans la liste '{str(self.enum)}'"
        enums = self.enum_list_key_value()
        enums_format = [f"{key[0]}. {key[1]}" for key in enums]
        print(texte, *enums_format, sep="\n")

    def enum_id(self)->list[int]:
        """get ids of enums"""
        return [int(i['id']) for i in self.enum_dict_key_value()]

    def enum_search(self, id:int= None)-> dict:
        """search enum by id"""
        enums_dict =self.enum_dict_key_value()
        enums_ids =self.enum_id()
        if id:
            if id in enums_ids:
                for i in enums_dict: return [i for i in enums_dict if i['id'] == id][0]
        else: return enums_dict
        
    def enum_presentation(self, id_enum: int = None):
        """print presentation de utils enum"""
        self.enum_format()
        id_enum = read_int(self.len)
        return self.enum_search(id_enum)
