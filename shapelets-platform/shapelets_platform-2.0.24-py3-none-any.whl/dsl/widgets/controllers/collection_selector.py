# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from typing import List

from shapelets.dsl import ArgumentType, ArgumentTypeEnum
from shapelets.dsl.widgets import WidgetNode, AttributeNames
from shapelets.model import Collection, Sequence


class CollectionSelector(WidgetNode):
    def __init__(self,
                 default_collection: Collection = None,
                 default_sequence: Sequence = None,
                 name: str = None,
                 title: str = None,
                 collection_label: str = None,
                 sequence_label: str = None,
                 **additional):
        super().__init__(self.__class__.__name__,
                         name,
                         ArgumentType(ArgumentTypeEnum.SEQUENCE),
                         default_sequence,
                         **additional)
        self.title = title
        self.default_collection = default_collection
        self.default_sequence = default_sequence
        self.collection_label = collection_label
        self.sequence_label = sequence_label

    def to_dict_widget(self):
        collection_selector_dict = super().to_dict_widget()
        if self.title is not None:
            collection_selector_dict[AttributeNames.PROPERTIES.value].update(
                {AttributeNames.TITLE.value: self.title}
            )
        if self.default_collection is not None:
            collection_selector_dict[AttributeNames.PROPERTIES.value].update(
                {AttributeNames.COLLECTION_ID.value: self.default_collection.collection_id}
            )
        if self.default_sequence is not None:
            collection_selector_dict[AttributeNames.PROPERTIES.value].update(
                {AttributeNames.SEQUENCE_ID.value: self.default_sequence.sequence_id}
            )
        if self.collection_label is not None:
            collection_selector_dict[AttributeNames.PROPERTIES.value].update(
                {AttributeNames.COLLECTION_LABEL.value: self.collection_label}
            )
        if self.sequence_label is not None:
            collection_selector_dict[AttributeNames.PROPERTIES.value].update(
                {AttributeNames.SEQUENCE_LABEL.value: self.sequence_label}
            )
        return collection_selector_dict
