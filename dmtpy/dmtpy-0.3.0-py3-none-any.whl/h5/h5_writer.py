""" Export entites as h5"""
from typing import Dict, Sequence
from enum import Enum
import uuid
import h5py as h5
from dmt.entity import Entity
from dmt.attribute import Attribute
from dmt.blueprint_attribute import BlueprintAttribute


class H5Writer:
    """Write entities to H5 file"""

    def __init__(self, use_external_refs=False):
        self.uuids = dict()
        self.use_external_refs = use_external_refs
        self.external_refs: Dict[str, Entity] = dict()
        self.datasource = None

    def write(self, entities: Sequence[Entity], filename):
        """Write entities to h5 file"""
        # Make sure all referenced enitites has id's
        for entity in entities:
            self.__set_alls_ids(entity)

        with h5.File(filename, "w") as root:
            for idx, entity in enumerate(entities):
                self.__write_root(root, idx, entity)

    def __write_root(self, group: h5.Group, idx, entity: Entity) -> str:
        try:
            name = entity.name
        except AttributeError:
            name = str(idx)
        grp = group.create_group(name)
        self.__write_group(grp, entity)
        return name

    def __write_group(self, group: h5.Group, entity: Entity):
        """Convert to dictionary"""
        blueprint = entity.blueprint
        stype = blueprint.get_path()
        if self.datasource:
            stype = self.datasource + "/" + stype

        group.attrs.create("type", stype)
        _id = self.uuids.get(entity, None)
        if _id:
            group.create_dataset("_id", data=_id)

        for attribute in blueprint.attributes:
            if entity.is_set(attribute):
                self.__write_attribute(group, entity, attribute)

    def __write_attribute(self, group: h5.Group, entity: Entity, attribute: Attribute):
        value = getattr(entity, attribute.name, None)
        if isinstance(attribute, BlueprintAttribute):
            if not attribute.contained:
                # This is a cross reference
                if attribute.has_dimensions():
                    raise Exception("Cross reference array not supported yet")
                reference: Entity = value
                _id = self.uuids.get(reference, None)
                if not _id:
                    if self.use_external_refs:
                        _id = self.external_refs.get(reference, None)
                        if not _id:
                            _id = str(uuid.uuid4())
                            self.external_refs[_id] = reference
                    else:
                        raise Exception("Id not set")
                child_group=group.create_group(attribute.name)
                child_group.create_dataset("_id", data = _id)
            elif attribute.has_dimensions():
                children_group=group.create_group(attribute.name)
                order = []
                for idx, entity in enumerate(value):
                    name=self.__write_root(children_group, idx, entity)
                    order.append(name)
                if len(order)>1:
                    children_group.attrs.create("order", order)
            else:
                child_group=group.create_group(attribute.name)
                self.__write_group(child_group, value)

        else:
            if attribute.is_primitive:
                if attribute.has_dimensions():
                    group.create_dataset(attribute.name, data = value)
                else:
                    if self.__is_optional_default(attribute, value):
                        return None
                    group.create_dataset(attribute.name, data = value)
            else:
                if attribute.is_enum:
                    enum: Enum = value
                    group.create_dataset(attribute.name, data = enum.name)

    def __set_alls_ids(self, entity: Entity):
        for child in entity.all_content():
            for atribute in child.blueprint.blueprint_attributes():
                if not atribute.contained and child.is_set(atribute):
                    self.__set_id(child, atribute)

    def __set_id(self, entity: Entity, attribute: BlueprintAttribute):
        uuids = self.uuids
        value = getattr(entity, attribute.name, None)
        if attribute.has_dimensions():
            entities: Sequence[Entity] = value
            for entity in entities:
                if entity not in uuids:
                    uuids[entity] = str(uuid.uuid4())
        else:
            entity: Entity = value
            if entity not in uuids:
                uuids[entity] = str(uuid.uuid4())

    def __is_optional_default(self, attribute: Attribute, value: any):
        if attribute.optional and attribute.is_primitive:
            return value == attribute.default
        return False
