""" Export entites as h5"""
from typing import Sequence,Dict,Callable
from importlib import import_module
import h5py as h5
from dmt.dmt_reader import DMTReader
from dmt.entity import Entity
from dmt.attribute import Attribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.enum_attribute import EnumAttribute
from collections import OrderedDict

class H5Reader:
    """Read entities from H5 file"""

    class Reference:
        """Holds a reference until it can be resolved"""

        def __init__(self,entity, prop: Attribute,uid: str):
            self.entity = entity
            self.prop = prop
            self.uid = uid

    def __init__(self, external_refs: Dict[str,Entity]=None):
        self.entities = dict()
        self.unresolved = list()
        self.external_refs = dict()
        if  external_refs:
            self.external_refs=external_refs
        self.datasource = None


    def read(self,filename) -> Sequence[Entity]:
        """Write entities to h5 file"""
        entities = []
        with h5.File(filename, "r") as root:
            for group in root.values():
                entities.append(self.__read_group(group))

        self.__resolve_all()
        return entities

    def __resolve_all(self):
        for ref in self.unresolved:
            if not self.__resolve(ref):
                raise Exception(f"Unresolved reference: {ref}")


    def __read_group(self,group: h5.Group) -> Entity:
        """ Read entities from Dict """
        entity_type: str=group.attrs["type"]
        constructor = self._resolve_type(entity_type)
        if not constructor:
            raise Exception(f"Unkown entity type {entity_type}")
        entity_instance: Entity = constructor()
        blueprint = entity_instance.blueprint
        for name, node in group.items():
            if name == "_id":
                uid = node[()].decode()
                self.entities[uid] = entity_instance
                continue
            attribute = blueprint.get_attribute(name)
            if not attribute:
                #FIXME
                continue
            if isinstance(attribute, BlueprintAttribute):
                self.__set_blueprint_value(entity_instance,attribute,node)
            elif attribute.is_enum:
                value = node[()].decode()
                self.__set_enum_value(entity_instance,attribute,value)
            else:
                value = node[()]
                if attribute.is_string():
                    setattr(entity_instance,name, value.decode())
                else:
                    setattr(entity_instance,name, value)

        return entity_instance

    def _resolve_type(self, atype: str) -> Callable:
        pkg: any = None
        parts = atype.split("/")
        if self.datasource:
            parts.remove(self.datasource)
        if parts[0] == "":
            del parts[0]
        ename = parts.pop()
        package_path = ".".join(parts)
        try:
            pkg = import_module(package_path)
        except ModuleNotFoundError as error:
            raise Exception(f"Unable to load package {package_path}") from error

        constructor = pkg.__dict__.get(ename)
        return constructor

    def __set_blueprint_value(self,entity_instance: Entity, attribute: BlueprintAttribute,value):
        if attribute.contained:
            self.__set_value(entity_instance,attribute,value)
        else:
            self.__set_reference(entity_instance,attribute,value)

    def __set_reference(self,entity_instance: Entity,prop: Attribute,group: h5.Group):
        uid = group.get("_id")[()].decode()
        ref = self.Reference(entity_instance,prop,uid)
        if not self.__resolve(ref):
            self.unresolved.append(ref)
        return

    def __set_value(self,entity_instance: Entity, attribute: BlueprintAttribute,value):
        if attribute.has_dimensions():
            root: h5.Group = value
            od = OrderedDict()
            children = []
            for name, v in root.items():
                od[name] = self.__read_group(v)

            order = root.attrs.get("order")
            if order is not None:
                sorder = order[()]
                for name in sorder:
                    children.append(od[name])
            else:
                children = od.values()
            setattr(entity_instance,attribute.name, children)
        else:
            setattr(entity_instance,attribute.name, self.__read_group(value) )

    def __resolve(self, ref: Reference):
        value = self.entities.get(ref.uid,self.external_refs.get(ref.uid,None))
        if value:
            setattr(ref.entity,ref.prop.name, value )
            return True

        return False

    def __set_enum_value(self,entity: Entity, attribute: EnumAttribute,value: str):
        """ Convert from string to Enum"""

        constructor = self._resolve_type(attribute.type)
        if not constructor:
            raise Exception(f"Unkown Enum type {attribute.type}")
        evalue = constructor[value]
        setattr(entity,attribute.name, evalue)
