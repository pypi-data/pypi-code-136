# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Data class for storing information that is needed to classify an object instance"""

from __future__ import annotations


class ClassIdentifier:

    __delimiter: str = "_"

    def __init__(
        self,
        class_id: int,
        class_name: str,
    ):
        # id of the 'class', respectively the id of the object type
        self.__class_id: int = class_id

        # name of the 'class', respectively the name of the object type
        self.__class_name: str = class_name

    def __eq__(self, other: ClassIdentifier) -> bool:  # type: ignore
        return self.class_id == other.class_id or self.class_name == other.class_name

    def __hash__(self) -> int:
        return hash((self.__class_id, self.__class_name))

    def __repr__(self) -> str:
        return f"{self.class_id}{ClassIdentifier.__delimiter}{self.class_name}"

    @property
    def class_id(self) -> int:
        return self.__class_id

    @property
    def class_name(self) -> str:
        return self.__class_name

    @staticmethod
    def from_str(class_identifier_str: str) -> ClassIdentifier:
        """
        Build a ClassIdentifier object from the given string

        Args:
            class_identifier_str: The string to build the ClassIdentifier from

        Returns:
            The built ClassIdentifier object
        """
        class_identifier_str_split = class_identifier_str.split(ClassIdentifier.__delimiter)

        if len(class_identifier_str_split) != 2:
            raise ValueError(
                f"Could not build ClassIdentifier from '{class_identifier_str}'. "
                f"Please provide it in the format: "
                f"'CLASSID{ClassIdentifier.__delimiter}CLASSNAME'"
            )

        return ClassIdentifier(
            class_id=int(class_identifier_str_split[0]), class_name=class_identifier_str_split[1]
        )
