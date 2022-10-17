import re
from functools import lru_cache
from pathlib import Path
from typing import Any, ClassVar, Optional, Sequence, Set, Tuple, Type

import autoflake
import black
from datamodel_code_generator import PythonVersion
from datamodel_code_generator.imports import (
    IMPORT_ANY,
    IMPORT_DATE,
    IMPORT_DATETIME,
    IMPORT_DECIMAL,
    IMPORT_TIME,
    IMPORT_UUID,
    Import,
)
from datamodel_code_generator.model import DataModel, DataModelFieldBase
from datamodel_code_generator.parser.openapi import OpenAPIParser
from datamodel_code_generator.types import DataType, DataTypeManager, StrictTypes, Types

IMPORT_TYPED_DICT = Import.from_full_path("typing_extensions.TypedDict")
IMPORT_NOT_REQUIRED = Import.from_full_path("typing_extensions.NotRequired")
IMPORT_BINARY_IO = Import.from_full_path("typing.BinaryIO")

NOT_REQUIRED = "NotRequired"


class _TypedDictDataModel(DataModel):
    TEMPLATE_FILE_PATH: ClassVar[str] = "typed_dict.jinja2"
    BASE_CLASS: ClassVar[str] = "typing_extensions.TypedDict"
    DEFAULT_IMPORTS: ClassVar[Tuple[Import, ...]] = IMPORT_NOT_REQUIRED, IMPORT_BINARY_IO


class _CustomRoot(_TypedDictDataModel):
    TEMPLATE_FILE_PATH: ClassVar[str] = "custom_root.jinja2"


class _TypedDictDataModelField(DataModelFieldBase):
    @property
    def type_hint(self) -> str:
        type_hint = self.data_type.type_hint

        if not type_hint:
            return NOT_REQUIRED
        elif self.nullable is not None:
            if self.nullable:
                return f"{NOT_REQUIRED}[{type_hint}]"
            return type_hint
        elif self.required:
            return type_hint
        return f"{NOT_REQUIRED}[{type_hint}]"


def _get_type_map(data_type: Type[DataType]):
    data_type_int = data_type(type="int")
    data_type_float = data_type(type="float")
    data_type_str = data_type(type="str")
    return {
        Types.integer: data_type_int,
        Types.int32: data_type_int,
        Types.int64: data_type_int,
        Types.number: data_type_float,
        Types.float: data_type_float,
        Types.double: data_type_float,
        Types.decimal: data_type.from_import(IMPORT_DECIMAL),
        Types.time: data_type.from_import(IMPORT_TIME),
        Types.string: data_type_str,
        Types.byte: data_type_str,  # base64 encoded string
        Types.binary: data_type(type="bytes"),
        Types.date: data_type.from_import(IMPORT_DATE),
        Types.date_time: data_type.from_import(IMPORT_DATETIME),
        Types.password: data_type_str,
        Types.email: data_type_str,
        Types.uuid: data_type.from_import(IMPORT_UUID),
        Types.uuid1: data_type.from_import(IMPORT_UUID),
        Types.uuid2: data_type.from_import(IMPORT_UUID),
        Types.uuid3: data_type.from_import(IMPORT_UUID),
        Types.uuid4: data_type.from_import(IMPORT_UUID),
        Types.uuid5: data_type.from_import(IMPORT_UUID),
        Types.uri: data_type_str,
        Types.hostname: data_type_str,
        Types.ipv4: data_type_str,
        Types.ipv6: data_type_str,
        Types.ipv4_network: data_type_str,
        Types.ipv6_network: data_type_str,
        Types.boolean: data_type(type="bool"),
        Types.object: data_type.from_import(IMPORT_ANY, is_dict=True),
        Types.null: data_type.from_import(IMPORT_ANY, is_optional=True),
        Types.array: data_type.from_import(IMPORT_ANY, is_list=True),
        Types.any: data_type.from_import(IMPORT_ANY),
    }


class _TypedDictDataTypeManager(DataTypeManager):
    def __init__(
        self,
        python_version: PythonVersion = PythonVersion.PY_37,
        use_standard_collections: bool = False,
        use_generic_container_types: bool = False,
        strict_types: Optional[Sequence[StrictTypes]] = None,
        use_non_positive_negative_number_constrained_types: bool = False,
    ) -> None:
        super().__init__(
            python_version,
            use_standard_collections,
            use_generic_container_types,
            strict_types,
            use_non_positive_negative_number_constrained_types,
        )
        self.type_map = _get_type_map(self.data_type)

    def get_data_type(self, types: Types, **kwargs: Any) -> DataType:
        return self.type_map[types]


class Result:
    def __init__(self, result: str, /) -> None:
        self._result = result

    @property
    def _root_models(self):
        @lru_cache
        def _get_root_models():
            return re.findall(r"class (\w+).+:", self._result) + re.findall(r"(\w+)\s=\s[\w\[\],]+", self._result)

        return set(_get_root_models())

    def _get_model_definition(self, model: str):
        return (
            re.search(rf"class {model}\(.*:(?:\s{{4}}.*)*", self._result)
            or re.search(r"(\w+)\s=\s[\w\[\],]+", self._result)
        ).group()  # type: ignore

    def _get_initial_models(self):
        if re.search(r"class\sOutput\(.+\n\s{4}pass", self._result):
            return {"Input"}
        else:
            return {"Input", "Output"}

    @staticmethod
    def _remove_unused_model(model: str, result: str):
        return re.sub(rf"class {model}\(.*:(?:\s{{4}}.*)*", "", result)

    def _get_used_models(self, used_models: Set[str], model_pool: Set[str]):
        unused_models = model_pool - used_models
        new_used_models: Set[str] = set()
        for unused_model in unused_models:
            if any(
                [
                    re.search(rf"\W{unused_model}\W", self._get_model_definition(used_model))
                    for used_model in used_models
                ]
            ):
                new_used_models.add(unused_model)
        merged_used_models = used_models | new_used_models
        if new_used_models and merged_used_models != new_used_models:
            new_used_models.update(self._get_used_models(new_used_models, model_pool))
        return new_used_models | used_models

    def _clean_misc(self, result: str):
        replacements = [
            (r"(class\s)(Input)(\()", r"\1JobInput\3"),
            (r"(class\s)(Output)(\()", r"\1JobResults\3"),
            (r"(Output)(\s=\s[\w\[\],]+)", r"JobResults\2"),
            (r"(\s{4}document: )(bytes)", r"\1BinaryIO"),
        ]
        for pattern, replacement in replacements:
            result = re.sub(pattern, replacement, result)
        return result

    def clean(self) -> str:
        used_models = self._get_used_models(self._get_initial_models(), self._root_models)
        unused_models = self._root_models - used_models

        result = self._result
        for model in unused_models:
            result = self._remove_unused_model(model, result)

        result = self._clean_misc(result)
        result = black.format_file_contents(result, mode=black.FileMode(), fast=False)
        result = "".join(autoflake.fix_code(result, remove_all_unused_imports=True))  # type: ignore
        return result


def generate(input: str):
    parser = OpenAPIParser(
        source=input,
        data_model_type=_TypedDictDataModel,
        data_model_root_type=_CustomRoot,
        data_model_field_type=_TypedDictDataModelField,
        data_type_manager_type=_TypedDictDataTypeManager,
        target_python_version=PythonVersion.PY_38,
        use_double_quotes=True,
        use_subclass_enum=True,
        field_constraints=True,
        custom_template_dir=Path(__file__).parent / "custom_templates",
    )
    return Result(parser.parse())
